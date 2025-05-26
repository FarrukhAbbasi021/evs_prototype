# AI-Based EV Charging Stop Recommender

This tool recommends optimal EV charging stops along a given route based on battery level, charger availability, and travel preferences.

## Setup

1. Clone the repository or copy the script.
2. Install the required libraries:

```
pip install streamlit geopy
```

3. Run the Streamlit app:

```
streamlit run ev_charging_assistant.py
```

## Sample Inputs

- Start Location: 37.7749, -122.4194 (San Francisco)
- End Location: 34.0522, -118.2437 (Los Angeles)
- Battery Level: 60%
- Max Range: 400 km

## Sample Output

- ChargeHub A - 0.0 km from start
- Tesla Supercharger C - 325.5 km from start

## Deployment

To share the app with your client:
1. Deploy using [Streamlit Community Cloud](https://streamlit.io/cloud) or any web host.
2. Share the app URL.