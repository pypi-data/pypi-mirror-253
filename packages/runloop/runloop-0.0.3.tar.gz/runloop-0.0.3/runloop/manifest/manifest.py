from dataclasses import dataclass
from typing import List


@dataclass
class LoopManifest:
    name: str
    module: str


class RunloopManifest:
    def __init__(self):
        self._lambdas: List[LoopManifest] = []

    def register_loop(self, loop: LoopManifest):
        self._lambdas.append(loop)

    def loops(self) -> List[LoopManifest]:
        return self._lambdas


runloop_manifest: RunloopManifest = RunloopManifest()
