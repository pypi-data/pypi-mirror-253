"""Initialize the alation_service subpackage of cdh_dav_python package"""
# allow absolute import from the root folder
# whatever its name is.
# from cdh_dav_python.az_storage_service import az_storage_queue


import sys  # don't remove required for error handling
import os


# Import from sibling directory ..\databricks_service
OS_NAME = os.name

sys.path.append("..")
if OS_NAME.lower() == "nt":
    print("cdc_metadata_service: windows")
    sys.path.append(os.path.dirname(os.path.abspath(__file__ + "\\..")))
    sys.path.append(os.path.dirname(os.path.abspath(__file__ + "\\..\\..")))
    sys.path.append(os.path.dirname(os.path.abspath(__file__ + "\\..\\..\\..")))
else:
    print("cdc_metadata_service: non windows")
    sys.path.append(os.path.dirname(os.path.abspath(__file__ + "/..")))
    sys.path.append(os.path.dirname(os.path.abspath(__file__ + "/../..")))
    sys.path.append(os.path.dirname(os.path.abspath(__file__ + "/../../..")))

import cdh_dav_python.databricks_service.notebook
import cdh_dav_python.databricks_service.secret_scope
import cdh_dav_python.databricks_service.workspace
import cdh_dav_python.databricks_service.dataset_crud
import cdh_dav_python.databricks_service.dataset_core
import cdh_dav_python.databricks_service.dataset_convert
import cdh_dav_python.databricks_service.dataset_extract
import cdh_dav_python.databricks_service.database
import cdh_dav_python.databricks_service.cluster

__all__ = [
    "database",
    "dataset_convert",
    "dataset_core",
    "dataset_crud",
    "dataset_extract",
    "notebook",
    "repo_core",
    "secret_scope",
    "workspace",
    "cluster",
    "sql",
]
