import enum
import json
import tempfile
from dataclasses import dataclass, field
from datetime import datetime
from typing import TextIO, Union

from dateutil import parser

from jf_ingest.utils import format_datetime_to_ingest_timestamp

JELLYFISH_API_BASE = "https://app.jellyfish.co"


class JiraAuthMethod(enum.Enum):
    BasicAuth = 1
    AtlassianConnect = 2


# Needs to subclass str to be serializable
class IngestionType(str, enum.Enum):
    AGENT = "AGENT"
    DIRECT_CONNECT = "DIRECT_CONNECT"


@dataclass
class IssueMetadata:
    id: str
    key: str
    updated: datetime
    project_id: str = (
        None  # NOTE: This field is optionally set, and generally only used for detected re-keys
    )
    # The following fields are used for detecting redownloads
    epic_link_field_issue_key: str = None
    parent_field_issue_key: str = None
    parent_id: str = None

    def __post_init__(self):
        """Post Init is called here to properly type everything by doing typecasts"""
        self.id = str(self.id)
        self.key = str(self.key)
        self.updated = (
            self.updated if isinstance(self.updated, datetime) else parser.parse(self.updated)
        )

        # Sanity recasts to make sure everything is a string
        if self.project_id:
            self.project_id = str(self.project_id)
        if self.epic_link_field_issue_key:
            self.epic_link_field_issue_key = str(self.epic_link_field_issue_key)
        if self.parent_field_issue_key:
            self.parent_field_issue_key = str(self.parent_field_issue_key)
        if self.parent_id:
            self.parent_id = str(self.parent_id)

    @staticmethod
    def deserialize_json_str_to_issue_metadata(
        json_str: str,
    ) -> Union["IssueMetadata", list["IssueMetadata"]]:
        """Helper function to deserialize a JSON type object to an IssueMetadata object, or a list of IssueMetadata Objects

        Raises:
            Exception: Raises an expection if the provided json str is not a valid JSON str

        Returns:
            _type_: Either a list of IssueMetadata Objects, or an IssueMetadata Object
        """
        json_data: Union[list, dict] = json.loads(json_str)
        if type(json_data) == list:
            list_of_issue_metadata = []
            for item in json_data:
                item['updated'] = datetime.fromisoformat(item['updated'])
                list_of_issue_metadata.append(IssueMetadata(**item))
            return list_of_issue_metadata
        elif type(json_data) == dict:
            json_data['updated'] = datetime.fromisoformat(json_data['updated'])
            return IssueMetadata(**json_data)
        else:
            raise Exception(
                f'Unrecognized type for deserialize_json_str_to_issue_metadata, type={type(json_data)}'
            )

    @staticmethod
    def from_json(
        json_source: Union[str, bytes, TextIO]
    ) -> Union["IssueMetadata", list["IssueMetadata"]]:
        """Generalized wrapper for the deserialize_json_str_to_issue_metadata function, which deserializes JSON Strings to Python objects

        Returns:
            _type_: Either a list of IssueMetadata objects or an IssueMetaData object, depending on what was supplied
        """
        if isinstance(json_source, str):
            return IssueMetadata.deserialize_json_str_to_issue_metadata(json_source)
        elif isinstance(json_source, bytes):
            return IssueMetadata.deserialize_json_str_to_issue_metadata(json_source.decode("utf-8"))
        elif isinstance(json_source, TextIO):
            json_str = json_source.read()
            return IssueMetadata.deserialize_json_str_to_issue_metadata(json_str)

    @staticmethod
    def to_json_str(issue_metadata: Union["IssueMetadata", list["IssueMetadata"]]) -> str:
        """This is a STATIC helper function that can serialize both a LIST of issue_metadata and a singluar
        IssueMetadata to a JSON string!

        Args:
            issue_metadata (Union[&quot;IssueMetadata&quot;, list[&quot;IssueMetadata&quot;]]): Either a list of IssueMetadata, or a singluar IssueMetadata object

        Returns:
            str: A serialized JSON str
        """

        def _serializer(value):
            if isinstance(value, datetime):
                return value.isoformat()
            elif isinstance(value, IssueMetadata):
                return value.__dict__
            else:
                return str(value)

        return json.dumps(issue_metadata, default=_serializer)

    @staticmethod
    def init_from_jira_issue(issue: dict, project_id: str = None, skip_parent_data: bool = False):
        fields: dict = issue.get("fields", {})
        return IssueMetadata(
            id=issue["id"],
            key=issue["key"],
            project_id=project_id,
            updated=parser.parse(fields.get("updated")) if fields.get("updated") else None,
            parent_id=fields.get("parent", {}).get("id") if not skip_parent_data else None,
            parent_field_issue_key=fields.get("parent", {}).get("key")
            if not skip_parent_data
            else None,
        )

    @staticmethod
    def init_from_jira_issues(issues=list[dict], skip_parent_data: bool = False):
        return [
            IssueMetadata.init_from_jira_issue(issue, skip_parent_data=skip_parent_data)
            for issue in issues
        ]

    # Define a hashing function so that we can find uniqueness
    # easily using sets
    def __hash__(self) -> str:
        return hash(self.id)

    def __eq__(self, __o) -> bool:
        return hash(self) == hash(__o)


