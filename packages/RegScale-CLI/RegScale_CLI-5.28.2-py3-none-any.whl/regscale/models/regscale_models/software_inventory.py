#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Model for SoftwareInventory in the application """

from typing import List, Optional

from pydantic import BaseModel

from regscale.core.app.api import Api
from regscale.core.app.application import Application


class SoftwareInventory(BaseModel):
    """
    SoftwareInventory
    """

    id: Optional[int]
    UUID: Optional[str]
    name: Optional[str]
    version: Optional[str]
    function: Optional[str]
    patchLevel: Optional[str]
    parentHardwareAssetId: Optional[int]
    parentSoftwareInventoryId: Optional[int]
    dateLastUpdated: Optional[str]
    createdById: Optional[str]
    dateCreated: Optional[str]
    lastUpdatedById: Optional[str]
    isPublic: Optional[bool]
    references: Optional[List[str]]

    def __eq__(self, other):
        """
        Override the default Equals behavior

        :param other: SoftwareInventory to compare
        :return: True if equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, SoftwareInventory):
            return self.name == other.name and self.version == other.version
        return False

    def __hash__(self) -> hash:
        """
        Override the default hash behavior

        :return: hash of the SoftwareInventory
        :rtype: hash
        """
        return hash((self.name, self.version))

    @classmethod
    def insert(cls, app: Application, obj: "SoftwareInventory") -> "SoftwareInventory":
        """
        Insert a new SoftwareInventory into RegScale

        :param Application app: application
        :param SoftwareInventory obj: SoftwareInventory to insert
        :return: SoftwareInventory object
        :rtype: SoftwareInventory
        """
        api = Api(app)
        result = {}
        res = api.post(
            url=app.config["domain"] + "/api/softwareinventory", json=obj.dict()
        )
        if res.status_code == 200 and res.ok:
            result = res.json()
        return result

    @classmethod
    def update(cls, app: Application, obj: "SoftwareInventory") -> "SoftwareInventory":
        """
        Update an existing SoftwareInventory in RegScale

        :param Application app: application
        :param SoftwareInventory obj: SoftwareInventory to update
        :return: SoftwareInventory object
        :rtype: SoftwareInventory
        """
        api = Api(app)
        result = {}
        res = api.put(
            url=app.config["domain"] + f"/api/softwareinventory/{obj.id}",
            json=obj.dict(),
        )
        if res.status_code == 200 and res.ok:
            result = res.json()
        return result
