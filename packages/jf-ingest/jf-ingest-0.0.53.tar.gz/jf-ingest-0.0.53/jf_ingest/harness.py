import logging
import os
import sys
from datetime import datetime

import urllib3
import yaml

from jf_ingest.jf_jira import IngestionConfig, load_and_push_jira_to_s3
from jf_ingest.jf_jira.auth import JiraDownloadConfig


def setup_harness_logging(logging_level: int):
    """Helper function to setting up logging in the harness"""
    logging.basicConfig(
        level=logging_level,
        format="%(asctime)s %(threadName)s %(levelname)s %(name)s %(message)s"
        if logging_level == logging.DEBUG
        else "%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.getLogger(urllib3.__name__).setLevel(logging.WARNING)


if __name__ == "__main__":
    """
    NOTE: This is a work in progress developer debugging tool.
    it is currently run by using the following command:
       pdm run ingest_harness [--debug]
    and it requires you to have a creds.env and a config.yml file at
    the root of this project
    """
    debug_mode = "--debug" in sys.argv

    # Get Config data for Ingestion Config
    with open("./config.yml") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
        general_config_data = yaml_data["general"]
        jira_config_data = general_config_data["jira_config"]
        jira_config_data["work_logs_pull_from"] = datetime.strptime(
            jira_config_data.get("earliest_issue_dt", datetime.min), "%Y-%m-%d"
        )
        jira_config_data["earliest_issue_dt"] = datetime.strptime(
            jira_config_data.get("earliest_issue_dt", datetime.min), "%Y-%m-%d"
        )
        ingest_config = IngestionConfig(
            timestamp=datetime.utcnow().strftime("%Y%m%d_%H%M%S"),
            jellyfish_api_token=os.getenv("JELLYFISH_API_TOKEN"),
            **general_config_data,
        )
        ingest_config.company_slug = (os.getenv("COMPANY_SLUG"),)
        jira_config = JiraDownloadConfig(**jira_config_data)
        jira_config.url = os.getenv("JIRA_URL")
        jira_config.user = os.getenv("JIRA_USERNAME")
        jira_config.password = os.getenv("JIRA_PASSWORD")
        ingest_config.local_file_path = f"{ingest_config.local_file_path}/{ingest_config.timestamp}"
        # Inject auth data into config
        ingest_config.jira_config = jira_config

    setup_harness_logging(logging_level=logging.DEBUG if debug_mode else logging.INFO)

    load_and_push_jira_to_s3(ingest_config)
