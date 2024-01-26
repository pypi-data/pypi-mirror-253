#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Class for a RegScale Ports and Protocols """
from pydantic import BaseModel
from typing import Any, Optional


class PortsProtocol(BaseModel):
    """Ports And Protocols"""

    parentId: int
    parentModule: Optional[str]
    startPort: int
    endPort: int
    protocol: Optional[str]
    service: Optional[str]
    purpose: Optional[str]
    usedBy: Optional[str]
    createdById: Optional[str]
    lastUpdatedById: Optional[str]

    @staticmethod
    def from_dict(obj: Any) -> "PortsProtocol":
        """
        Create RegScale Port and Protocol from dictionary

        :param Any obj: ports and protocol dictionary
        :return: ControlImplementation class
        :rtype: ControlImplementation
        """
        if "id" in obj:
            del obj["id"]
        return PortsProtocol(**obj)

    def __eq__(self, other: "PortsProtocol") -> bool:
        """
        Compare two PortsProtocols objects

        :param PortsProtocol other: PortsProtocols object
        :return: True if PortsProtocols are equal
        :rtype: bool
        """
        if isinstance(other, PortsProtocol):
            return self.dict() == other.dict()
        return False

    def __hash__(self) -> hash:
        """
        Return hash of PortsProtocols

        :return: hash of PortsProtocols
        :rtype: hash
        """
        return hash(
            (
                self.parentId,
                self.parentModule,
                self.startPort,
                self.endPort,
                self.protocol,
                self.service,
                self.purpose,
            )
        )
