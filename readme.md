#  **_City Map Navigation Project_**

This project is a **City Map Navigation System** developed using Python and Streamlit.  
It demonstrates core concepts of **Data Structures & Algorithms**, including graphs, weighted edges, connectivity checking, and shortest path calculation using **Dijkstra’s Algorithm**.  
The application provides a mini-Google-Maps–style interface where users can add roads, analyze city connectivity, and visualize shortest paths on an interactive map.


---
## **Overview**
This project is a **City Map Navigation System** implemented in Python using **NetworkX**, **Folium**, and **Streamlit**.  
It allows users to:  
- Add roads between cities dynamically  
- Check if two cities are connected  
- Find the **shortest path** between cities using **Dijkstra's algorithm**  
- Visualize cities, roads, and shortest paths on an interactive map  

It works like a mini Google Maps for a custom city network.

---

## **Features**
1. **Add Roads:** Dynamically connect cities with weighted distances  
2. **Check Connectivity:** Verify if two cities are connected  
3. **Shortest Path:** Calculate shortest path and total distance using Dijkstra algorithm  
4. **Interactive Map:**  
   - Blue lines: roads  
   - Red lines: shortest path  
   - Markers: cities  
5. **Persistent State:** Roads and shortest paths persist during interactions using Streamlit session state  

---
#  **Data Structures Used**

This project uses the following core **DSA concepts**:

### **1.Graph (Weighted) – Main Data Structure**
- Implemented using **NetworkX Graph()**
- Cities → Nodes  
- Roads → Weighted edges  
- Supports:
  - Adding nodes  
  - Adding weighted edges  
  - Checking connectivity  
  - Dijkstra shortest path  

### **2.Hash Table (Implicit via Dictionaries)**
NetworkX stores:
- node data  
- edge data  
- weights  
using underlying dictionary structures.

### **3.Lists**
- Paths (list of cities)  
- Dropdown menus for UI  
- Coordinates list for drawing map routes  

➡ Even though we do not create a linked list or tree manually, the graph itself internally uses hashing and adjacency lists.

---

#  **Algorithms Used**

###  **Dijkstra’s Algorithm**
- For shortest path  
- Uses edge weights  
- Returns:
  - City sequence  
  - Total distance  

### **BFS/DFS (handled internally by NetworkX)**
- Used to check connectivity  

---

## **Technologies Used**
- **Python 3.10+**  
- **Streamlit** → Web interface  
- **NetworkX** → Graph structure and shortest path calculations  
- **Folium** → Interactive map visualization  
- **Streamlit-Folium** → Embed Folium maps in Streamlit  

---

## **Project Structure**
**_City Map Navigation_**

├── **``graph.py``** # Graph creation, add roads, predefined cities

├── **``connectivity.py``** # Check if two cities are connected

├── **```shortest_path.py```** # Dijkstra shortest path calculation

├── **``map.py``** # Folium map visualization

├── **``streamlit_app.py``** # Main Streamlit interface

├── **``venv/``** # Virtual environment

└── **``README.md``** # Project documentation


---


#  **How the Project Works**

### **Step 1 – Load Graph**
Cities and predefined roads are loaded into a NetworkX graph.

### **Step 2 – User Interacts Through Streamlit**
User can:
- Add new roads  
- Check connectivity  
- Request shortest path  

### **Step 3 – Compute Shortest Path (Dijkstra)**
If user selects:
- Start city  
- End city  

Then:
- Algorithm calculates shortest path  
- Calculates total distance  

### **Step 4 – Map Visualization (Folium)**
The map displays:
- Blue lines → All existing roads  
- Red line → Shortest path  
- Yellow markers → Cities  

### **Step 5 – Display Results**
The UI displays:
- Path as text  
- Distance in km  
- A beautifully styled map  

---
# **Install dependencies:**

**````pip install streamlit folium networkx streamlit-folium````**
