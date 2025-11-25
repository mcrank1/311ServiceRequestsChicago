import requests
import pandas as pd

#API endpoint for Chicago 311 Service Requests
API_URL = "https://data.cityofchicago.org/resource/v6vf-nfxy.json?$limit=500"

#Fetch data
response = requests.get(API_URL)
data = response.json()

#Load data into a pandas dataframe
df = pd.DataFrame(data)

#Keep only relevant columns

df = df [["sr_number", "sr_type", "status", "created_date"]]

#convert dates to datetime
df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce")

#Drop rows with missing data
df = df.dropna(subset=["created_date", "sr_number"])

#Simple Analysis

#Total number of requests
print("Total Requests:", df.shape[0])

#Count by request type
print("\nRequests by Type:")
print(df["sr_type"].value_counts())


#Daily trend
print("\nRequests per Day:")
daily_counts = df.groupby(df["created_date"].dt.date).size()
print(daily_counts)

#Latest 5 Requests
print("\nLatest 5 Requests:")
print(df.sort_values(by="created_date", ascending=False).head(5))
