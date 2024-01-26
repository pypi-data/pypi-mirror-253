#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Model for Leveraged Authorizations in the application """

from typing import Optional
from urllib.parse import urljoin

from pydantic import BaseModel, validator

from regscale.core.app.api import Api
from regscale.core.app.application import Application


class LeveragedAuthorization(BaseModel):
    """LeveragedAuthorizations model."""

    id: Optional[int] = 0
    isPublic: Optional[bool] = True
    uuid: Optional[str] = None
    title: str
    fedrampId: Optional[str] = None
    ownerId: str
    securityPlanId: int
    dateAuthorized: str
    description: Optional[str] = None
    servicesUsed: Optional[str] = None
    securityPlanLink: Optional[str] = None
    crmLink: Optional[str] = None
    responsibilityAndInheritanceLink: Optional[str] = None
    createdById: str
    dateCreated: Optional[str] = None
    lastUpdatedById: str
    dateLastUpdated: Optional[str] = None
    tenantsId: Optional[int] = None

    @validator("crmLink", pre=True, always=True)
    def validate_crm_link(cls, value):
        """
        Validate the CRM link.

        :param value: The CRM link.
        :return: The validated CRM link.
        :rtype: str
        """
        if not value:
            value = ""
        return value

    @validator("responsibilityAndInheritanceLink", pre=True, always=True)
    def validate_responsibility_and_inheritance_link(cls, value):
        """
        Validate the responsibility and inheritance link.

        :param value: The responsibility and inheritance link.
        :return: The validated responsibility and inheritance link.
        :rtype: str
        """
        if not value:
            value = ""
        return value

    @validator("securityPlanLink", pre=True, always=True)
    def validate_security_plan_link(cls, value):
        """
        Validate the security plan link.

        :param value: The security plan link.
        :return: The validated security plan link.
        :rtype: str
        """
        if not value:
            value = ""
        return value

    @staticmethod
    def insert_leveraged_authorizations(
        app: Application, leveraged_auth: "LeveragedAuthorization"
    ) -> dict:
        """
        Insert a leveraged authorization into the database.

        :param Application app: The application instance.
        :param LeveragedAuthorization leveraged_auth: The leveraged authorization to insert.
        :return: The response from the API or raise an exception
        :rtype: dict
        """
        api = Api(app)

        # Construct the URL by joining the domain and endpoint
        url = urljoin(app.config.get("domain"), "/api/leveraged-authorization")
        # Convert the Pydantic model to a dictionary
        data = leveraged_auth.dict()
        # Make the POST request to insert the data
        response = api.post(url, json=data)

        # Check for success and handle the response as needed
        return response.json() if response.ok else response.raise_for_status()
