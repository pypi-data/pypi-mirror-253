#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Model for a RegScale Asset """

# standard python imports
from concurrent.futures import ThreadPoolExecutor
from typing import Any, List, Optional
from urllib.parse import urljoin

from pydantic import ConfigDict
from requests import JSONDecodeError, Response
from rich.progress import Progress

from regscale.core.app.api import Api
from regscale.core.app.application import Application
from regscale.core.app.utils.app_utils import get_current_datetime
from .regscale_model import RegScaleModel


class Asset(RegScaleModel):
    """Asset Model"""

    _model_slug = "assets"

    name: str  # Required
    id: int = 0  # Required
    parentId: int  # Required
    parentModule: str  # Required
    isPublic: bool = True  # Required as Bool
    ram: int = 0  # Required as int
    assetOwnerId: str = "Unknown"  # Required as string
    dateCreated: Optional[str] = get_current_datetime()  # Required as string
    dateLastUpdated: Optional[str] = get_current_datetime()  # Required as string
    assetType: Optional[str]
    location: Optional[str]
    diagramLevel: Optional[str]
    cpu: Optional[int]
    description: Optional[str]
    diskStorage: Optional[int]
    ipAddress: Optional[str]
    macAddress: Optional[str]
    manufacturer: Optional[str]
    model: Optional[str]
    osVersion: Optional[str]
    operatingSystem: Optional[str]
    otherTrackingNumber: Optional[str]
    uuid: Optional[str]
    serialNumber: Optional[str]
    createdById: Optional[str]
    lastUpdatedById: Optional[str]
    endOfLifeDate: Optional[str]
    purchaseDate: Optional[str]
    status: Optional[str]
    tenantsId: Optional[int]
    facilityId: Optional[int]
    orgId: Optional[int]
    cmmcAssetType: Optional[str]
    wizId: Optional[str]
    wizInfo: Optional[str]
    assetCategory: Optional[str]
    assetTagNumber: Optional[str]
    baselineConfiguration: Optional[str]
    fqdn: Optional[str]
    netBIOS: Optional[str]
    softwareName: Optional[str]
    softwareVendor: Optional[str]
    softwareVersion: Optional[str]
    vlanId: Optional[str]
    bAuthenticatedScan: Optional[bool]
    bPublicFacing: Optional[bool]
    bVirtual: Optional[bool]
    notes: Optional[str]
    patchLevel: Optional[str]
    softwareFunction: Optional[str]
    systemAdministratorId: Optional[str]
    bLatestScan: Optional[bool]
    managementType: Optional[str]
    qualysId: Optional[str]
    sicuraId: Optional[str]
    tenableId: Optional[str]
    firmwareVersion: Optional[str]
    purpose: Optional[str]
    awsIdentifier: Optional[str]
    azureIdentifier: Optional[str]
    googleIdentifier: Optional[str]
    otherCloudIdentifier: Optional[str]
    ipv6Address: Optional[str]
    scanningTool: Optional[str]
    uri: Optional[str]
    bScanDatabase: Optional[bool]
    bScanInfrastructure: Optional[bool]
    bScanWeb: Optional[bool]

    def find_by_unique(self) -> Optional["Asset"]:
        """
        Find a object by unique query.

        :return: Asset object if found, else None
        :rtype: Optional[Asset]
        """

        for instance in self.get_by_parent(
            parent_id=self.parentId, parent_module=self.parentModule
        ):
            if instance.name == self.name:
                return instance
        return None

    @staticmethod
    def _get_additional_endpoints() -> ConfigDict:
        """
        Get additional endpoints for the Assets model.

        :return: A dictionary of additional endpoints
        :rtype: ConfigDict
        """
        return ConfigDict(
            drilldown="/api/{model_slug}/drilldown/{strMonth}/{strCategory}",
            get_count="/api/{model_slug}/getCount",
            graph="/api/{model_slug}/graph",
            graph_by_date="/api/{model_slug}/graphByDate/{strGroupBy}/{year}",
            filter_dashboard="/api/{model_slug}/filterDashboard/{dtStart}/{dtEnd}",
            dashboard="/api/{model_slug}/dashboard/{strGroupBy}",
            dashboard_by_parent="/api/{model_slug}/dashboardByParent/{strGroupBy}/{intId}/{strModule}",
            schedule="/api/{model_slug}/schedule/{year}/{dvar}",
            report="/api/{model_slug}/report/{strReport}",
            filter_assets="/api/{model_slug}/filterAssets",
            query_by_custom_field="/api/{model_slug}/queryByCustomField/{strFieldName}/{strValue}",
        )

    # Legacy code

    @classmethod
    def find_os(cls, os_string: str) -> str:
        """
        Determine the RegScale OS from a string.

        :param str os_string: String containing OS information or description
        :return: RegScale compatible OS string
        :rtype: str
        """
        if "windows" in os_string.lower():
            return "Windows Server"
        elif "linux" in os_string.lower():
            return "Linux"
        elif "mac" in os_string.lower():
            return "Mac OSX"
        else:
            return "Other"

    @staticmethod
    def from_dict(obj: dict) -> "Asset":
        """
        Create Asset object from dict

        :param dict obj: Asset object as a dictionary
        :return: Asset class
        :rtype: Asset
        """
        if isinstance(obj, dict) and "assetOwnerId" not in obj.keys():
            obj["assetOwnerId"] = "Unknown"
        return Asset(**obj)

    # 'uniqueness': 'ip, macaddress'
    # Enable object to be hashable
    def __hash__(self):
        """
        Enable object to be hashable

        :return: Hashed TenableAsset
        :rtype: int
        """
        return hash(
            (
                self.name,
                self.ipAddress,
                self.macAddress.lower() if self.macAddress else None,
                self.assetCategory,
                self.assetType,
                self.fqdn,
                self.parentId,
                self.parentModule,
                self.description,
                self.notes,
            )
        )

    def __getitem__(self, key: Any) -> any:
        """
        Get attribute from Pipeline

        :param any key: Key to get value of
        :return: value of provided key
        :rtype: any
        """
        return getattr(self, key)

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Set attribute in Pipeline with provided key

        :param any key: Key to change to provided value
        :param any value: New value for provided Key
        :return: None
        """
        return setattr(self, key, value)

    def __eq__(self, other) -> "Asset":
        """
        Update items in Asset class

        :param other: Asset object to compare to
        :return: Updated Asset
        :rtype: Asset
        """
        return (
            self.name == other.name
            and self.ipAddress == other.ipAddress
            and self.macAddress == other.macAddress
            and self.wizId == other.wizId
            and self.description == other.description
            and self.notes == other.notes
            and self.status == other.status
            and self.parentId == other.parentId
            and self.otherTrackingNumber == other.otherTrackingNumber
            and self.parentModule == other.parentModule
        )

    @staticmethod
    def insert_asset(
        app: Application,
        obj: Any,
        retry_count: Optional[int] = 3,
    ) -> Response:
        """
        Create an asset in RegScale via API

        :param Application app: Application Instance
        :param Any obj: Asset Object
        :param Optional[int] retry_count: Number of times to retry if it fails, defaults to 3
        :return: Response from RegScale after inserting the provided asset object
        :rtype: Response
        """
        url = urljoin(app.config["domain"], "/api/assets")
        if isinstance(obj, Asset):
            obj = obj.dict()
        api = Api(app)
        res = api.post(url=url, json=obj)
        if not res.ok:
            if res.status_code == 500:
                app.logger.error(
                    "%i: %s\nError creating asset: %s", res.status_code, res.text, obj
                )
            # as long as the status code is not 500, retry
            while res.status_code != 500 and retry_count >= 0:
                app.logger.warning(
                    "Retrying to create asset, attempts remaining: %i", retry_count
                )
                res = api.post(url=url, json=obj)
                retry_count -= 1
                if res.ok:
                    app.logger.info(
                        "[green]Successfully created asset: %s", res.json()["id"]
                    )
                    break
            if retry_count < 0:
                app.logger.error(
                    "%i: %s\n[red]Failed to create asset: %s",
                    res.status_code,
                    res.reason,
                    obj,
                )
        return res

    @staticmethod
    def update_asset(
        app: Application,
        obj: Any,
    ) -> Response:
        """
        Create an asset in RegScale via API

        :param Application app: Application Instance
        :param Any obj: Asset Object
        :return: Response from RegScale after inserting the provided asset object
        :rtype: Response
        """
        url = urljoin(app.config["domain"], f"/api/assets/{obj['id']}")
        if isinstance(obj, Asset):
            obj = obj.dict()
        api = Api(app)
        res = api.put(url=url, json=obj)
        if res.status_code != 200:
            app.logger.error("Error updating asset: %s", obj)
        return res

    @staticmethod
    def fetch_assets_by_module(
        app: Application, parent_id: int, parent_module: str
    ) -> List["Asset"]:
        """
        Find all assets in a module by parent id and parent module

        :param Application app: Application Instance
        :param int parent_id: Parent Id
        :param str parent_module: Parent Module
        :return: List of Assets
        :rtype: List[Asset]
        """
        api = Api(app)
        logger = app.logger
        existing_assets = []
        try:
            response = api.get(
                url=urljoin(
                    app.config["domain"],
                    f"/api/assets/getAllByParent/{parent_id}/{parent_module}",
                )
            )
            existing_assets = (
                [Asset(**asset) for asset in response.json()] if response.ok else []
            )
        except JSONDecodeError:
            logger.error(
                "Error fetching assets by module: %s, %s", parent_id, parent_module
            )
        return existing_assets

    @staticmethod
    def bulk_insert(
        app: Application,
        assets: List["Asset"],
        max_workers: Optional[int] = 30,
        retries: Optional[int] = 3,
        batch_size: Optional[int] = 100,
        batch: Optional[bool] = False,
    ) -> List[Response]:
        """
        Bulk insert assets using the RegScale API and ThreadPoolExecutor

        :param Application app: Application Instance
        :param List[Asset] assets: Asset List
        :param Optional[int] max_workers: Max Workers, defaults to 30
        :param Optional[int] retries: Number of times to retry if it fails, defaults to 3
        :param Optional[int] batch_size: Number of assets to insert per batch, defaults to 100
        :param Optional[bool] batch: Insert assets in batches, defaults to False
        :return: List of Responses from RegScale
        :rtype: List[Response]
        """
        url = urljoin(app.config["domain"], "/api/assets/batchcreate")
        api = Api(app)
        results = []
        if batch:
            # Chunk list into batches
            batches = [
                assets[i : i + batch_size] for i in range(0, len(assets), batch_size)
            ]

            with Progress() as progress:
                total_task = progress.add_task(
                    "[red]Creating Total Assets", total=len(assets)
                )
                for batch in batches:
                    res = api.post(url=url, json=[asset.dict() for asset in batch])
                    if not res.ok:
                        app.logger.error(
                            "%i: %s\nError creating batch of assets: %s",
                            res.status_code,
                            res.text,
                            batch,
                        )
                    results.append(res)
                    progress.update(total_task, advance=len(batch))

            return results
        # Deprecated in favor of batch
        else:
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                workers = [
                    executor.submit(
                        Asset.insert_asset,
                        app,
                        asset,
                        retries,
                    )
                    for asset in assets
                ]
            return [worker.result() for worker in workers] or []

    @staticmethod
    def bulk_update(
        app: Application,
        assets: List["Asset"],
        max_workers: int = 30,
        batch_size: Optional[int] = 100,
        batch: Optional[bool] = False,
    ) -> List[Response]:
        """Bulk insert assets using the RegScale API and ThreadPoolExecutor

        :param Application app: Application Instance
        :param List[Asset] assets: Asset List
        :param Optional[int] max_workers: Max Workers, defaults to 30
        :param Optional[int] batch_size: Number of assets to insert per batch, defaults to 100
        :param Optional[bool] batch: Insert assets in batches, defaults to False
        :return: List of Responses from RegScale
        :rtype: List[Response]
        """
        url = urljoin(app.config["domain"], "/api/assets/batchupdate")
        api = Api(app)
        results = []
        if batch:
            # Chunk list into batches
            batches = [
                assets[i : i + batch_size] for i in range(0, len(assets), batch_size)
            ]
            with Progress() as progress:
                total_task = progress.add_task(
                    "[red]Updating Total Assets", total=len(assets)
                )
                for batch in batches:
                    res = api.put(url=url, json=[asset.dict() for asset in batch])
                    if not res.ok:
                        app.logger.error(
                            "%i: %s\nError batch updating assets: %s",
                            res.status_code,
                            res.text,
                            batch,
                        )
                    results.append(res)
                    progress.update(total_task, advance=len(batch))
            return results
        else:
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                workers = [
                    executor.submit(
                        Asset.update_asset,
                        app,
                        asset,
                    )
                    for asset in assets
                ]
            return [worker.result() for worker in workers] or []

    @staticmethod
    def find_assets_by_parent(
        app: Application,
        parent_id: int,
        parent_module: str,
    ) -> List["Asset"]:
        """
        Find all assets by parent id and parent module

        :param Application app: Application Instance
        :param int parent_id: Parent Id
        :param str parent_module: Parent Module
        :return: List of Assets
        :rtype: List[Asset]
        """
        api = Api(app)
        try:
            res = api.get(
                url=urljoin(
                    app.config["domain"],
                    f"/api/assets/getAllByParent/{parent_id}/{parent_module}",
                )
            )
            existing_assets = [Asset(**asset) for asset in res.json()] if res.ok else []
        except JSONDecodeError:
            existing_assets = []
        return existing_assets

    @staticmethod
    def fetch_asset_by_id(asset_id: int) -> Optional[dict]:
        """
        Find all assets by parent id and parent module

        :param int asset_id: RegScale Asset ID number
        :return: Asset, if found
        :rtype: Optional[dict]
        """
        app = Application()
        api = Api(app)
        url = urljoin(app.config["domain"], f"/api/assets/{asset_id}")
        try:
            res = api.get(url=url)
            if res.ok:
                return res.json()
        except JSONDecodeError:
            return None
