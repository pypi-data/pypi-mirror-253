import importlib
import os
import sys
from pathlib import Path

_user_directory = Path(__file__).resolve().parent / "user"


def test_module_simple():
    sys.path.append(str(_user_directory))
    module = importlib.import_module("simple")
    import runloop
    manifest = [x for x in runloop.runloop_manifest.loops() if x.name == "simple_echo"][0]

    method = getattr(module, f"{manifest.name}")
    echo_response = method({}, ["hello simple"])
    assert echo_response[0][0] == "hello simple to you!"


def test_module_dynamic():
    # Load simple_load, which dynamically creates our module
    from .user.dynamic import simple_loop

    # Load our module by name
    module = importlib.import_module("dynamic_module")
    import runloop
    manifest = [x for x in runloop.runloop_manifest.loops() if x.name == "dynamic_echo"][0]

    # Load loop via manifest
    method = getattr(module, manifest.name)
    echo_response = method({}, ["hello dynamic"])
    assert echo_response[0][0] == "hello dynamic to you!"


def test_module_nested():
    sys.path.append(str(_user_directory))
    module = importlib.import_module("nested")
    import runloop
    manifest = [x for x in runloop.runloop_manifest.loops() if x.name == "nested"][0]

    method = getattr(module, f"{manifest.name}")
    echo_response = method({}, ["hello nested"])
    assert echo_response[0][0] == "hello nested to you!"


def test_single_file():
    # NOTE: In theory this is equivalent to module loading
    namespace = {}
    with open(_user_directory / "file/single_file_loop.py") as file:
        exec(file.read(), namespace)

    import runloop
    manifest = [x for x in runloop.runloop_manifest.loops() if x.name == "single_file_echo"][0]
    method = namespace[manifest.name]
    echo_response = method({}, ["hello nested"])
    assert echo_response[0][0] == "single_file_echo hello nested to you!"
