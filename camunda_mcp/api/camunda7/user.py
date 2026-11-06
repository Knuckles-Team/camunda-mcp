"""Operaton / Camunda 7 engine REST: the User operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7User(ApiClientBase):
    """User: 8 engine REST operation(s)."""

    def create_user(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Create.

        Create a new user. Request body: an object with profile, credentials.

        POST /user/create
        """
        return self._call(
            "POST",
            "/user/create",
            body=body,
        )

    def delete_user(
        self,
        id: str,
    ) -> Any:
        """Delete.

        Deletes a user by id.

        DELETE /user/{id}
        """
        return self._call(
            "DELETE",
            "/user/{id}",
            path={"id": id},
        )

    def get_user_count(
        self,
        *,
        id: str | None = None,
        id_in: str | None = None,
        first_name: str | None = None,
        first_name_like: str | None = None,
        last_name: str | None = None,
        last_name_like: str | None = None,
        email: str | None = None,
        email_like: str | None = None,
        member_of_group: str | None = None,
        member_of_tenant: str | None = None,
        potential_starter: str | None = None,
    ) -> Any:
        """Get List Count.

        Queries for the number of deployments that fulfill given parameters. Takes
        the same parameters as the Get Users method.

        GET /user/count
        """
        return self._call(
            "GET",
            "/user/count",
            params={
                "id": id,
                "idIn": id_in,
                "firstName": first_name,
                "firstNameLike": first_name_like,
                "lastName": last_name,
                "lastNameLike": last_name_like,
                "email": email,
                "emailLike": email_like,
                "memberOfGroup": member_of_group,
                "memberOfTenant": member_of_tenant,
                "potentialStarter": potential_starter,
            },
        )

    def get_user_profile(
        self,
        id: str,
    ) -> Any:
        """Get Profile.

        Retrieves a user's profile.

        GET /user/{id}/profile
        """
        return self._call(
            "GET",
            "/user/{id}/profile",
            path={"id": id},
        )

    def get_users(
        self,
        *,
        id: str | None = None,
        id_in: str | None = None,
        first_name: str | None = None,
        first_name_like: str | None = None,
        last_name: str | None = None,
        last_name_like: str | None = None,
        email: str | None = None,
        email_like: str | None = None,
        member_of_group: str | None = None,
        member_of_tenant: str | None = None,
        potential_starter: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        first_result: int | None = None,
        max_results: int | None = None,
    ) -> Any:
        """Get List.

        Query for a list of users using a list of parameters. The size of the result
        set can be retrieved by using the Get User Count method. Get User Count
        method.

        GET /user
        """
        return self._call(
            "GET",
            "/user",
            params={
                "id": id,
                "idIn": id_in,
                "firstName": first_name,
                "firstNameLike": first_name_like,
                "lastName": last_name,
                "lastNameLike": last_name_like,
                "email": email,
                "emailLike": email_like,
                "memberOfGroup": member_of_group,
                "memberOfTenant": member_of_tenant,
                "potentialStarter": potential_starter,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "firstResult": first_result,
                "maxResults": max_results,
            },
        )

    def unlock_user(
        self,
        id: str,
    ) -> Any:
        """Unlock User.

        Unlocks a user by id.

        POST /user/{id}/unlock
        """
        return self._call(
            "POST",
            "/user/{id}/unlock",
            path={"id": id},
        )

    def update_credentials(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update Credentials.

        Updates a user's credentials (password) Request body: an object with
        password, authenticatedUserPassword.

        PUT /user/{id}/credentials
        """
        return self._call(
            "PUT",
            "/user/{id}/credentials",
            path={"id": id},
            body=body,
        )

    def update_profile(
        self,
        id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update User Profile.

        Updates the profile information of an already existing user. Request body:
        an object with id, firstName, lastName, email.

        PUT /user/{id}/profile
        """
        return self._call(
            "PUT",
            "/user/{id}/profile",
            path={"id": id},
            body=body,
        )
