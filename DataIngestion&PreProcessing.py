import requests
import pandas as pd

url = "https://data.elexon.co.uk/bmrs/api/v1/balancing/pricing/market-index"

params = {
    "from": "2025-01-01T00:00Z",
    "to": "2025-01-02T00:00Z"
}

response = requests.get(url, params=params)

print("Status code:", response.status_code)

data = response.json()
df = pd.DataFrame(data["data"])

df = df[df["dataProvider"] == "APXMIDP"]

df = df[
    [
        "startTime",
        "settlementPeriod",
        "price",
        "volume"    
    ]
]

df = df.sort_values("startTime")
print(df.head(10))