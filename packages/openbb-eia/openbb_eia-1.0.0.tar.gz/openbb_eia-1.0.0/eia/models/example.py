"""Example Data Integration.

The OpenBB Platform gives developers easy tools for integration.

To use it, developers should:
1. Define the request/query parameters.
2. Define the resulting data schema.
3. Define how to fetch raw data.

First 2 steps make sure developers really get to know their data.
This is called the "Know Your Data" principle.

Note: The format of the QueryParams and Data is defined by a pydantic model that can
be entirely custom, or inherit from the OpenBB standardized models.

This file shows an example of how to integrate data from a provider.
"""
# pylint: disable=unused-argument
from typing import Any, Dict, List, Optional
from pydantic import Field
from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.abstract.query_params import QueryParams
from ..utils.helpers import get_ts
from typing import List
import pandas as pd

class EIAQueryParams(QueryParams):
    ''' US Energy Intelligence series codes '''
    series: List[str] = Field(default=[], description="List of EIA series identifiers.")

# class EIAQueryParams(QueryParams):
#     ''' US Energy Inteligence series code '''
#     series: str = Field(default="",description="EIA series identifier.")

class EIATimeSeriesData(Data):
    date: str = Field(description="Date of the data point.")
    value: float = Field(description="Value of the data point.")
    series_name: str = Field(description="Name of the EIA series.")

class EIAFetcher(Fetcher[EIAQueryParams, List[EIATimeSeriesData]]):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> EIAQueryParams:
        return EIAQueryParams(**params)

    @staticmethod
    async def extract_data(query: EIAQueryParams, credentials: Optional[Dict[str, str]], **kwargs: Any) -> List[dict]:
        api_key = credentials.get("eia_api_key") if credentials else ""
        response = await get_ts(query.series, api_key)  # Use 'await' to get the actual response
        return response

    @staticmethod
    def transform_data(query: EIAQueryParams, data: pd.DataFrame, **kwargs: Any) -> List[EIATimeSeriesData]:
        # Reshape the DataFrame from wide format to long format
        melted_data = data.melt(id_vars=['period'], var_name='series_name', value_name='value')

        # Convert the melted DataFrame to a list of EIATimeSeriesData objects
        transformed_data = [
            EIATimeSeriesData(date=row['period'], value=row['value'], series_name=row['series_name'])
            for _, row in melted_data.iterrows()
        ]

        return transformed_data