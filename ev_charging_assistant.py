import streamlit as st
import geopy.distance
from datetime import datetime

# ------------------ MOCK DATA ------------------ #
CHARGING_STATIONS = [
    {"name": "ChargeHub A", "location": (37.7749, -122.4194), "available": True},
    {"name": "EVgo B", "location": (36.7783, -119.4179), "available": False},
    {"name": "Tesla Supercharger C", "location": (35.3733, -119.0187), "available": True},
    {"name": "ChargePoint D", "location": (34.0522, -118.2437), "available": True},
    {"name": "Blink E", "location": (33.4484, -112.0740), "available": False},
]

# ------------------ UTILS ------------------ #
def haversine(coord1, coord2):
    return geopy.distance.distance(coord1, coord2).km

def find_stations_near_route(start, end, battery_level, max_range_km):
    midpoint = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
    recommendations = []

    for station in CHARGING_STATIONS:
        dist_to_midpoint = haversine(station["location"], midpoint)
        dist_to_start = haversine(station["location"], start)

        if station["available"] and dist_to_start <= max_range_km * (battery_level / 100):
            recommendations.append({
                "name": station["name"],
                "location": station["location"],
                "distance_from_start": round(dist_to_start, 2),
                "estimated_arrival_time": datetime.now().strftime('%H:%M')
            })

    recommendations.sort(key=lambda x: x["distance_from_start"])
    return recommendations

# ------------------ STREAMLIT UI ------------------ #
st.title("AI-based EV Charging Stop Recommender")

with st.form("user_input"):
    st.subheader("Enter Trip Details")
    start_lat = st.number_input("Start Latitude", value=37.7749)
    start_lon = st.number_input("Start Longitude", value=-122.4194)
    end_lat = st.number_input("End Latitude", value=34.0522)
    end_lon = st.number_input("End Longitude", value=-118.2437)
    battery_level = st.slider("Current Battery Level (%)", min_value=0, max_value=100, value=60)
    max_range = st.number_input("Max Range on Full Battery (km)", value=400)
    submitted = st.form_submit_button("Find Charging Stops")

if submitted:
    start_coord = (start_lat, start_lon)
    end_coord = (end_lat, end_lon)

    st.info("Finding optimal charging stations...")
    results = find_stations_near_route(start_coord, end_coord, battery_level, max_range)

    if results:
        st.success(f"Found {len(results)} recommended station(s):")
        for station in results:
            st.markdown(f"**{station['name']}** - {station['distance_from_start']} km from start")
            st.text(f"Location: {station['location']}, ETA: {station['estimated_arrival_time']}")
    else:
        st.warning("No suitable charging stations found within range.")