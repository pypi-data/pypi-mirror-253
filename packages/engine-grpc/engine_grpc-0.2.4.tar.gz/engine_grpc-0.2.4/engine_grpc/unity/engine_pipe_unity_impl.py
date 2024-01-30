import time
from ..engine_pipe_impl import SimulationEngineImpl
from ..engine_pipe_abstract import EnginePlatform
from typing import List
from ..engine_stub_interface import GRPCInterface
from ugrpc_pipe import ProjectInfoResp, GenericResp
import os
import re
from re import Pattern
import grpclib


class UnityEngineImpl(SimulationEngineImpl):
    @property
    def engine_platform(self) -> str:

        return EnginePlatform.unity.name


class UnityEditorImpl(SimulationEngineImpl):

    asset_root_folder_name: str = "Assets"

    @property
    def engine_platform(self) -> str:

        return EnginePlatform.unity_editor.name

    def find_asset_guid_list(self, filter: str, paths: List[str]) -> List[str]:

        resp = self.command_parser(cmd=GRPCInterface.method_editor_assetdatabase_find_assets,
                                   params=[filter,
                                           paths])
        return resp.payload

    def find_assets(self, filter: str, paths: List[str]) -> List[str]:

        guid_list = self.find_asset_guid_list(filter=filter, paths=paths)

        asset_paths = []

        for guid in guid_list:
            asset_paths.append(self.command_parser(
                cmd=GRPCInterface.method_editor_assetdatabase_guid_to_path, params=[guid]).payload)

        return asset_paths

    def find_assets_by_regex(self, filter: str, paths: List[str], pattern: Pattern) -> List[str]:

        assets = self.find_assets(filter=filter, paths=paths)
        result = []
        for asset_path in assets:
            if pattern.search(asset_path):
                result.append(asset_path)

        return result

    def get_dependencies(self, path: str, recursive: bool) -> List[str]:

        return self.command_parser(cmd=GRPCInterface.method_editor_assetdatabase_get_dependencies, params=[path, recursive]).payload

    def get_project_info(self) -> ProjectInfoResp:

        return self.command_parser(cmd=GRPCInterface.method_system_get_projectinfo, return_type=ProjectInfoResp)

    def fetch_full_path(self, path: str) -> str:
        if not path.startswith(self.asset_root_folder_name):
            raise ValueError(
                f"The specified path is invalid: {path}. Path should start with '{self.asset_root_folder_name}'")

        return os.path.join(self.get_project_info().project_root, path)

    def quit_without_saving(self) -> None:

        try:
            self.command_parser(
                cmd=GRPCInterface.method_system_quit_without_saving)
        except grpclib.exceptions.StreamTerminatedError as e:
            print(e)

    def wait_until_unity_editor_launched(self, timeout: float = 15.0) -> None:

        while not self.get_service_status():
            time.sleep(1.0)
            timeout -= 1.0

            if timeout <= 0.0:
                raise TimeoutError(
                    f"Timeout while waiting for Unity Editor launched")
