#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Model for Interconnect in the application """

from typing import Any, Optional

from pydantic import BaseModel


class Interconnect(BaseModel):
    """RegScale Interconnects model"""

    id: Optional[int] = 0
    authorizationType: str
    categorization: str
    connectionType: str
    name: str
    organization: str
    status: str
    parentId: int
    parentModule: Optional[str]
    aOId: str
    interconnectOwnerId: str
    isPublic: Optional[bool] = True
    agreementDate: Optional[str]
    expirationDate: Optional[str]
    description: Optional[str]
    createdById: Optional[str]
    dateCreated: Optional[str]
    dateLastUpdated: Optional[str]
    lastUpdatedById: Optional[str]
    tenantsId: Optional[int]
    uuid: Optional[str]
    dataDirection: Optional[str]
    externalEmail: Optional[str]
    externalFQDN: Optional[str]
    externalIpAddress: Optional[str]
    externalPOC: Optional[str]
    externalPhone: Optional[str]
    sourceFQDN: Optional[str]
    sourceIpAddress: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> "Interconnect":
        """
        Construct an Interconnect from provided obj

        :param Any obj:
        :return:
        """
        return Interconnect(**obj)
