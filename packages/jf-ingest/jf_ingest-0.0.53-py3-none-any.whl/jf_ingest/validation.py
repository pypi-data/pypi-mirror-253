import json
import logging
from dataclasses import asdict, dataclass, field
from typing import Union

from jira import JIRA, JIRAError
from requests.exceptions import RequestException

from jf_ingest.config import IngestionType
from jf_ingest.jf_jira.auth import JiraAuthMethod, get_jira_connection
from jf_ingest.config import JiraAuthConfig, JiraDownloadConfig
from jf_ingest.jf_jira.downloaders import download_users
from jf_ingest.utils import retry_for_429s

# NOTE:
# Logger.info will log to stdout AND to our log file.
# We do NOT want to log any passwords or usernames.
# To be extra safe, use print instead of logger.log within validation if you think data could be sensitive.
logger = logging.getLogger(__name__)


@dataclass
class JiraConnectionHealthCheckResult:
    """
    Representing the result of a Jira connnection healthcheck report.
    """

    successful: bool

    # The version of Jira that is being run
    server_version: str = None

    # Total list of projects accessible
    accessible_projects: list[str] = field(default_factory=list)

    # Projects included in the ingestion configuration to be downloaded but inaccessible from the validator.
    included_inaccessible_projects: list[str] = field(default_factory=list)

    # How many users the validator can access
    num_accessible_users: int = 0

    # Permissions granted to the user.
    granted_permissions: list[str] = field(default_factory=list)

    # Whether we have been able to receive an X-ANODE-ID header from the Jira connection.
    # This means the customer is a Jira Data Center customer.
    returns_anode_id_header: bool = False

    @classmethod
    def from_dict(cls, body: dict):
        return cls(**body)


@dataclass
class GitConnectionHealthCheckResult:
    """
    Representing the result of a Git connection healthcheck report.
    """

    instance_slug: str

    successful: bool

    # Git server information
    # This may be experimental for now -- we need to see if we can get this from all git providers
    server_version: str = None

    # Dict of project name : repo list of repos we can access
    accessible_projects_and_repos: dict[str, list] = field(default_factory=dict)

    # list of repos explicitly included in the config but inaccessible with our credentials
    included_inaccessible_repos: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, body: dict):
        return cls(**body)


@dataclass
class IngestionHealthCheckResult:
    """
    Dataclass representing the result of a pre-ingestion permission healthcheck run.
    """

    ingestion_type: IngestionType

    # Whether the healthcheck result was fully successful
    fully_successful: bool = False

    # Customers may have multiple git configs, so we want to account for that with multiple healthcheck results.
    # The key here should be the instance slug.
    git_connection_healthcheck: list[GitConnectionHealthCheckResult] = field(default_factory=list)

    jira_connection_healthcheck: JiraConnectionHealthCheckResult = None

    def __post_init__(self):
        """
        Sets the fully_successful field based on the successful fields on the jira and git inputs.
        """
        jira_successful = (
            self.jira_connection_healthcheck.successful
            if self.jira_connection_healthcheck
            else False
        )

        # If we have a non-empty git healthcheck result list, ensure all its members are successful.
        git_successful = bool(self.git_connection_healthcheck) and all(
            [x.successful for x in self.git_connection_healthcheck]
        )

        self.fully_successful = jira_successful and git_successful

    def to_dict(self) -> dict:
        """
        Converts to a dictionary representation.

        Returns: The IngestionHealthCheckResult as a dict.

        """
        return asdict(self)

    def to_json(self) -> str:
        """
        Converts to a JSON string.

        Returns: The IngestionHealthCheckResult as a JSON representation.

        """
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, body: str):
        """
        Deserializes a JSON string into an IngestionHealthCheckResult

        Args:
            body:

        Returns: The IngestionHealthCheckResult as a properly nested dataclass

        """
        healthcheck_dict = json.loads(body)

        # We need to do this because Python dataclasses won't natively deserialize a dict representation of a nested
        # dataclass (without third-party packages), so we intercept the list[dict] result
        # and convert it into a list[dataclass].

        new_git_healthcheck_list = []

        for healthcheck_result in healthcheck_dict["git_connection_healthcheck"]:
            parsed_result = GitConnectionHealthCheckResult.from_dict(healthcheck_result)
            new_git_healthcheck_list.append(parsed_result)

        healthcheck_dict["git_connection_healthcheck"] = new_git_healthcheck_list

        healthcheck_dict["jira_connection_healthcheck"] = (
            JiraConnectionHealthCheckResult.from_dict(
                healthcheck_dict["jira_connection_healthcheck"]
            )
            if healthcheck_dict["jira_connection_healthcheck"]
            else None
        )

        return cls(**healthcheck_dict)


