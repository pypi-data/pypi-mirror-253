#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Model for Control Test Plan in the application """

from typing import Optional
from urllib.parse import urljoin

from pydantic import BaseModel

from regscale.core.app.api import Api
from regscale.core.app.application import Application
from regscale.core.app.utils.api_handler import APIInsertionError


class ControlTestPlan(BaseModel):
    """
    ControlTestPlan class
    """

    id: int = 0
    uuid: Optional[str] = None
    test: Optional[str] = None
    testId: Optional[str] = None
    securityControlId: Optional[int] = None
    archived: Optional[bool] = False
    createdById: Optional[str] = None
    dateCreated: Optional[str] = None
    lastUpdatedById: Optional[str] = None
    dateLastUpdated: Optional[str] = None
    tenantsId: Optional[int] = None
    isPublic: Optional[bool] = True

    def insert_controltestplan(self, app: Application) -> dict:
        """
        Insert a ControlTestPlan into the database

        :param Application app: Application object
        :raises APIInsertionError: API request failed
        :return: JSON response
        :rtype: dict
        """
        # Convert the model to a dictionary
        api = Api(app)
        data = self.dict()
        api_url = urljoin(app.config["domain"], "/api/controltestplans")
        # Make the API call
        response = api.post(api_url, json=data)

        # Check the response
        if not response.ok:
            print(response.text)
            raise APIInsertionError(
                f"API request failed with status {response.status_code}"
            )

        return response.json()

    @staticmethod
    def from_dict(obj: dict) -> "ControlTestPlan":
        """
        Create ControlTestPlan object from dict

        :param dict obj: dictionary object
        :return: ControlTestPlan class
        :rtype: ControlTestPlan
        """
        return ControlTestPlan(**obj)
