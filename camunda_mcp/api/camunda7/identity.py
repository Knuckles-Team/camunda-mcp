"""Operaton / Camunda 7 engine REST: the Identity operations."""

from typing import Any

from camunda_mcp.api.api_client_base import ApiClientBase


class Camunda7Identity(ApiClientBase):
    """Identity: 4 engine REST operation(s)."""

    def check_password(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Validate Password.

        A password policy consists of a list of rules that new passwords must follow
        to be policy compliant. A password can be checked for compliance via this
        end point. More information on password policies in Operaton can be found in
        the password policy user guide and in the security instructions. Request
        body: an object with password, profile.

        POST /identity/password-policy
        """
        return self._call(
            "POST",
            "/identity/password-policy",
            body=body,
        )

    def get_group_info(
        self,
        *,
        user_id: str,
    ) -> Any:
        """Get a User's Groups.

        Gets the groups of a user by id and includes all users that share a group
        with the given user.

        GET /identity/groups
        """
        return self._call(
            "GET",
            "/identity/groups",
            params={
                "userId": user_id,
            },
        )

    def get_password_policy(
        self,
    ) -> Any:
        """Get Password Policy.

        A password policy consists of a list of rules that new passwords must follow
        to be policy compliant. This end point returns a JSON representation of the
        list of policy rules. More information on password policies in Operaton can
        be found in the password policy user guide and in the security instructions.

        GET /identity/password-policy
        """
        return self._call(
            "GET",
            "/identity/password-policy",
        )

    def verify_user(
        self,
        *,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Verify User.

        Verifies that user credentials are valid. Request body: an object with
        username, password.

        POST /identity/verify
        """
        return self._call(
            "POST",
            "/identity/verify",
            body=body,
        )