def _attempt_anode_id_header_check(jira_connection: JIRA) -> bool:
    """

    Args:
        jira_connection: The Jira Connection to query over

    Returns: Whether the X-ANODEID header exists on the response.
    If it does, this means the customer is Jira Data Center.

    """
    try:
        logger.info("==> Getting Jira deployment type...")

        res = jira_connection._session.get(jira_connection._get_url("serverInfo"))
        headers = res.headers

        if "X-ANODEID" in headers:
            logger.info(
                "Response headers contains X-ANODEID! Customer is running Jira Data Center."
            )

            return True
        else:
            logger.info(
                "Response headers does not contain X-ANODEID! Customer is NOT running Jira Data Center."
            )

            return False

    except Exception:
        # This is a pretty hacky check using private members of the jira connection class
        # So we can't rely on it always working. If it breaks we should just return False
        # and move on.
        logger.error("Unable to get X-ANODEID headers from request!")

        return False


def get_jira_version(jira_connection: JIRA) -> str | None:
    """

    Args:
        jira_connection: The Jira connection

    Returns: the string representation of the Jira server version.

    """

    logger.info("==> Getting Jira version...")

    server_info = jira_connection.server_info()

    jira_version = server_info["version"] if "version" in server_info.keys() else None

    logger.info(f"Found Jira version as {jira_version}")

    return jira_version


def get_jira_permissions(jira_connection: JIRA) -> list[str]:
    """
    Gets the Jira permissions we know about for this user (experimental)
    Args:
        jira_connection: The jira connection to request over.

    Returns: A list of permissions that the user has.

    """

    logger.info("==> Getting Jira permissions...")

    # These are most of the permissions that Jira says are built-in, per this doc:
    # https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-permission-schemes/#built-in-permissions
    # We can pare this down if we decide we don't care about any of these.
    permission_set = {
        "ADMINISTER_PROJECTS",
        "BROWSE_PROJECTS",
        "VIEW_READONLY_WORKFLOW",
        "ASSIGNABLE_USER",
        "ASSIGN_ISSUES",
        "CLOSE_ISSUES",
        "CREATE_ISSUES",
        "DELETE_ISSUES",
        "EDIT_ISSUES",
        "LINK_ISSUES",
        "MODIFY_REPORTER",
        "MOVE_ISSUES",
        "RESOLVE_ISSUES",
        "SCHEDULE_ISSUES",
        "SET_ISSUE_SECURITY",
        "TRANSITION_ISSUES",
        "ADD_COMMENTS",
        "DELETE_ALL_COMMENTS",
        "DELETE_OWN_COMMENTS",
        "EDIT_ALL_COMMENTS",
        "EDIT_OWN_COMMENTS",
        "DELETE_ALL_WORKLOGS",
        "DELETE_OWN_WORKLOGS",
        "EDIT_ALL_WORKLOGS",
        "EDIT_OWN_WORKLOGS",
        "WORK_ON_ISSUES",
    }

    params = {"permissions": ", ".join(list(permission_set))}

    # Jira has some changes here, and we want to be backwards and forwards compatible.
    # Our version of the Jira client does *not* support this parameter right now, so we manually do it.
    # If we update the Jira version we can instead do jira_connection.my_permissions
    # https://developer.atlassian.com/cloud/jira/platform/change-notice-get-my-permissions-requires-permissions-query-parameter/#let-s-see-the-code

    permissions = jira_connection._get_json("mypermissions", params=params)

    granted_permissions = []

    for key, value in permissions["permissions"].items():
        if value["havePermission"]:
            granted_permissions.append(key)

    logger.info(f"Found granted permissions as {granted_permissions}")

    return granted_permissions


