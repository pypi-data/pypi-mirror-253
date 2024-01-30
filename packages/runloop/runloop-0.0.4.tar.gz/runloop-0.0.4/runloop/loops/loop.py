from typing import Callable, Dict, List, Tuple

from runloop.manifest.manifest import LoopManifest, runloop_manifest

LoopSignature = Callable[[Dict[str, str], List[str]], Tuple[List[str], Dict[str, str]]]


def _make_loop_manifest(func: LoopSignature) -> LoopManifest:
    return LoopManifest(
        name=func.__name__,
        module=func.__module__,
    )


def loop(func: LoopSignature) -> LoopSignature:
    """Register Runloop loop lambda.

    // TODO: Relax requirements
    function must be in the definition
    def handle_input(self, metadata: dict[str, str], input: list[str]) -> tuple[list[str], dict[str, str]]:

    Raises
    ------
        ValueError: If function signature is invalid
    """
    runloop_manifest.register_loop(_make_loop_manifest(func))

    return func
