#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide References models."""
from typing import List, Union, Optional

from pydantic import BaseModel, Field

from regscale.core.app.api import Api
from regscale.core.app.application import Application
from regscale.core.app.logz import create_logger
from regscale.core.app.utils.app_utils import get_current_datetime

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


class Reference(BaseModel):
    """References model"""

    id: Optional[int] = 0
    createdById: Optional[str] = ""  # this should be userID
    dateCreated: str = Field(default=get_current_datetime(dt_format=DATE_FORMAT))
    lastUpdatedById: Optional[str] = ""  # this should be userID
    isPublic: Optional[bool] = True
    identificationNumber: Optional[str] = ""
    title: Optional[str] = ""
    version: Optional[str] = ""
    datePublished: Optional[str] = Field(
        default=get_current_datetime(dt_format=DATE_FORMAT)
    )
    referenceType: Optional[str] = ""
    link: Optional[str] = ""
    parentId: Optional[int] = 0
    parentModule: Optional[str] = ""
    dateLastUpdated: Optional[str] = Field(
        default=get_current_datetime(dt_format=DATE_FORMAT)
    )

    @staticmethod
    def from_dict(data: dict) -> "Reference":
        """
        Convert dict to References object

        :param dict data: dict to create object from
        :return: A References object
        :rtype: Reference
        """
        return Reference(**data)

    @staticmethod
    def create_references_from_list(
        parent_id: Union[str, int],
        references_list: List[dict],
        parent_module: Optional[str] = "securityplans",
    ) -> List[Union["Reference", bool]]:
        """
        Create a list of References objects from a list of dicts

        :param Union[str, int] parent_id: ID of the SSP to create the References objects for
        :param List[dict] references_list: List of dicts to create objects from
        :param Optional[str] parent_module: Parent module of the References objects, defaults to "securityplans"
        :return: List of References objects or False if unsuccessful
        :rtype: List[Union[Reference, bool]]
        """
        references = [
            Reference(parentId=parent_id, parentModule=parent_module, **references)
            for references in references_list
        ]
        response = []
        for reference in references:
            response.append(reference.create_new_references(return_object=True))
        return response

    def create_new_references(
        self, return_object: Optional[bool] = False
    ) -> Union[bool, "Reference"]:
        """
        Create a new References object in RegScale

        :param Optional[bool] return_object: Return the References object if successful, defaults to False
        :return: True if successful, False otherwise
        :rtype: Union[bool, "Reference"]
        """
        app = Application()
        api = Api(app=app)
        data = self.dict()
        data["createdById"] = api.config["userId"]
        data["lastUpdatedById"] = api.config["userId"]
        references_response = api.post(
            f'{api.config["domain"]}/api/references/',
            json=data,
        )
        logger = create_logger()
        if references_response.ok:
            logger.info(f'Created References: {references_response.json()["id"]}')
            if return_object:
                return Reference.from_dict(references_response.json())
            return True
        logger.error(f"Error creating References: {references_response.text}")
        return False
