# Day-to-week-conversion

### A Streamlit app to input days and convert it into weeks and save all data to MongoDB. Supports error correction scenarios.

## Feature:
1.Input any number of day values dynamically

2.Converts each input into weeks + remaining days

3.Saves results to MongoDB

## Algorithm

Connect to MongoDB (DAYS database, CONVERSIONS collection)

Ask how many conversions user wants

Dynamically generate input fields

On "Convert & Save":

Convert days → weeks and remaining days

Display results

Save all records to MongoDB

## Installation:
```
pip install streamlit pymongo
streamlit run days_to_weeks.py
```

## Program Code (days_to_weeks.py):

```
import streamlit as st
from pymongo import MongoClient

st.title("Days to Weeks Converter")

# connect to MongoDB
try:
    client = MongoClient("mongodb://127.0.0.1:27017/")
    # create database
    db = client["database_name"]
    # create collection
    collection = db["collection_name"]
    st.success("Connected to MongoDB")
except Exception as e:
    st.error(f"Failed to connect to MongoDB: {e}")

days = st.number_input("Enter number of days:", min_value=0, step=1, value=0)

if days is not None:
    # Calculate weeks and remaining days
    weeks = days // 7
    remaining_days = days % 7

    # Display result
    st.write(f"{weeks} week(s) and {remaining_days} day(s)")
    
    # Insert data into MongoDB
    if st.button("Save to Database"):
        data = {"days": days, "weeks": weeks, "remaining_days": remaining_days}
        collection.insert_one(data)
        st.success("Data saved to MongoDB!")
```

## Output:

<img width="1919" height="906" alt="Screenshot 2026-02-13 190717" src="https://github.com/user-attachments/assets/ecee9e7d-d7f1-42a0-b920-43be4dd0bcec" />
<img width="1425" height="1006" alt="Screenshot 2026-02-13 190702" src="https://github.com/user-attachments/assets/b64e5371-9360-4a55-86fa-0e06d7c6f5c4" />

