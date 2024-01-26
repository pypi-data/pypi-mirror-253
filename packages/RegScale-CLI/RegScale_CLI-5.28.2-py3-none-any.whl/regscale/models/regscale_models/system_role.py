#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Class for a RegScale SystemRoles """
from typing import Any, List, Optional
from urllib.parse import urljoin

import requests
from pydantic import BaseModel

from regscale.core.app.api import Api
from regscale.core.app.application import Application
from regscale.core.app.logz import create_logger


class SystemRole(BaseModel):
    """Class for a RegScale SystemRoles"""

    roleName: str  # Required Field
    roleType: str  # Required Field
    roleType: str  # Required Field
    accessLevel: str  # Required Field
    sensitivityLevel: str  # Required field
    sensitivityLevel: str  # Required field
    privilegeDescription: str  # Required Field
    securityPlanId: int  # Required Field
    createdById: Optional[str] = None
    id: Optional[int] = 0
    uuid: Optional[str] = ""
    functions: Optional[str] = None
    lastUpdatedById: Optional[str] = None
    isPublic: Optional[bool] = True
    dateCreated: Optional[str] = None
    dateLastUpdated: Optional[str] = ""
    assignedUserId: Optional[str] = ""
    fedrampRoleId: Optional[str] = ""

    @staticmethod
    def from_dict(obj: Any) -> "SystemRole":
        """
        Create a SystemRoles object from a dictionary

        :param Any obj: The dictionary to convert to a SystemRoles object
        :return: A SystemRoles object
        :rtype: SystemRole
        """
        if "id" in obj:
            del obj["id"]
        if isinstance(obj["functions"], list):
            obj["functions"] = ", ".join(obj["functions"])
        return SystemRole(**obj)

    def __eq__(self, other: object) -> bool:
        """
        Compare two SystemRoles objects

        :param other: The object to compare to
        :return: True if the SystemRoles objects are equal
        :rtype: bool
        """
        if not isinstance(other, SystemRole):
            return NotImplemented
        return self.dict() == other.dict()

    def __hash__(self) -> hash:
        """
        Hash a SystemRoles object

        :return: The hash of the SystemRoles object
        :rtype: hash
        """
        return hash(
            (
                self.roleName,
                self.roleType,
                self.accessLevel,
                self.sensitivityLevel,
                self.privilegeDescription,
                tuple(self.functions),
                self.securityPlanId,
                self.isPublic,
                self.assignedUserId,
                self.fedrampRoleId,
            )
        )

    def insert_systemrole(self, app: Application, **kwargs) -> dict:
        """
        Insert a SystemRoles object into the database

        :param Application app: The application object
        :param kwargs: Additional keyword arguments
        :return: The dict of the SystemRoles object
        :rtype: dict
        """
        # Convert the object to a dictionary
        api = Api(app)
        url = urljoin(app.config.get("domain"), "/api/systemRoles/")
        logger = app.logger if "logger" not in kwargs else kwargs["logger"]
        del self.id
        del self.uuid
        del self.dateCreated
        data = self.dict()
        data["functions"] = ",".join(self.functions)
        # Make the API call
        try:
            response = api.post(url, json=data)
            if response.ok:
                # Parse the response to a SystemRoles object
                logger.info(
                    "Successfully saved System Role %s to RegScale Security"
                    + " Plan %i",
                    data["roleName"],
                    data["securityPlanId"],
                )
                return response.json()
        except requests.exceptions.RequestException as err:
            logger.warning(
                "Unable to post System Role to RegScale Security Plan #%i, \n%s",
                self.securityPlanId,
                err,
            )
        return {}

    @classmethod
    def get_or_create(
        cls, app: Application, role_name: str, ssp_id: int, **kwargs
    ) -> dict:
        """
        Get or create a SystemRoles object for a given SSP ID

        :param Application app: The application object
        :param str role_name: The name of the role
        :param int ssp_id: The SSP ID
        :param kwargs: Additional keyword arguments
        :return: The SystemRoles dict object
        :rtype: dict
        """
        # Check if a role with the same name already exists
        if "all_roles" not in kwargs:
            all_roles = cls.get_all_by_ssp_id(app, ssp_id)
        else:
            all_roles = kwargs["all_roles"]
        existing_role = next(
            (role for role in all_roles if role.roleName.lower() == role_name.lower()),
            None,
        )
        if existing_role:
            if "logger" in kwargs:
                logger = kwargs["logger"]
                logger.info(
                    "Role: %s already exists in RegScale, skipping insert..", role_name
                )
            return existing_role

        # If it doesn't exist, create a new one
        new_role = cls(roleName=role_name, **kwargs)
        return new_role.insert_systemrole(app=app, **kwargs)

    @staticmethod
    def get_all_by_ssp_id(app: Application, ssp_id: int) -> List["SystemRole"]:
        """
        Get a list of SystemRoles objects for a given SSP ID

        :param Application app: The application object
        :param int ssp_id: The SSP ID
        :return: A list of SystemRoles objects
        :rtype: List[SystemRole]
        """
        api = Api(app)
        url = urljoin(
            app.config.get("domain"), f"/api/systemRoles/getAllByParent/{ssp_id}"
        )
        response = api.get(url)
        # TODO don't raise
        # Parse the response to a list of SystemRoles objects
        return (
            [SystemRole.from_dict(role) for role in response.json()]
            if response.ok
            else []
        )
