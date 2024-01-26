#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Model for a RegScale Security Checklist """

# standard python imports
from json import JSONDecodeError
from typing import Any, Optional
from urllib.parse import urljoin

from pydantic import BaseModel

from regscale.core.app.api import Api
from regscale.core.app.application import Application
from regscale.core.app.utils.app_utils import get_current_datetime


class Checklist(BaseModel):
    """RegScale Checklist

    :return: RegScale Checklist
    """

    # Required
    status: str
    assetId: int
    tool: str
    baseline: str
    id: Optional[int] = 0
    uuid: Optional[str]
    vulnerabilityId: Optional[str]
    ruleId: Optional[str]
    cci: Optional[str]
    check: Optional[str]
    results: Optional[str]
    comments: Optional[str]
    createdById: Optional[str]
    lastUpdatedById: Optional[str]
    datePerformed: Optional[str]
    isPublic: Optional[bool] = True
    dateCreated: Optional[str] = get_current_datetime()
    dateLastUpdated: Optional[str] = get_current_datetime()

    def __hash__(self) -> hash:
        """
        Enable object to be hashable

        :return: Hashed Checklist
        :rtype: hash
        """
        return hash(
            (
                self.tool,
                self.vulnerabilityId,
                self.ruleId,
                self.baseline,
                self.check,
                self.results,
                self.comments,
                self.assetId,
            )
        )

    def __eq__(self, other) -> "Checklist":
        """
        Compare Checklists

        :param other: Checklist to compare against
        :return: Updated Checklist
        :rtype: Checklist
        """
        return (
            # Unique values
            # Tool, VulnerabilityId, RuleId, Baseline, [Check], Results, Comments, Status, AssetId,
            # TenantsId, CCI, Version
            self.tool == other.tool
            and self.vulnerabilityId == other.vulnerabilityId
            and self.ruleId == other.ruleId
            and self.baseline == other.baseline
            and self.check == other.check
            and self.results == other.results
            and self.comments == other.comments
            and self.assetId == other.assetId
        )

    def __delitem__(self, key: Any) -> None:
        """
        Delete an item from the Checklist

        :param Any key: Key to delete
        :return: None
        """
        del self[key]

    @staticmethod
    def from_dict(obj: Any) -> "Checklist":
        """
        Create a Checklist object from a dictionary

        :param Any obj: Dictionary to create a Checklist object from
        :return: Checklist object
        :rtype: Checklist
        """
        return Checklist(**obj)

    @staticmethod
    def insert_or_update_checklist(
        app: Application,
        new_checklist: "Checklist",
        existing_checklists: list["Checklist"],
    ) -> Optional[int]:
        """
        Insert or update a checklist

        :param Application app: RegScale Application instance
        :param Checklist new_checklist: New checklist to insert or update
        :param list[Checklist] existing_checklists: Existing checklists to compare against
        :return: int of the checklist id or None
        :rtype: Optional[int]
        """
        delete_keys = [
            "asset",
            "uuid",
            "lastUpdatedById",
            "dateLastUpdated",
            "createdById",
            "dateCreated",
        ]
        for dat in existing_checklists:
            for key in delete_keys:
                if key in dat:
                    del dat[key]
        api = Api(app)
        matching_checklists = [
            Checklist.from_dict(chk)
            for chk in existing_checklists
            if Checklist.from_dict(chk) == new_checklist
        ]
        if matching_checklists:
            app.logger.info("Updating checklist %s", new_checklist.baseline)
            new_checklist.id = matching_checklists[0].id
            res = api.put(
                url=app.config["domain"] + f"/api/securitychecklist/{new_checklist.id}",
                json=new_checklist.dict(),
            )
        else:
            app.logger.info("Inserting checklist %s", new_checklist.baseline)
            res = api.post(
                url=app.config["domain"] + "/api/securitychecklist",
                json=new_checklist.dict(),
            )
        if res.status_code != 200:
            app.logger.warning(
                "Unable to insert or update checklist %s", new_checklist.baseline
            )
            return None
        return res.json()["id"]

    @staticmethod
    def batch_insert_or_update(
        api: Api, checklists: list["Checklist"], method: Optional[str] = "insert"
    ) -> Optional[list["Checklist"]]:
        """
        Insert a batch of checklists

        :param Api api: RegScale API instance
        :param list[Checklist] checklists: List of checklists to insert
        :param Optional[str] method: Method to use (insert or update), defaults to insert
        :return: List of checklists inserted
        :rtype: Optional[list[Checklist]]
        """
        if method == "insert":
            endpoint = "batchCreate"
            api.logger.info("Creating %i checklist(s) in RegScale...", len(checklists))
        elif method == "update":
            endpoint = "batchUpdate"
            api.logger.info("Updating %i checklist(s) in RegScale...", len(checklists))
        else:
            api.logger.error("Invalid method %s, please use insert or update.", method)
            return None
        response = api.post(
            url=urljoin(api.app.config["domain"], f"/api/securityChecklist/{endpoint}"),
            json=[checklist.dict() for checklist in checklists],
        )
        if response.ok:
            try:
                return [Checklist(**check) for check in response.json()]
            except TypeError as err:
                api.logger.error("Unable to convert checklist(s): %s", err)
                return None
            except JSONDecodeError:
                api.logger.error(
                    "Unable to %s checklist(s) in batch: %s", method, response.text
                )
                return None
        else:
            api.logger.error(
                "Unable to %s checklist(s) in batch: %s", method, response.text
            )
            response.raise_for_status()
        return None

    @staticmethod
    def analyze_and_batch_process(
        app: Application,
        new_checklists: Optional[list["Checklist"]] = None,
        existing_checklists: Optional[list["Checklist"]] = None,
    ) -> dict:
        """
        Function to insert or update a checklist using batches via API

        :param Application app: RegScale CLI Application instance
        :param Optional[list[Checklist]] new_checklists: List of new checklists to insert or update
        :param Optional[list[Checklist]] existing_checklists: List of existing checklists to compare against
        :return: Dictionary with list of checklists inserted and/or updated
            example: {'inserted': [], 'updated': [Checklist()...]}
        :rtype: dict
        """
        results = {"inserted": [], "updated": []}
        # if no existing checklists, insert all new checklists and return results
        if existing_checklists is None:
            results["inserted"] = Checklist.batch_insert_or_update(
                Api(app), new_checklists, "insert"
            )
            return results
        api = Api(app)
        # see if any of the new checklists already exist
        update_checks = []
        create_checks = []
        for new_checklist in new_checklists:
            if matching_checklists := [
                check
                for check in existing_checklists
                if check.vulnerabilityId == new_checklist.vulnerabilityId
            ]:
                new_checklist.id = matching_checklists[0].id
                update_checks.append(new_checklist)
            else:
                create_checks.append(new_checklist)
        if update_checks:
            results["updated"] = Checklist.batch_insert_or_update(
                api, update_checks, "update"
            )
        if create_checks:
            results["inserted"] = Checklist.batch_insert_or_update(
                api, create_checks, "insert"
            )
        return results

    @staticmethod
    def get_checklists_by_asset(api: Api, asset_id: int) -> list["Checklist"]:
        """
        Return all checklists for a given RegScale parent id and parent module

        :param Api api: RegScale CLI API instance
        :param int asset_id: RegScale Asset ID
        :return: List of checklists for the given asset_id
        :rtype: list[Checklist]
        """
        api.logger.info("Fetching all checklists for RegScale asset #%i...", asset_id)
        response = api.get(
            url=urljoin(
                api.config.get("domain"),
                f"/api/securityChecklist/getAllByParent/{asset_id}",
            )
        )
        try:
            if checklists := [Checklist(**check) for check in response.json()]:
                api.logger.info(
                    "Found %i checklist(s) for asset #%i in RegScale.",
                    len(checklists),
                    asset_id,
                )
                return checklists
        except TypeError as err:
            api.logger.error("Unable to convert checklist(s): %s", err)
        except JSONDecodeError:
            api.logger.error(
                "Unable to retrieve any checklists for asset #%i.\n%i: %s-%s",
                asset_id,
                response.status_code,
                response.reason,
                response.text,
            )
        return []

    @staticmethod
    def get_checklists(
        parent_id: int, parent_module: Optional[str] = "components"
    ) -> list["Checklist"]:
        """
        Return all checklists for a given RegScale parent id and parent module

        :param int parent_id: RegScale parent id
        :param Optional[str] parent_module: RegScale parent module, defaults to components
        :return: List of checklists for the given parent id and module
        :rtype: list[Checklist]
        """
        app = Application()
        api = Api(app)
        app.logger.debug("Fetching all checklists for %s %s", parent_module, parent_id)
        checklists = []
        query = """
                           query {
                securityChecklists(skip: 0, take: 50,where:{asset: {parentId: {eq: parent_id_placeholder}, parentModule: {eq: "parent_module_placeholder"}}}) {
                    items {
                            id
                            asset {
                              id
                              name
                              parentId
                              parentModule
                            }
                            status
                            tool
                            datePerformed
                            vulnerabilityId
                            ruleId
                            cci
                            check
                            results
                            baseline
                            comments
                    }
                    totalCount
                    pageInfo {
                        hasNextPage
                    }
                }
            }
            """.replace(
            "parent_id_placeholder", str(parent_id)
        ).replace(
            "parent_module_placeholder", parent_module
        )
        data = api.graph(query)
        if "securityChecklists" in data and "items" in data["securityChecklists"]:
            for item in data["securityChecklists"]["items"]:
                item["assetId"] = item["asset"]["id"]
                checklists.append(item)
        return checklists
