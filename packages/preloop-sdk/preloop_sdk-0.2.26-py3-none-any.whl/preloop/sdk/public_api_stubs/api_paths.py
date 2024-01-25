from enum import Enum


class DatasourceAPIPaths(str, Enum):
    """
    The different API paths for the datasource API are defined in this
    enum. There are 4 main endpoints that all start with the parent
    word datasource:

    datasource/create: Used to create a new datasource.
    datasource/list: List all the datasources that are available for a given account.
    datasource/describe: Used to describe a given datasource.
    datasource/delete: Used to delete a given datasource.
    datasource/modify: Used to modify a given datasource.
    """

    DATASOURCE_LIST = "/api/datasource/list"
    DATASOURCE_DELETE = "/api/datasource/delete"
    DATASOURCE_MODIFY = "/api/datasource/modify"


class FeatureAPIPaths(str, Enum):
    """
    The different API paths for the feature API are defined in this
    enum. There are 5 main endpoints that all start with the parent
    word feature:

    feature/create: Used to create a new feature.
    feature/list: List all the features that are available for a given account.
    feature/describe: Used to describe a given feature.
    feature/delete: Used to delete a given feature.
    feature/modify: Used to modify a given feature.
    """

    FEATURE_LIST = "/api/feature/list"
    FEATURE_DELETE = "/api/feature/delete"
    FEATURE_MODIFY = "/api/feature/modify"
    FEATURE_GET = "/api/feature/get"
    FEATURE_EXPERIMENTAL_GET = "/api/feature/experimental/get"
    FEATURE_UPLOAD_SCRIPT = "/api/feature/upload-script"
    FEATURE_LIST_EXECUTIONS = "/api/feature/list-executions"
    FEATURE_TRIGGER_EXECUTION = "/api/feature/trigger-execution"
