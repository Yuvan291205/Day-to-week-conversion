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
from datetime import datetime

st.title("Days to Weeks Converter")


try:
    client = MongoClient("mongodb://127.0.0.1:27017/")
    db = client["days_to_week_convertor"]
    collection = db["conversions"]
    st.success("Connected to MongoDB")
except Exception as e:
    st.error(f"Failed to connect to MongoDB: {e}")


days_input = st.text_input(
    "Enter days separated by commas (Example: 10, 15, 21)"
)


if st.button("Convert & Save"):

    try:
        input_array = [int(x.strip()) for x in days_input.split(",")]

        output_array = []

        for d in input_array:
            weeks = d // 7
            remaining = d % 7
            output_array.append([weeks, remaining])

            st.write(f"{d} days = {weeks} week(s) and {remaining} day(s)")

        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        document = {
            "timestamp": current_time,
            "input_array": input_array,
            "output_array": output_array
        }

        collection.insert_one(document)

        st.success("Data saved to MongoDB!")

    except:
        st.error("Please enter valid numbers separated by commas.")
```

## Output:
<img width="1919" height="1008" alt="Screenshot 2026-02-17 081022" src="https://github.com/user-attachments/assets/ceeae9a8-a0bc-4b35-94bd-a2be6168b0d0" />

<img width="1013" height="1010" alt="Screenshot 2026-02-17 081003" src="https://github.com/user-attachments/assets/a252e3d2-4ded-4cfe-84b8-5fcd04099d46" />

