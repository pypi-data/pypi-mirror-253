import uuid
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


# Datasource models
class SQLConnectionParams(BaseModel):
    user_name: str
    host_name: str
    port_number: int
    database_name: str
    table_name: str
    schema_name: str | None = None


class SQLAuthParams(BaseModel):
    password: str


class S3ConnectionDetails(BaseModel):
    bucket_name: str
    object_key: str


class SQLConnectionDetails(BaseModel):
    connection_params: SQLConnectionParams
    auth_params: SQLAuthParams


class ListDatasourcesRequest(BaseModel):
    datasource_id: uuid.UUID


class DataSourceDetails(BaseModel):
    id: str
    team: Optional[str] = None
    datasource_name: str
    datasource_description: Optional[str] = None
    datasource_type: str
    connection_details: SQLConnectionDetails | S3ConnectionDetails
    datasource_details: Optional[Dict[Any, Any]] = None
    creation_date: str
    last_updated: str | None


class ListDatasourcesResult(BaseModel):
    datasources: List[DataSourceDetails]


class DeleteDatasourceRequest(BaseModel):
    datasource_id: uuid.UUID


class DeleteDatasourceResult(BaseModel):
    message: str
    details: Dict[str, Any] | List[Dict[str, Any]] | None


class DatasourceIdentifierField(BaseModel):
    datasource_id: uuid.UUID


class ModifiableDatasourceFields(BaseModel):
    datasource_name: Optional[str] = None
    datasource_description: Optional[str] = None
    connection_details: Optional[SQLConnectionDetails | S3ConnectionDetails] = None


class ModifyDatasourceRequest(BaseModel):
    fields: DatasourceIdentifierField
    modfield: ModifiableDatasourceFields


class ModifyDatasourceResult(BaseModel):
    message: str
    details: Dict[str, Any] | List[Dict[str, Any]] | None


# Feature models
class ListFeaturesRequest(BaseModel):
    feature_id: uuid.UUID


class FeatureDetails(BaseModel):
    id: str
    creation_date: Optional[str] = None
    last_updated: Optional[str] = None
    datasource_names: List[str]
    feature_name: str
    feature_description: str = Field(
        title="Feature Description", max_length=400, default="The description for this feature"
    )
    column_types: Dict[Any, Any]
    feature_cols: List[str]
    id_cols: List[str]
    target_cols: Optional[List[str]] = None
    scheduling_expression_string: Optional[str] = None
    versioning: bool = False
    latest_version: int
    feature_drift_enabled: bool
    team: Optional[str] = None


class ListFeaturesResult(BaseModel):
    features: List[FeatureDetails]


class DeleteFeatureRequest(BaseModel):
    feature_id: uuid.UUID


class DeleteFeatureResult(BaseModel):
    message: str
    details: Dict[str, Any] | List[Dict[str, Any]] | None


class FeatureIdentifierField(BaseModel):
    feature_id: uuid.UUID


class ModifiableFeatureFields(BaseModel):
    feature_name: str
    feature_description: Optional[str] = None
    update_freq: Optional[str] = None


class ModifyFeatureRequest(BaseModel):
    fields: FeatureIdentifierField
    modfield: ModifiableFeatureFields


class ModifyFeatureResult(BaseModel):
    message: str
    details: Dict[str, Any] | List[Dict[str, Any]] | None


class GetFeatureRequest(BaseModel):
    feature_id: str
    version: int | None = None


class CreationMethod(str, Enum):
    PARSER = "parser"
    INCEPTION = "inception"


class UploadFeatureScriptRequest(BaseModel):
    file_path: str
    creation_method: CreationMethod
    scheduling_expression: str | None = None
    versioning: bool = False


class UploadFeatureScriptResult(BaseModel):
    message: str
    details: Dict[str, Any] | List[Dict[str, Any]] | None


class ListFeatureExecutionsRequest(BaseModel):
    execution_id: uuid.UUID


class FeatureExecution(BaseModel):
    id: str
    status: str
    execution_type: str
    record_date: str
    reason: Optional[str] = None


class ListFeatureExecutionsResult(BaseModel):
    executions: List[FeatureExecution]


class TriggerFeatureExecutionRequest(BaseModel):
    feature_id: uuid.UUID


class TriggerFeatureExecutionResult(BaseModel):
    message: str
    details: Dict[str, Any] | List[Dict[str, Any]] | None
