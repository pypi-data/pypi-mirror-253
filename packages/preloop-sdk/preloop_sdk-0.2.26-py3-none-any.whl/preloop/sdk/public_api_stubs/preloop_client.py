import io
import json
import os
from typing import List, Optional

import pandas as pd
import requests

from preloop.sdk.public_api_stubs.api_paths import DatasourceAPIPaths, FeatureAPIPaths
from preloop.sdk.public_api_stubs.exceptions import PreloopError
from preloop.sdk.public_api_stubs.models import (
    DeleteDatasourceRequest,
    DeleteDatasourceResult,
    DeleteFeatureRequest,
    DeleteFeatureResult,
    GetFeatureRequest,
    ListDatasourcesRequest,
    ListDatasourcesResult,
    ListFeatureExecutionsRequest,
    ListFeatureExecutionsResult,
    ListFeaturesRequest,
    ListFeaturesResult,
    ModifyDatasourceRequest,
    ModifyDatasourceResult,
    ModifyFeatureRequest,
    ModifyFeatureResult,
    TriggerFeatureExecutionRequest,
    TriggerFeatureExecutionResult,
    UploadFeatureScriptRequest,
    UploadFeatureScriptResult,
)


class PreloopClient:
    def __init__(
        self,
        endpoint_url: str = "https://api.preloop.com",
        key_id: str = os.getenv("PRELOOP_KEY_ID"),
        secret: str = os.getenv("PRELOOP_SECRET"),
    ) -> None:
        """
        Initialize a new instance of the PreloopClient class.

        Args:
            endpoint_url (str, optional): The endpoint URL of the Preloop API. Defaults to "api.preloop.com".
            key_id (str, optional): The key ID for the Preloop API. Defaults to the value of the "PRELOOP_KEY_ID" environment variable.
            secret (str, optional): The secret for the Preloop API. Defaults to the value of the "PRELOOP_SECRET" environment variable.
        """
        self.endpoint_url = endpoint_url
        self.headers = {
            "User-Agent": "PreloopClient/1.0",
            "key-id": key_id,
            "secret": secret,
        }

    def list_datasources(self, request: Optional[ListDatasourcesRequest] = None) -> ListDatasourcesResult:
        """
        List all datasources. If a request is provided, the request is used to filter the datasources.

        Args:
            request (ListDatasourcesRequest, optional): The request object for listing datasources. If None, a default request is made.

        Returns:
            List[ListDatasourcesResult]: A list of datasources.

        Raises:
            PreloopError: If an HTTP error occurs.
        """
        try:
            if request is None:
                response = requests.post(
                    url=f"{self.endpoint_url}{DatasourceAPIPaths.DATASOURCE_LIST.value}", headers=self.headers
                )
            else:
                response = requests.post(
                    url=f"{self.endpoint_url}{DatasourceAPIPaths.DATASOURCE_LIST.value}",
                    headers=self.headers,
                    json=json.loads(request.model_dump_json()),
                )
            response.raise_for_status()
        except requests.HTTPError as http_error:
            raise PreloopError(message=json.loads(http_error.response.text)["detail"]) from None
        response = ListDatasourcesResult.model_validate_json(json_data=response.text)
        return response

    def delete_datasource(self, request: DeleteDatasourceRequest) -> DeleteDatasourceResult:
        """
        Delete a specific datasource.

        Args:
            request (DeleteDatasourceRequest): The request object for deleting a datasource.

        Returns:
            DeleteDatasourceResult: The result of the delete operation.

        Raises:
            PreloopError: If an HTTP error occurs.
        """
        try:
            response = requests.post(
                url=f"{self.endpoint_url}{DatasourceAPIPaths.DATASOURCE_DELETE.value}",
                headers=self.headers,
                json=json.loads(request.model_dump_json()),
            )
            response.raise_for_status()
        except requests.HTTPError as http_error:
            raise PreloopError(message=json.loads(http_error.response.text)["detail"]) from None
        response = DeleteDatasourceResult.model_validate_json(json_data=response.text)
        return response

    def modify_datasource(self, request: ModifyDatasourceRequest) -> ModifyDatasourceResult:
        """
        Modify a specific datasource.

        Args:
            request (ModifyDatasourceRequest): The request object for modifying a datasource.

        Returns:
            ModifyDatasourceResult: The result of the modify operation.

        Raises:
            PreloopError: If an HTTP error occurs.
        """
        try:
            response = requests.post(
                url=f"{self.endpoint_url}{DatasourceAPIPaths.DATASOURCE_MODIFY.value}",
                headers=self.headers,
                json=json.loads(request.model_dump_json()),
            )
            response.raise_for_status()
        except requests.HTTPError as http_error:
            raise PreloopError(message=json.loads(http_error.response.text)["detail"]) from None
        response = ModifyDatasourceResult.model_validate_json(json_data=response.text)
        return response

    def list_features(self, request: Optional[ListFeaturesRequest] = None) -> ListFeaturesResult:
        """
        List all features. If a request is provided, the request is used to filter the features.

        Args:
            request (ListFeaturesRequest, optional): The request object for listing features. If None, a default request is made.

        Returns:
            ListFeaturesResult: A list of features.

        Raises:
            PreloopError: If an HTTP error occurs.
        """
        try:
            if request is None:
                response = requests.post(
                    url=f"{self.endpoint_url}{FeatureAPIPaths.FEATURE_LIST.value}", headers=self.headers
                )
            else:
                response = requests.post(
                    url=f"{self.endpoint_url}{FeatureAPIPaths.FEATURE_LIST.value}",
                    headers=self.headers,
                    json=json.loads(request.model_dump_json()),
                )
            response.raise_for_status()
        except requests.HTTPError as http_error:
            raise PreloopError(message=json.loads(http_error.response.text)["detail"]) from None
        response = ListFeaturesResult.model_validate_json(json_data=response.text)
        return response

    def delete_feature(self, request: DeleteFeatureRequest) -> DeleteFeatureResult:
        """
        Delete a specific feature.

        Args:
            request (DeleteFeatureRequest): The request object for deleting a feature.

        Returns:
            DeleteFeatureResult: The result of the delete operation.

        Raises:
            PreloopError: If an HTTP error occurs.
        """
        try:
            response = requests.post(
                url=f"{self.endpoint_url}{FeatureAPIPaths.FEATURE_DELETE.value}",
                headers=self.headers,
                json=json.loads(request.model_dump_json()),
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_error:
            raise PreloopError(message=json.loads(http_error.response.text)["detail"]) from None
        response = DeleteFeatureResult.model_validate_json(json_data=response.text)
        return response

    def modify_feature(self, request: ModifyFeatureRequest) -> ModifyFeatureResult:
        """
        Modify a specific feature.

        Args:
            request (ModifyFeatureRequest): The request object for modifying a feature.

        Returns:
            ModifyFeatureResult: The result of the modify operation.

        Raises:
            PreloopError: If an HTTP error occurs.
        """
        try:
            response = requests.post(
                url=f"{self.endpoint_url}{FeatureAPIPaths.FEATURE_MODIFY.value}",
                headers=self.headers,
                json=json.loads(request.model_dump_json()),
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_error:
            raise PreloopError(message=json.loads(http_error.response.text)["detail"]) from None
        response = ModifyFeatureResult.model_validate_json(json_data=response.text)
        return response

    def get_feature(self, request: GetFeatureRequest):
        """
        Get a specific feature.

        Args:
            request (GetFeatureRequest): The request object for getting a feature.

        Returns:
            DataFrame: A DataFrame containing the feature data.

        Raises:
            PreloopError: If an HTTP error occurs.
        """
        try:
            response = requests.post(
                url=f"{self.endpoint_url}{FeatureAPIPaths.FEATURE_GET.value}",
                headers=self.headers,
                json=json.loads(request.model_dump_json()),
                stream=True,
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_error:
            raise PreloopError(message=json.loads(http_error.response.text)["detail"]) from None
        buffer = io.BytesIO()
        for chunk in response.iter_content():
            buffer.write(chunk)
        buffer.seek(0)
        df = pd.read_parquet(buffer)
        return df

    def upload_feature_script(self, request: UploadFeatureScriptRequest) -> UploadFeatureScriptResult:
        """
        Upload a feature script.

        Args:
            request (UploadFeatureScriptRequest): The request object for uploading a feature script.

        Returns:
            UploadFeatureScriptResult: The result of the upload operation.

        Raises:
            PreloopError: If an HTTP error occurs or if there's an issue with the file.
        """
        try:
            with open(request.file_path, "rb") as script:
                response = requests.post(
                    url=f"{self.endpoint_url}{FeatureAPIPaths.FEATURE_UPLOAD_SCRIPT.value}",
                    headers=self.headers,
                    data=json.loads(request.model_dump_json(exclude=["file_path"])),
                    files={"script": script},
                )
                response.raise_for_status()
        except requests.exceptions.HTTPError as http_error:
            raise PreloopError(message=json.loads(http_error.response.text)["detail"]) from None
        except Exception as e:
            raise PreloopError(message=str(e)) from None
        response = UploadFeatureScriptResult.model_validate_json(json_data=response.text)
        return response

    def list_feature_executions(
        self, request: Optional[ListFeatureExecutionsRequest] = None
    ) -> ListFeatureExecutionsResult:
        """
        List all feature executions. If a request is provided, the request is used to filter the executions.

        Args:
            request (ListExecutionsRequest, optional): The request object for listing executions. If None, a default request is made.

        Returns:
            ListExecutionsResult: A list of executions.

        Raises:
            PreloopError: If an HTTP error occurs.
        """
        try:
            if request is None:
                response = requests.post(
                    url=f"{self.endpoint_url}{FeatureAPIPaths.FEATURE_LIST_EXECUTIONS.value}", headers=self.headers
                )
            else:
                response = requests.post(
                    url=f"{self.endpoint_url}{FeatureAPIPaths.FEATURE_LIST_EXECUTIONS.value}",
                    headers=self.headers,
                    json=json.loads(request.model_dump_json()),
                )
            response.raise_for_status()
        except requests.HTTPError as http_error:
            raise PreloopError(message=json.loads(http_error.response.text)["detail"]) from None
        response = ListFeatureExecutionsResult.model_validate_json(json_data=response.text)
        return response

    def trigger_feature_execution(self, request: TriggerFeatureExecutionRequest) -> TriggerFeatureExecutionResult:
        """
        Trigger a manual feature execution.

        Args:
            request (TriggerFeatureExecutionRequest): The request object for triggering a feature execution.

        Returns:
            TriggerFeatureExecutionResult: The result of the trigger operation.

        Raises:
            PreloopError: If an HTTP error occurs.
        """
        try:
            response = requests.post(
                url=f"{self.endpoint_url}{FeatureAPIPaths.FEATURE_TRIGGER_EXECUTION.value}",
                headers=self.headers,
                json=json.loads(request.model_dump_json()),
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_error:
            raise PreloopError(message=json.loads(http_error.response.text)["detail"]) from None
        response = TriggerFeatureExecutionResult.model_validate_json(json_data=response.text)
        return response