@dataclass
class JiraAuthConfig:
    # Provides an authenticated connection to Jira, without the additional
    # settings needed for download/ingest.
    company_slug: str = None
    url: str = None
    # NOTE: Used in the User-Agent header. Not related
    # to the Jellyfish Agent
    user_agent: str = "jellyfish/1.0"
    # Used for Basic Auth
    user: str = None
    password: str = None
    personal_access_token: str = None
    # Used for Atlassian Direct Connect
    jwt_attributes: dict[str, str] = field(default_factory=dict)
    bypass_ssl_verification: bool = False
    required_email_domains: bool = False
    is_email_required: bool = False
    available_auth_methods: list[JiraAuthMethod] = field(default_factory=list)
    connect_app_active: bool = False


@dataclass
class JiraDownloadConfig(JiraAuthConfig):
    # Indicates whether the email augmentation should be performed. This is needed
    # when testing connect-driven data refreshes locally since the connect app used
    # for testing does not (and can not) have the required "Email" permission. As
    # such, this allows us to skip that step when necessary.
    should_augment_emails: bool = True

    # Jira Server Information
    gdpr_active: bool = None

    include_fields: list[str] = None
    exclude_fields: list[str] = None
    # User information
    force_search_users_by_letter: bool = False
    search_users_by_letter_email_domain: str = None

    # Projects information
    include_projects: list[str] = None
    exclude_projects: list[str] = None
    include_project_categories: list[str] = None
    exclude_project_categories: list[str] = None

    # Boards/Sprints
    download_sprints: bool = False

    # Issues
    skip_issues: bool = False
    only_issues: bool = False
    full_redownload: bool = False
    earliest_issue_dt: datetime = datetime.min
    issue_download_concurrent_threads: int = 1
    # Dict of Issue ID (str) to IssueMetadata Object
    jellyfish_issue_metadata: list[IssueMetadata] = None
    jellyfish_project_ids_to_keys: dict = None

    # worklogs
    download_worklogs: bool = False
    # Potentially solidify this with the issues date, or pull from
    work_logs_pull_from: datetime = datetime.min

    # Jira Ingest Feature Flags
    feature_flags: dict = field(default_factory=dict)


@dataclass
class IngestionConfig:
    # upload info
    save_locally: bool = True
    upload_to_s3: bool = False
    local_file_path: str = None
    company_slug: str = None
    timestamp: str = None

    # Jira Auth Info and Download Configuration
    jira_config: JiraDownloadConfig = None

    # JF specific config
    jellyfish_api_token: str = None
    jellyfish_api_base: str = JELLYFISH_API_BASE
    ingest_type: IngestionType = None

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = format_datetime_to_ingest_timestamp(datetime.utcnow())

        if not self.local_file_path:
            self.local_file_path = f"{tempfile.TemporaryDirectory().name}/{self.timestamp}"
