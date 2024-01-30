
def test_loop_manifest():
    from runloop import loop, runloop_manifest

    @loop
    def handle_input(self, metadata: dict[str, str], input: list[str]) -> tuple[list[str], dict[str, str]]:
        pass

    manifest = [x for x in runloop_manifest.loops() if x.name == "handle_input"][0]
    assert len(runloop_manifest.loops()) > 0
    assert manifest.name == "handle_input"
    assert manifest.module == "tests.lambdas.test_lambdas"
