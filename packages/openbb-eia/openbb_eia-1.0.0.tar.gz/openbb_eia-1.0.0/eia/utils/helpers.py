import aiohttp
import pandas as pd

async def get_ts(series_list, api_key=None):
    if not api_key:
        raise ValueError("API key is required")

    all_series_data = []
    for series in series_list:
        url = f'https://api.eia.gov/v2/seriesid/{series}?api_key={api_key}'

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise Exception(f"Error fetching data for series {series}: {response.status}")
                json_response = await response.json()

        # Process each series DataFrame
        series_name = json_response.get('response').get('data')[0].get('series-description')
        series_data = pd.DataFrame(json_response.get('response').get('data'), columns=['period', 'value'])
        series_data.set_index('period', inplace=True)
        series_data.rename(columns={'value': series_name}, inplace=True)

        all_series_data.append(series_data)
    # Combine all series data into a single DataFrame with a common 'period' index
    combined_df = pd.concat(all_series_data, axis=1).reset_index()
    return combined_df
