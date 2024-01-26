"""Provide a SystemRoleExternalAssignments model."""
from typing import Optional
from urllib.parse import urljoin

from pydantic import BaseModel

from regscale.core.app.api import Api
from regscale.core.app.application import Application


class SystemRoleExternalAssignment(BaseModel):
    id: Optional[int] = 0
    uuid: Optional[str] = ""
    stakeholderId: Optional[int] = 0
    roleId: Optional[int] = 0

    @staticmethod
    def from_dict(data: dict) -> "SystemRoleExternalAssignment":
        """
        Convert dict to SystemRoleExternalAssignments object

        :param dict data: dict to create object from
        :return: A SystemRoleExternalAssignments object
        :rtype: SystemRoleExternalAssignments
        """
        return SystemRoleExternalAssignment(**data)

    def post(self, app: Application) -> Optional[dict]:
        """
        Post a SystemRoleExternalAssignments to RegScale

        :param Application app: The application instance
        :return: The response from the API or None
        :rtype: Optional[dict]
        """
        api = Api(app)
        url = urljoin(app.config.get("domain"), "/api/systemRoleExternalAssignments")
        data = self.dict()
        response = api.post(url, json=data)
        return SystemRoleExternalAssignment(**response.json()) if response.ok else None
