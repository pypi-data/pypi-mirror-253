### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from openbb_core.app.static.container import Container


class Extensions(Container):
    # fmt: off
    """
Routers:
    /eia

Extensions:
    - eia@1.0.0

    - eia@1.0.0    """
    # fmt: on

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @property
    def eia(self):
        # pylint: disable=import-outside-toplevel
        from . import eia

        return eia.ROUTER_eia(command_runner=self._command_runner)