def validate_jira(
    config: Union[JiraDownloadConfig, JiraAuthConfig]
) -> JiraConnectionHealthCheckResult:
    """
    Validates jira configuration and credentials. Returns a JiraHealthcheckResult object
    representing whether the check was successful and what the errors were, if any.
    Modified from the original Jira validation logic in the Agent.
    """

    healthcheck_result = JiraConnectionHealthCheckResult(successful=True)

    print("\nJira details:")
    print(f"  URL:      {config.url}")
    print(f"  Username: {config.user}")

    if config.user and config.password:
        print("  Password: **********")
    elif config.personal_access_token:
        print("  Token: **********")
    else:
        logger.error("No Jira credentials found in Jira authentication config!")
        healthcheck_result.successful = False

        return healthcheck_result

    # test Jira connection
    try:
        logger.info("==> Testing Jira connection...")
        jira_connection = get_jira_connection(
            config=config, auth_method=JiraAuthMethod.BasicAuth, max_retries=1
        )
        jira_connection.myself()

        healthcheck_result.server_version = get_jira_version(jira_connection)
        healthcheck_result.returns_anode_id_header = _attempt_anode_id_header_check(jira_connection)
        healthcheck_result.granted_permissions = get_jira_permissions(jira_connection)

    except JIRAError as e:
        print(e)

        print("Response:")
        print("  Headers:", e.headers)
        print("  URL:", e.url)
        print("  Status Code:", e.status_code)
        print("  Text:", e.text)

        if "Basic authentication with passwords is deprecated." in str(e):
            logger.error(
                f"Error connecting to Jira instance at {config.url}. Please use a Jira API token, see https://confluence.atlassian.com/cloud/api-tokens-938839638.html"
            )
        else:
            logger.error(
                f"Error connecting to Jira instance at {config.url}, please validate your credentials. Error: {e}"
            )

        healthcheck_result.successful = False

        return healthcheck_result

    except RequestException as e:
        logger.error(f"RequestException when validating Jira! Message: {e}")

        # Print debugging information related to the request exception
        if e.request:
            print("Request:")
            print("  URL:", e.request.method, e.request.url)
            print("  Body:", e.request.body)
        else:
            print('RequestException contained no "request" value.')

        if e.response:
            print("Response:")
            print("  Headers:", e.response.headers)
            print("  URL:", e.response.url)
            print("  Status Code:", e.response.status_code)
            print("  Text:", e.response.text)
        else:
            print('RequestException contained no "response" value.')

        healthcheck_result.successful = False

        return healthcheck_result

    except Exception as e:
        raise

    # test jira users permission
    try:
        logger.info("==> Testing Jira user browsing permissions...")
        user_count = len(
            download_users(
                jira_basic_connection=jira_connection,
                jira_atlas_connect_connection=None,
                gdpr_active=config.gdpr_active,
            )
        )
        logger.info(f"The agent is aware of {user_count} Jira users.")

        healthcheck_result.num_accessible_users = user_count

    except Exception as e:
        logger.error(
            f'Error downloading users from Jira instance at {config.url}, please verify that this user has the "browse all users" permission. Error: {e}'
        )
        healthcheck_result.successful = False

    # test jira project access
    logger.info("==> Testing Jira project permissions...")
    accessible_projects = [p.key for p in retry_for_429s(jira_connection.projects)]

    logger.info(f"The agent has access to projects {accessible_projects}.")

    healthcheck_result.accessible_projects = accessible_projects

    inaccessible_projects = []

    if config.include_projects:
        for proj in config.include_projects:
            if proj not in accessible_projects:
                inaccessible_projects.append(proj)

    healthcheck_result.included_inaccessible_projects = inaccessible_projects

    if inaccessible_projects:
        project_list_str = ", ".join(inaccessible_projects)
        logger.warn(
            f"\nERROR: Unable to access the following projects explicitly included in the config file! {project_list_str}."
        )
        healthcheck_result.successful = False

    return healthcheck_result
