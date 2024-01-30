
import json
import os
import re
from asyncio import AbstractEventLoop
from typing import Any, List, Optional

from betterproto import Message
from compipe.utils.logging import logger
from google.protobuf import any_pb2
from google.protobuf.struct_pb2 import ListValue
from ugrpc_pipe import (CommandParserReq, GenericResp, ProjectInfoResp,
                        UGrpcPipeStub)

from .engine_pipe_abstract import EngineAbstract, EnginePlatform
from .engine_pipe_decorator import grpc_call_general
from .engine_stub_interface import (GRPC_INTERFACE_METHOD_HEADER,
                                    INTERFACE_MAPPINGS, GRPCInterface)
from betterproto.lib.google import protobuf
from google.protobuf import wrappers_pb2, struct_pb2


class BaseEngineImpl(EngineAbstract):
    _event_loop: AbstractEventLoop = None
    _stub: Any = None

    @property
    def stub(self):
        return self._stub

    @stub.setter
    def stub(self, value):
        self._stub = value

    @property
    def event_loop(self) -> AbstractEventLoop:
        return self._event_loop

    @event_loop.setter
    def event_loop(self, value):
        self._event_loop = value

    @property
    def engine_platform(self) -> str:
        raise NotImplementedError

    @classmethod
    def unpack(cls, data: protobuf.Any) -> Any:
        any_obj = any_pb2.Any()
        any_obj.type_url = data.type_url
        any_obj.value = data.value
        if any_obj.Is(wrappers_pb2.StringValue.DESCRIPTOR):
            unpacked_str_value = wrappers_pb2.StringValue()
            any_obj.Unpack(unpacked_str_value)
            return unpacked_str_value.value
        elif any_obj.Is(struct_pb2.ListValue.DESCRIPTOR):
            results = []
            unpacked_list_value = struct_pb2.ListValue()
            any_obj.Unpack(unpacked_list_value)
            for value in unpacked_list_value.values:
                field = value.WhichOneof('kind')
                if field == 'number_value':
                    results.append(value.number_value)
                elif field == 'string_value':
                    results.append(value.string_value)
                elif field == 'bool_value':
                    results.append(value.bool_value)
            return results
        elif any_obj.Is(wrappers_pb2.Int32Value.DESCRIPTOR):
            unpacked_int_value = wrappers_pb2.Int32Value()
            any_obj.Unpack(unpacked_int_value)
            return unpacked_int_value.value
        elif any_obj.Is(wrappers_pb2.BoolValue.DESCRIPTOR):
            unpacked_bool_value = wrappers_pb2.BoolValue()
            any_obj.Unpack(unpacked_bool_value)
            return unpacked_bool_value.value
        else:
            logger.warning(
                f"Not found matched data type to unpack: {any_obj.DESCRIPTOR}")
            return None


class SimulationEngineImpl(BaseEngineImpl):

    @property
    def stub(self) -> UGrpcPipeStub:
        return self._stub

    @stub.setter
    def stub(self, value):
        self._stub = value

    @property
    def asset_root_folder_name(self) -> str:
        pass

    # keep a copy of the cached project info
    _project_info: ProjectInfoResp = None

    # retrieve full command chains from the specified name
    def resolve_command_name(self, cmd: GRPCInterface):
        if cmd not in INTERFACE_MAPPINGS:
            raise KeyError("Not found the specific key: {cmd}")
        if (command_str := INTERFACE_MAPPINGS[cmd].get(EnginePlatform[self.engine_platform], None)) == None:
            raise ValueError(
                f"Not found the matched command: {cmd}: {self.engine_platform}")
        return command_str

    def command_parser_request(self, cmd: GRPCInterface, params: List = []) -> CommandParserReq:

        return CommandParserReq(payload=json.dumps({
            'type': self.resolve_command_name(cmd=cmd),
            'parameters': params
        }))

    @grpc_call_general()
    def command_parser(self, cmd: GRPCInterface, params: List = [], return_type: Any = None, verbose: bool = False, timeout: Optional[float] = None) -> GenericResp:

        logger.debug(f"Execute command: {cmd.name} : {params}")

        # parse full command str from the specific engine platform
        cmd_str = self.resolve_command_name(cmd=cmd)

        # parse command mode: method/property(static)
        # to involve the correct way to call through reflection
        is_method: bool = bool(
            re.match(fr'{GRPC_INTERFACE_METHOD_HEADER}_.*', cmd.name, re.IGNORECASE))

        # parse the module type name and method name from the full command str
        # i.e., UGrpc.SystemUtils.GetProjectInfo
        # -> cls: UGrpc.SystemUtils
        # -> method: GetProjectInfo
        # The method can be resolved through the reflection / delegate on the specific engine platform
        type_name, method_name = os.path.splitext(cmd_str)

        payload = {
            'type': type_name,
            'isMethod': is_method,
            # remove the '.' from method name segment
            'method': method_name[1:],
            'parameters': [value for value in map(lambda n: '%@%'.join([str(v) for v in n]) if isinstance(n, List) else n, params)]
        }

        command_parser_req = CommandParserReq(payload=json.dumps(payload))

        if verbose:
            logger.debug(f"Command command: {cmd}")
            logger.debug(f"Command payload: {command_parser_req.payload}")

        resp = self.event_loop.run_until_complete(
            self.stub.command_parser(command_parser_req, timeout=timeout))

        return_resp = None

        if not return_type and isinstance(resp.payload, protobuf.Any):
            resp.payload = BaseEngineImpl.unpack(resp.payload)
            return_resp = resp
        else:
            try:
                return_resp = return_type().parse(resp.payload.value)
            except:
                pass

            # # try to cast payload into the specific type
            # caller_code_obj = inspect.stack()[2].frame.f_code
            # # retrieve function from the gc referrers list
            # upper_callers = [obj for obj in gc.get_referrers(caller_code_obj) if hasattr(
            #     obj, '__code__') and obj.__code__ is caller_code_obj][0]

        # support casting into the message object
        return return_resp

    @grpc_call_general()
    def get_project_info(self, is_reload: bool = False) -> ProjectInfoResp:
        """Retrieve the current project context of the connected engine.

        Args:
            is_reload (bool, optional): Represent the flag of force re-retrieving project info. Defaults to False.

        Returns:
            ProjectInfoResp: Represent the returned project context
        """
        if not self._project_info or is_reload:

            # retrieve the project info from the engine / platform
            self._project_info = self.command_parser(
                cmd=GRPCInterface.method_system_get_projectinfo, return_type=ProjectInfoResp)

        return self._project_info

    def get_service_status(self) -> bool:
        try:
            resp = self.command_parser(
                cmd=GRPCInterface.method_system_get_service_status, return_type=GenericResp)
            return True if resp.status == 0 else False

        except Exception as e:
            return False
