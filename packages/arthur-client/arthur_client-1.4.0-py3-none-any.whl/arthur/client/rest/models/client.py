from typing import Optional, Any, Union, Dict, List, Tuple
from http import HTTPStatus
from requests.cookies import RequestsCookieJar
from requests import Response

# import http client
from arthur.client.http.requests import HTTPClient

from arthur.client.rest.models.models import (
    ExpandEnum,
    IDTypeEnum,
    ModelAttribute,
    ModelExpand,
    ModelHealthResponse,
    ModelObject,
    ModelPinnedColumns,
    ModelPinnedColumnsPatchRequest,
    ModelRequest,
    ModelUpdateRequest,
    OutputType,
    PaginatedAttributeResponse,
    PaginatedModelResponse,
    PaginatedTagResponse,
    Tag,
    TagUpdateRequest,
)


PATH_PREFIX = "/api"


class ArthurModelsClient:
    """
    A Python client to interact with the Arthur Models API
    """

    def __init__(self, http_client: HTTPClient):
        """
        Create a new ArthurModelsClient from an HTTPClient

        :param http_client: the :class:`~arthurai.client.http.requests.HTTPClient` to use for underlying requests
        """
        self.http_client = http_client
        self.http_client.set_path_prefix(PATH_PREFIX)

    def get_paginated_models(
        self,
        include_archived: Optional[bool] = False,
        latest_version_sequence_nums: Optional[bool] = False,
        display_name: Optional[str] = None,
        input_types: Optional[List[str]] = None,
        output_types: Optional[List[OutputType]] = None,
        statuses: Optional[List[str]] = None,
        tag: Optional[List[str]] = None,
        model_group_ids: Optional[List[str]] = None,
        created_since: Optional[str] = None,
        expand: Optional[ModelExpand] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort: Optional[str] = None,
    ) -> PaginatedModelResponse:
        """
        Returns a paginated response of all the models within an organization

        :param include_archived:
        :param latest_version_sequence_nums:
        :param display_name:
        :param input_types:
        :param output_types:
        :param statuses:
        :param tag:
        :param model_group_ids:
        :param created_since:
        :param expand:
        :param page:
        :param page_size:
        :param sort: Must be supplied in the format [column_name] to denote asc sort by this column OR -[column_name] to denote desc sort by this column
        """

        params: Dict[str, Any] = {}
        if include_archived is not None:
            params["include_archived"] = include_archived
        if latest_version_sequence_nums is not None:
            params["latest_version_sequence_nums"] = latest_version_sequence_nums
        if display_name is not None:
            params["display_name"] = display_name
        if input_types is not None:
            params["input_types"] = input_types
        if output_types is not None:
            params["output_types"] = output_types
        if statuses is not None:
            params["statuses"] = statuses
        if tag is not None:
            params["tag"] = tag
        if model_group_ids is not None:
            params["model_group_ids"] = model_group_ids
        if created_since is not None:
            params["created_since"] = created_since
        if expand is not None:
            params["expand"] = expand.value
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["page_size"] = page_size
        if sort is not None:
            params["sort"] = sort

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/models", params=params, validation_response_code=200
        )
        return PaginatedModelResponse(**parsed_resp)

    def create_model(self, json_body: ModelRequest) -> ModelObject:
        """
        Creates a new model object

        The model must have at least two attributes - one in stages (`NON_INPUT_DATA`, `PIPELINE_INPUT`), and one in stage `PREDICTED_VALUE`. On the successful execution of this API, an async process is run to get the model ready to accept inferences. The model will be in the `Creating` state until the async process is complete. Once the async process is complete, the model will be in the `Ready` state - when it is ready to accept inferences. The current status of the model can be retrieved using the `GET /api/v3/models/{model_id}` API, using the model ID returned in this response. If the model onboarding fails, the model will be in the `CreationFailed` state and onboarding can be retried by calling the `/api/v3/models/{model_id}/retry` endpoint.

        :param json_body:
        """

        parsed_resp: Dict[str, Any] = self.http_client.post(  # type: ignore
            f"/v3/models",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=201,
        )
        return ModelObject(**parsed_resp)

    def get_model_by_id(
        self,
        model_id: str,
        id_type: Optional[IDTypeEnum] = IDTypeEnum("id"),
        expand: Optional[ExpandEnum] = None,
    ) -> ModelObject:
        """
        Retrieve a specific model object

        :param model_id:
        :param id_type:
        :param expand:
        """

        params: Dict[str, Any] = {}
        if id_type is not None:
            params["id_type"] = id_type.value
        if expand is not None:
            params["expand"] = expand.value

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/models/{model_id}", params=params, validation_response_code=200
        )
        return ModelObject(**parsed_resp)

    def update_model(
        self,
        model_id: str,
        json_body: ModelUpdateRequest,
        id_type: Optional[IDTypeEnum] = IDTypeEnum("id"),
        expand: Optional[ExpandEnum] = None,
    ) -> ModelObject:
        """
        Updates an existing model object

        If attributes are included, then the model's attributes will be replaced with the ones provided. Attributes can only be replaced if the model has no inferences. The model's attributes will remain unchanged if attributes are excluded from the request.

        :param model_id:
        :param json_body:
        :param id_type:
        :param expand:
        """

        params: Dict[str, Any] = {}
        if id_type is not None:
            params["id_type"] = id_type.value
        if expand is not None:
            params["expand"] = expand.value

        parsed_resp: Dict[str, Any] = self.http_client.put(  # type: ignore
            f"/v3/models/{model_id}",
            json=json_body.dict(by_alias=True, exclude_none=True),
            params=params,
            validation_response_code=200,
        )
        return ModelObject(**parsed_resp)

    def archive_model(
        self,
        model_id: str,
        id_type: Optional[IDTypeEnum] = IDTypeEnum("id"),
        expand: Optional[ExpandEnum] = None,
    ) -> Response:
        """
        Archives an existing model object

        It will delete any compute resources for the model but will not delete inference data. The model will no longer appear in the Arthur Dashboard.

        :param model_id:
        :param id_type:
        :param expand:
        """

        params: Dict[str, Any] = {}
        if id_type is not None:
            params["id_type"] = id_type.value
        if expand is not None:
            params["expand"] = expand.value

        raw_resp: Response = self.http_client.delete(  # type: ignore
            f"/v3/models/{model_id}",
            params=params,
            validation_response_code=204,
            return_raw_response=True,
        )
        return raw_resp

    def modelsmodel_idretry(self, model_id: str) -> Response:
        """
        Re-trigger model provisioning workflow for this model

        This functionality is only available if the model status is Creation Failed.

        :param model_id:
        """

        raw_resp: Response = self.http_client.post(  # type: ignore
            f"/v3/models/{model_id}/retry",
            validation_response_code=200,
            return_raw_response=True,
        )
        return raw_resp

    def get_paginated_model_attributes(
        self,
        model_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort: Optional[str] = None,
    ) -> PaginatedAttributeResponse:
        """
        Returns a paginated response of a model's attributes

        :param model_id:
        :param page:
        :param page_size:
        :param sort: Must be supplied in the format [column_name] to denote asc sort by this column OR -[column_name] to denote desc sort by this column
        """

        params: Dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["page_size"] = page_size
        if sort is not None:
            params["sort"] = sort

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/models/{model_id}/attributes",
            params=params,
            validation_response_code=200,
        )
        return PaginatedAttributeResponse(**parsed_resp)

    def replace_model_attributes(
        self, model_id: str, json_body: List["ModelAttribute"]
    ) -> Response:
        """
        Updates all of a model's attributes

        If the model already has inferences, only the attribute labels and category labels can be updated. Note that this is a \"put\" so all attributes must be included in the request unless they should be deleted. To update a specific attribute, use the /models/{model_id}/attributes/{attribute_id} and to update a subset of attributes use the patch endpoint. Attribute ids should be included for attributes that already exist, otherwise we will attempt to create a new attribute. Any alert rules created for the model prior to this call will be archived.

        :param model_id:
        :param json_body:
        """

        raw_resp: Response = self.http_client.put(  # type: ignore
            f"/v3/models/{model_id}/attributes",
            json=[x.dict(by_alias=True, exclude_none=True) for x in json_body],
            validation_response_code=204,
            return_raw_response=True,
        )
        return raw_resp

    def delete_all_model_attributes(self, model_id: str) -> Response:
        """
        Deletes all of a model's attributes

        Attributes can only be deleted if no inferences exist for this model. Any alert rules created for the model prior to this call will be archived.

        :param model_id:
        """

        raw_resp: Response = self.http_client.delete(  # type: ignore
            f"/v3/models/{model_id}/attributes",
            validation_response_code=204,
            return_raw_response=True,
        )
        return raw_resp

    def update_model_attributes(
        self, model_id: str, json_body: List["ModelAttribute"]
    ) -> Response:
        """
        Updates a subset of a model's attributes

        If the model already has inferences, only the attribute labels and category labels can be updated. Attribute ids should be included for attributes that already exist, otherwise we will attempt to create a new attribute.

        :param model_id:
        :param json_body:
        """

        raw_resp: Response = self.http_client.patch(  # type: ignore
            f"/v3/models/{model_id}/attributes",
            json=[x.dict(by_alias=True, exclude_none=True) for x in json_body],
            validation_response_code=204,
            return_raw_response=True,
        )
        return raw_resp

    def get_model_attribute_by_id(
        self, model_id: str, attribute_id: str
    ) -> ModelAttribute:
        """
        Gets the model attribute

        :param model_id:
        :param attribute_id:
        """

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/models/{model_id}/attributes/{attribute_id}",
            validation_response_code=200,
        )
        return ModelAttribute(**parsed_resp)

    def update_model_attribute(
        self, model_id: str, attribute_id: str, json_body: ModelAttribute
    ) -> ModelAttribute:
        """
        Updates a model attribute

        If the model already has inferences then only the label and category labels can be updated.

        :param model_id:
        :param attribute_id:
        :param json_body: A model attribute. Note that an attribute can only have categories if it is categorical and bins if it is not categorical, it can never have both.
        """

        parsed_resp: Dict[str, Any] = self.http_client.put(  # type: ignore
            f"/v3/models/{model_id}/attributes/{attribute_id}",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=200,
        )
        return ModelAttribute(**parsed_resp)

    def delete_model_attribute(self, model_id: str, attribute_id: str) -> Response:
        """
        Deletes the model attribute

        An attribute can only be deleted if the model does not have any inferences.

        :param model_id:
        :param attribute_id:
        """

        raw_resp: Response = self.http_client.delete(  # type: ignore
            f"/v3/models/{model_id}/attributes/{attribute_id}",
            validation_response_code=204,
            return_raw_response=True,
        )
        return raw_resp

    def get_model_pinned_columns(self, model_id: str) -> ModelPinnedColumns:
        """
        Returns the pinned columns to be displayed to the user for the model's \"Inferences Deep Dive\" page

        Each item in the \"columns\" section of the response corresponds to either a model attribute name or a pre-defined column name for non-attribute columns such as inference_id, partner_inference_id, inference_timestamp, anomaly_score, or raw_anomaly_score.

        :param model_id:
        """

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/models/{model_id}/pinned_columns", validation_response_code=200
        )
        return ModelPinnedColumns(**parsed_resp)

    def set_model_pinned_columns(
        self, model_id: str, json_body: ModelPinnedColumns
    ) -> ModelPinnedColumns:
        """
        Sets the pinned columns to be displayed to the user for the model's \"Inferences Deep Dive\" page

        Each item in the \"columns\" section of the request corresponds to either a model attribute name or a pre-defined column name for non-attribute columns such as inference_id, partner_inference_id, inference_timestamp, anomaly_score, or raw_anomaly_score. The order of the columns in the request will be the order in which the columns will be displayed in the UI. This request overwrites any existing pinned columns for the model.

        :param model_id:
        :param json_body:
        """

        parsed_resp: Dict[str, Any] = self.http_client.put(  # type: ignore
            f"/v3/models/{model_id}/pinned_columns",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=200,
        )
        return ModelPinnedColumns(**parsed_resp)

    def delete_model_pinned_columns(self, model_id: str) -> Response:
        """
        Deletes the pinned columns for the model

        This will result in the pinned columns for the model being reset on the \"Inferences Deep Dive\".

        :param model_id:
        """

        raw_resp: Response = self.http_client.delete(  # type: ignore
            f"/v3/models/{model_id}/pinned_columns",
            validation_response_code=204,
            return_raw_response=True,
        )
        return raw_resp

    def add_or_remove_model_pinned_columns(
        self, model_id: str, json_body: ModelPinnedColumnsPatchRequest
    ) -> ModelPinnedColumns:
        """
        Removes columns from the existing list of pinned columns for the model specified in columns_to_remove and appends columns specified in columns_to_add to the end of the list of pinned columns for the model

        This updates the columns that will be displayed on the \"Inferences Deep Dive\" page. The order of the columns in the request will be the order in which the columns will be displayed in the UI.

        :param model_id:
        :param json_body:
        """

        parsed_resp: Dict[str, Any] = self.http_client.patch(  # type: ignore
            f"/v3/models/{model_id}/pinned_columns",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=200,
        )
        return ModelPinnedColumns(**parsed_resp)

    def get_model_health_score(self, model_id: List[str]) -> ModelHealthResponse:
        """
        Returns the most recent model health scores for the requested models

        If the score is null and timestamp is null, it means the score has not been calculated yet for this model. If the score is null and the timestamp is not null, it means there was no data for the model from the last month for calculating a model health score.

        :param model_id:
        """

        params: Dict[str, Any] = {"model_id": model_id}

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/models/health", params=params, validation_response_code=200
        )
        return ModelHealthResponse(**parsed_resp)

    def get_paginated_tags(
        self, page: Optional[int] = None, page_size: Optional[int] = None
    ) -> PaginatedTagResponse:
        """
        Get all registered tags

        :param page:
        :param page_size:
        """

        params: Dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["page_size"] = page_size

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/tags", params=params, validation_response_code=200
        )
        return PaginatedTagResponse(**parsed_resp)

    def update_tag(self, tag_name: str, json_body: TagUpdateRequest) -> Tag:
        """
        Update a specific tag by name

        :param tag_name:
        :param json_body:
        """

        parsed_resp: Dict[str, Any] = self.http_client.put(  # type: ignore
            f"/v3/tags/{tag_name}",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=200,
        )
        return Tag(**parsed_resp)

    def delete_tag(self, tag_name: str) -> Response:
        """
        Delete a specific tag by name

        :param tag_name:
        """

        raw_resp: Response = self.http_client.delete(  # type: ignore
            f"/v3/tags/{tag_name}",
            validation_response_code=204,
            return_raw_response=True,
        )
        return raw_resp

    def add_tag_to_model(self, model_id: str, tag_name: str) -> Tag:
        """
        Add an existing or new tag to a model

        :param model_id:
        :param tag_name:
        """

        parsed_resp: Dict[str, Any] = self.http_client.put(  # type: ignore
            f"/v3/models/{model_id}/tags/{tag_name}", validation_response_code=200
        )
        return Tag(**parsed_resp)

    def unlink_tag_from_a_model(self, model_id: str, tag_name: str) -> Response:
        """
        Unlinks the tag from the model

        If tag is not linked to any other model, it deletes the tag as well.

        :param model_id:
        :param tag_name:
        """

        raw_resp: Response = self.http_client.delete(  # type: ignore
            f"/v3/models/{model_id}/tags/{tag_name}",
            validation_response_code=200,
            return_raw_response=True,
        )
        return raw_resp
