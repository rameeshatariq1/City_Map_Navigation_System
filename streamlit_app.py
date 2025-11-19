import streamlit as st
from graph import G, cities, add_road
from connectivity import is_connected
from shortest_path import get_shortest_path
from map import create_map
from streamlit_folium import st_folium

# Page config
st.set_page_config(page_title="City Map Navigation", layout="wide", page_icon="🗺️")

# Sidebar Controls

st.sidebar.title(" City Navigation Controls")
st.sidebar.markdown("Manage roads, check connectivity, and find shortest paths between cities.")

# Add Road Section
st.sidebar.subheader("Add Road")
city_list = list(G.nodes)
city1 = st.sidebar.selectbox("From City:", city_list, key="from")
city2 = st.sidebar.selectbox("To City:", city_list, key="to")
distance = st.sidebar.number_input("Distance (km):", min_value=1, step=1, key="dist")

if st.sidebar.button("Add Road"):
    try:
        msg = add_road(city1, city2, distance)
        st.sidebar.success(msg)
    except ValueError as e:
        st.sidebar.error(str(e))

# Connectivity Check
st.sidebar.subheader("Check Connectivity")
city_a = st.sidebar.selectbox("City A:", city_list, key="city_a")
city_b = st.sidebar.selectbox("City B:", city_list, key="city_b")

if st.sidebar.button("Check Connectivity"):
    try:
        connected = is_connected(city_a, city_b)
        if connected:
            st.sidebar.success(f"{city_a} and {city_b} are connected!")
        else:
            st.sidebar.warning(f"{city_a} and {city_b} are NOT connected!")
    except ValueError as e:
        st.sidebar.error(str(e))

# Shortest Path
st.sidebar.subheader("Shortest Path")
start_city = st.sidebar.selectbox("Start City:", city_list, key="start")
end_city = st.sidebar.selectbox("End City:", city_list, key="end")

# Initialize session_state variables
if "shortest_path" not in st.session_state:
    st.session_state.shortest_path = None
if "total_distance" not in st.session_state:
    st.session_state.total_distance = None

if st.sidebar.button("Find Shortest Path"):
    try:
        path, dist = get_shortest_path(start_city, end_city)
        st.session_state.shortest_path = path
        st.session_state.total_distance = dist
        if path:
            st.sidebar.success("Shortest Path Found!")
        else:
            st.sidebar.error("No path exists between these cities.")
    except ValueError as e:
        st.sidebar.error(str(e))
        st.session_state.shortest_path = None
        st.session_state.total_distance = None

# Use session_state variables for display and map
shortest_path = st.session_state.shortest_path
total_distance = st.session_state.total_distance

# Main UI

st.markdown("## **_City Map_**")
st.markdown("Use the sidebar to add roads, check connectivity, and find shortest paths between cities.")

# Display Map
m = create_map(shortest_path=shortest_path, path_distance=total_distance)
st_data = st_folium(m, width=900, height=500)


# Metrics / Info Cards

if shortest_path:
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Shortest Path", value=" → ".join(shortest_path))
    with col2:
        st.metric(label="Total Distance (km)", value=total_distance)

