import pandas as pd
import numpy as np
from datetime import datetime, timedelta

start_date = "2020-01-01"
end_date = datetime.now() + timedelta(days=1)

dates = pd.date_range(start=start_date, end=end_date, freq="10min")

df = pd.DataFrame({
    "timestamp": dates,
    "chain_id": np.random.choice([1,2,3,4,5,6,7,8], len(dates)),
    "request_type": np.random.choice(["price","swap","oracle","nft","defi"], len(dates)),
    "address": np.random.choice(["0x1","0x2","0x3","0x4","0x5"], len(dates)),
    "api_key": np.random.choice(["k1","k2","k3"], len(dates)),
    "oracle_latency": np.random.normal(200, 50, len(dates)),
    "chain_latency": np.random.normal(100, 30, len(dates))
})

# Add anomalies (5%)
for i in range(int(0.05 * len(df))):
    idx = np.random.randint(0, len(df))
    df.loc[idx, "oracle_latency"] = np.random.randint(500, 900)

df.to_csv("dataset.csv", index=False)

print("Dataset updated: 2020 ? tomorrow ?")
