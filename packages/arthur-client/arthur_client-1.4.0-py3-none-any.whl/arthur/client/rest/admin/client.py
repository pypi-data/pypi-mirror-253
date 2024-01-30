from typing import Optional, Any, Union, Dict, List, Tuple
from http import HTTPStatus
from requests.cookies import RequestsCookieJar
from requests import Response

# import http client
from arthur.client.http.requests import HTTPClient

from arthur.client.rest.admin.models import (
    CustomRBACRequest,
    LoginRequest,
    NewOrganizationRequest,
    OrgExpand,
    Organization,
    OrganizationLimits,
    OrganizationUsage,
    PaginatedOrganizations,
    PaginatedUsageResponse,
    PermissionRequest,
    RolesRequest,
    SetCurrentOrganizationRequest,
    UpdateOrganizationRequest,
    UsageCategory,
    UsageRollups,
    User,
)


PATH_PREFIX = "/api"


class ArthurAdminClient:
    """
    A Python client to interact with the Arthur Admin API
    """

    def __init__(self, http_client: HTTPClient):
        """
        Create a new ArthurAdminClient from an HTTPClient

        :param http_client: the :class:`~arthurai.client.http.requests.HTTPClient` to use for underlying requests
        """
        self.http_client = http_client
        self.http_client.set_path_prefix(PATH_PREFIX)

    def login(self, json_body: LoginRequest) -> Tuple[User, RequestsCookieJar]:
        """
        If the login attempt is successful, the user will be returned in the response body and an HttpOnly, set-cookie \"Authorization\" header will be returned that contains a JWT to be used in subsequent requests to the API in either the \"Authorization\" or cookie header

        :param json_body:
        """

        raw_resp: Response = self.http_client.post(  # type: ignore
            f"/v3/login",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=200,
            return_raw_response=True,
        )
        return User(**raw_resp.json()), raw_resp.cookies

    def get_paginated_organizations(
        self,
        name: Optional[str] = None,
        expand: Optional[OrgExpand] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort: Optional[str] = None,
    ) -> PaginatedOrganizations:
        """
        Returns a paginated list of organizations

        Requires a global role.

        :param name:
        :param expand:
        :param page:
        :param page_size:
        :param sort: Must be supplied in the format [column_name] to denote asc sort by this column OR -[column_name] to denote desc sort by this column
        """

        params: Dict[str, Any] = {}
        if name is not None:
            params["name"] = name
        if expand is not None:
            params["expand"] = expand.value
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["page_size"] = page_size
        if sort is not None:
            params["sort"] = sort

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/organizations", params=params, validation_response_code=200
        )
        return PaginatedOrganizations(**parsed_resp)

    def create_organization(self, json_body: NewOrganizationRequest) -> Organization:
        """
        Creates a new organization

        Requires a global role.

        :param json_body:
        """

        parsed_resp: Dict[str, Any] = self.http_client.post(  # type: ignore
            f"/v3/organizations",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=201,
        )
        return Organization(**parsed_resp)

    def get_organization_by_id(self, organization_id: str) -> Organization:
        """
        Fetches a specific organization

        :param organization_id:
        """

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/organizations/{organization_id}", validation_response_code=200
        )
        return Organization(**parsed_resp)

    def delete_organization(self, organization_id: str) -> Response:
        """
        Deletes the organization

        This is a HARD delete. This request will fail if there are any objects associated with this organization (e.g. users, models).

        :param organization_id:
        """

        raw_resp: Response = self.http_client.delete(  # type: ignore
            f"/v3/organizations/{organization_id}",
            validation_response_code=204,
            return_raw_response=True,
        )
        return raw_resp

    def update_organization(
        self, organization_id: str, json_body: UpdateOrganizationRequest
    ) -> Organization:
        """
        Updates the organization's name and plan

        :param organization_id:
        :param json_body:
        """

        parsed_resp: Dict[str, Any] = self.http_client.patch(  # type: ignore
            f"/v3/organizations/{organization_id}",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=200,
        )
        return Organization(**parsed_resp)

    def get_organization_limits(self, organization_id: str) -> OrganizationLimits:
        """
        Retrieves the specified organization's limits based on its license plan

        :param organization_id:
        """

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/organizations/{organization_id}/limits", validation_response_code=200
        )
        return OrganizationLimits(**parsed_resp)

    def get_organization_usage(self, organization_id: str) -> OrganizationUsage:
        """
        Retrieves the specified organization's usage

        :param organization_id:
        """

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/organizations/{organization_id}/usage", validation_response_code=200
        )
        return OrganizationUsage(**parsed_resp)

    def get_current_organization(self) -> Organization:
        """
        Returns the calling user's current organization

        """

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/organizations/current", validation_response_code=200
        )
        return Organization(**parsed_resp)

    def update_current_organization(
        self, json_body: SetCurrentOrganizationRequest
    ) -> SetCurrentOrganizationRequest:
        """
        Sets your current organization

        :param json_body:
        """

        parsed_resp: Dict[str, Any] = self.http_client.put(  # type: ignore
            f"/v3/organizations/current",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=200,
        )
        return SetCurrentOrganizationRequest(**parsed_resp)

    def get_current_user_organizations(self) -> List[Organization]:
        """
        Returns all the organizations that the calling user is in

        """

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/organizations/me", validation_response_code=200
        )
        return List[Organization](**parsed_resp)

    def authorize_user_caller(self, json_body: PermissionRequest) -> Response:
        """
        Endpoint for validating a requesting caller has the permissions on the supplied action and resource

        :param json_body:
        """

        raw_resp: Response = self.http_client.post(  # type: ignore
            f"/v3/authorization/authorize",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=200,
            return_raw_response=True,
        )
        return raw_resp

    def get_user_permissions(self) -> List[PermissionRequest]:
        """
        Endpoint that returns all permissions for the requesting caller

        Will return an empty list if the caller has no permissions in the current organization.

        """

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/authorization/permissions", validation_response_code=200
        )
        return List[PermissionRequest](**parsed_resp)

    def get_organization_custom_roles(
        self, roles: Optional[str] = None
    ) -> CustomRBACRequest:
        """
        Returns custom defined roles for the calling organization

        :param roles:
        """

        params: Dict[str, Any] = {}
        if roles is not None:
            params["roles"] = roles

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/authorization/custom_roles",
            params=params,
            validation_response_code=200,
        )
        return CustomRBACRequest(**parsed_resp)

    def create_organization_custom_roles(
        self, json_body: CustomRBACRequest
    ) -> CustomRBACRequest:
        """
        Create custom defined roles for the calling organization

        If roles exist for this org already, this request will be additive

        :param json_body:
        """

        parsed_resp: Dict[str, Any] = self.http_client.post(  # type: ignore
            f"/v3/authorization/custom_roles",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=200,
        )
        return CustomRBACRequest(**parsed_resp)

    def delete_organization_custom_roles(
        self, json_body: RolesRequest
    ) -> CustomRBACRequest:
        """
        Delete any or all custom roles defined for the calling organization

        :param json_body:
        """

        parsed_resp: Dict[str, Any] = self.http_client.delete(  # type: ignore
            f"/v3/authorization/custom_roles",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=200,
        )
        return CustomRBACRequest(**parsed_resp)

    def get_usage_metrics(
        self,
        rollup: UsageRollups,
        metric_category: List[UsageCategory],
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
    ) -> PaginatedUsageResponse:
        """


        :param rollup:
        :param metric_category:
        :param start_time:
        :param end_time:
        """

        params: Dict[str, Any] = {
            "metric_category": metric_category,
        }
        if start_time is not None:
            params["start_time"] = start_time
        if end_time is not None:
            params["end_time"] = end_time

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/usage/{rollup}", params=params, validation_response_code=200
        )
        return PaginatedUsageResponse(**parsed_resp)
