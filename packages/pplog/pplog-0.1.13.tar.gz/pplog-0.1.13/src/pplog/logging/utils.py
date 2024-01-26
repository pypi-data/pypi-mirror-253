""" Logging utils module """


import json
from typing import Dict


def get_databricks_log_properties(dbutils, config: Dict) -> Dict:  # type: ignore
    """Get databricks log properties to setup logging with a unique job run identifier
    from databricks-notebook-context.
    If notebook submitted as databricks-job: `cluster-id.job-id.run-id`.
    If notebook submitted manually: `cluster-id.notebook-name.notebook-id`
    :param dbutils: Dbutils, databricks utilities class
    :param config: project config
    :return: dict, with databricks properties to uniquely identify job run
    """
    context = json.loads(dbutils.notebook.entry_point.getDbutils().notebook().getContext().toJson())
    cluster = context["tags"]["clusterId"]
    job = context["tags"].get("jobId") or context["extraContext"]["notebook_path"].split("/")[-1]
    run = context.get("currentRunId") or context["tags"]["notebookId"]
    mandant_id = config["filter_mandant"]
    databricks_properties = {
        "stage": config["project"]["stage"],
        "deployment": config["deployment_branch"],
        "job_id": f"{cluster}.{job}.{run}",
        "country_name": config["country_mandant"][mandant_id],
    }
    return databricks_properties
