#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Dataclass for Requirement in the application """

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Requirement:
    title: str  # Required
    status: str  # Required
    lastUpdatedById: str  # Required
    controlID: int  # Required
    requirementOwnerId: str  # Required
    parentId: int  # Required
    id: Optional[int] = 0
    assessmentPlan: Optional[str] = ""
    dateLastAssessed: Optional[str] = ""
    lastAssessmentResult: Optional[str] = ""
    parentRequirementId: Optional[int] = None
    parentModule: Optional[str] = "implementations"
    createdById: Optional[str] = ""
    dateCreated: Optional[str] = ""
    dateLastUpdated: Optional[str] = ""
    isPublic: Optional[bool] = True
    description: Optional[str] = ""
    implementation: Optional[str] = ""
    uuid: Optional[str] = ""
