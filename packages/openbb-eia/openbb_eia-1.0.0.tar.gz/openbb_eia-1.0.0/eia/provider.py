"""openbb_eia OpenBB Platform Provider."""

from openbb_core.provider.abstract.provider import Provider
from eia.models.example import EIAFetcher

# mypy: disable-error-code="list-item"

provider = Provider(
    name="eia",
    description="Data provider for energy information agency",
    # Only add 'credentials' if they are needed.
    # For multiple login details, list them all here.
    credentials=["api_key"],
    website="https://api.eia.gov/v2/seriesid/",
    # Here, we list out the fetchers showing what our provider can get.
    # The dictionary key is the fetcher's name, used in the `router.py`.
    fetcher_dict={
        "EIAHistorical": EIAFetcher,
    }
)
