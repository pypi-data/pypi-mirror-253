### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from openbb_core.app.static.container import Container
from openbb_core.app.model.obbject import OBBject
from typing import Optional, Literal
from openbb_core.app.static.utils.decorators import validate

from openbb_core.app.static.utils.filters import filter_inputs


class ROUTER_eia(Container):
    """/eia
    historical
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @validate
    def historical(
        self, provider: Optional[Literal["eia"]] = None, **kwargs
    ) -> OBBject:
        """Example Data.

        Parameters
        ----------
        provider : Optional[Literal['eia']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'eia' if there is
            no default.
        series : List[str]
            List of EIA series identifiers. (provider: eia)

        Returns
        -------
        OBBject
            results : List[EIAHistorical]
                Serializable results.
            provider : Optional[Literal['eia']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        EIAHistorical
        -------------
        date : Optional[str]
            Date of the data point. (provider: eia)
        value : Optional[float]
            Value of the data point. (provider: eia)
        series_name : Optional[str]
            Name of the EIA series. (provider: eia)

        Example
        -------
        >>> from openbb import obb
        >>> obb.eia.historical()
        """  # noqa: E501

        return self._run(
            "/eia/historical",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={},
                extra_params=kwargs,
            )
        )
