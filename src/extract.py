import requests

#Build the api url
url = "https://stats.oecd.org/SDMX-JSON/data/PRICES_CPI/..GY.CPALTT01.IXOB.R/all?startTime=2023-1&endTime=2023-12"

# Fetch data
def fetch_data_cpi():
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch data")
    return response.json()

json_data = fetch_data_cpi()
