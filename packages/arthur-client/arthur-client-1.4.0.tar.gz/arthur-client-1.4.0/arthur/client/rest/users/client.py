from typing import Optional, Any, Union, Dict, List, Tuple
from http import HTTPStatus
from requests.cookies import RequestsCookieJar
from requests import Response

# import http client
from arthur.client.http.requests import HTTPClient

from arthur.client.rest.users.models import (
    AuthenticationInfo,
    InviteRequest,
    InviteResponse,
    NewUserRequest,
    PaginatedUsers,
    UpdateCurrentUserRequest,
    UpdateUserRequest,
    User,
    UserResponse,
)


PATH_PREFIX = "/api"


class ArthurUsersClient:
    """
    A Python client to interact with the Arthur Users API
    """

    def __init__(self, http_client: HTTPClient):
        """
        Create a new ArthurUsersClient from an HTTPClient

        :param http_client: the :class:`~arthurai.client.http.requests.HTTPClient` to use for underlying requests
        """
        self.http_client = http_client
        self.http_client.set_path_prefix(PATH_PREFIX)

    def authenticate(self) -> AuthenticationInfo:
        """
        Returns authentication info for the calling, token-bearing user

        """

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/users/me/auth_info", validation_response_code=200
        )
        return AuthenticationInfo(**parsed_resp)

    def get_paginated_users(
        self,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        sort: Optional[str] = None,
    ) -> PaginatedUsers:
        """
        Returns a paginated list of users

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
            f"/v3/users", params=params, validation_response_code=200
        )
        return PaginatedUsers(**parsed_resp)

    def create_user(self, json_body: NewUserRequest) -> User:
        """
        Creates a new user

        :param json_body:
        """

        parsed_resp: Dict[str, Any] = self.http_client.post(  # type: ignore
            f"/v3/users",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=201,
        )
        return User(**parsed_resp)

    def get_current_user(self) -> UserResponse:
        """
        Returns the currently authenticated user

        """

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/users/me", validation_response_code=200
        )
        return UserResponse(**parsed_resp)

    def update_current_user(self, json_body: UpdateCurrentUserRequest) -> UserResponse:
        """
        Updates the currently authenticated user

        :param json_body:
        """

        parsed_resp: Dict[str, Any] = self.http_client.patch(  # type: ignore
            f"/v3/users/me",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=200,
        )
        return UserResponse(**parsed_resp)

    def get_user_by_id(self, user_id: str) -> User:
        """
        Returns a single user

        :param user_id:
        """

        parsed_resp: Dict[str, Any] = self.http_client.get(  # type: ignore
            f"/v3/users/{user_id}", validation_response_code=200
        )
        return User(**parsed_resp)

    def delete_user(self, user_id: str) -> Response:
        """
        Deletes a user (by marking them as inactive) and invalidates any existing api keys

        :param user_id:
        """

        raw_resp: Response = self.http_client.delete(  # type: ignore
            f"/v3/users/{user_id}",
            validation_response_code=204,
            return_raw_response=True,
        )
        return raw_resp

    def update_user(self, user_id: str, json_body: UpdateUserRequest) -> User:
        """
        Updates a user

        Request to update the password must include the old password unless a super admin is making the request.

        :param user_id:
        :param json_body:
        """

        parsed_resp: Dict[str, Any] = self.http_client.patch(  # type: ignore
            f"/v3/users/{user_id}",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=200,
        )
        return User(**parsed_resp)

    def send_user_invites(self, json_body: InviteRequest) -> InviteResponse:
        """
        Send email invitations to have users join the requesters organization

        :param json_body:
        """

        parsed_resp: Dict[str, Any] = self.http_client.post(  # type: ignore
            f"/v3/users/invite_users",
            json=json_body.dict(by_alias=True, exclude_none=True),
            validation_response_code=200,
        )
        return InviteResponse(**parsed_resp)
