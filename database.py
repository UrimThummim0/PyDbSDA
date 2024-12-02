import streamlit as st
import pandas as pd

# Function to load the data from either URL or local path
def load_data(url, local_path):
    try:
        # Attempt to load data from URL
        df = pd.read_csv(url, sep=",")
    except:
        # Fallback to local file if URL fails
        try:
            df = pd.read_csv(local_path, sep=",")
        except Exception as e:
            st.error(f"Error loading the data: {str(e)}")
            df = pd.DataFrame()  # Return an empty dataframe as a fallback
    return df

# Function to plot the bar chart
def plot_bar_chart(df, x_col, y_cols, title, subtitle, colors):
    st.header(title)
    st.subheader(subtitle)
    st.bar_chart(df.set_index(x_col)[y_cols], color=colors)

# Function to display class data
def display_class_data(class_name, file_name, url, local_path, colors):
    df = load_data(url, local_path)
    if not df.empty:
        plot_bar_chart(df, x_col="sabata", y_cols=["mambra_tonga", "nianatra_im-pito"], 
                       title=f"Tahan'ny fianarana im-pito - {class_name}", subtitle=f"Kilasy {class_name}", 
                       colors=colors)

# URL and local paths
base_url = "https://raw.githubusercontent.com/UrimThummim0/python-project/main/"
local_dir = "database/"

# Set session state for tracking the visibility of the main title and page content
if "dashboard_shown" not in st.session_state:
    st.session_state.dashboard_shown = False

# Main page title only appears if dashboard is not shown
if not st.session_state.dashboard_shown:
    st.title("Tongasoa eto amin'ny fizahana ny :blue[antontan'isa] eto amin'ny Fiangonantsika.")

# Sidebar with navigation buttons
with st.sidebar:
    st.logo("media/sda.png")
    st.text("SDA Ivandry - Dashboard")
    st.header("Sekoly Sabata")
    st.subheader("Tahan'ny fianarana lesona im-pito nandritry ny telovolana")
    st.subheader("Telovolana faha-4")

# Button to trigger class data display
if st.button("Lehibe"):
    display_class_data("Lehibe", "ivandry_ss_db_lehibe.csv", f"{base_url}ivandry_ss_db_lehibe.csv", f"{local_dir}ivandry_ss_db_lehibe.csv", ["#808080", "#ffff00"])
    st.session_state.dashboard_shown = True
if st.button("Tanora Zokiny"):
    display_class_data("Tanora Zokiny", "ivandry_ss_db_tanorazokiny.csv", f"{base_url}ivandry_ss_db_tanorazokiny.csv", f"{local_dir}ivandry_ss_db_tanorazokiny.csv", ["#808080", "#ff1e1e"])
    st.session_state.dashboard_shown = True
if st.button("Zatovo"):
    display_class_data("Zatovo", "ivandry_ss_db_zatovo.csv", f"{base_url}ivandry_ss_db_zatovo.csv", f"{local_dir}ivandry_ss_db_zatovo.csv", ["#808080", "#ff1e10"])
    st.session_state.dashboard_shown = True
if st.button("Mantoanto"):
    display_class_data("Mantoanto", "ivandry_ss_db_mantoanto.csv", f"{base_url}ivandry_ss_db_mantoanto.csv", f"{local_dir}ivandry_ss_db_mantoanto.csv", ["#808080", "#ff1e1e"])
    st.session_state.dashboard_shown = True
if st.button("Tanora Zandriny"):
    display_class_data("Tanora Zandriny", "ivandry_ss_db_tanorazandriny.csv", f"{base_url}ivandry_ss_db_tanorazandriny.csv", f"{local_dir}ivandry_ss_db_tanorazandriny.csv", ["#808080", "#ff1e1e"])
    st.session_state.dashboard_shown = True
if st.button("Ankizy"):
    display_class_data("Ankizy", "ivandry_ss_db_ankizy.csv", f"{base_url}ivandry_ss_db_ankizy.csv", f"{local_dir}ivandry_ss_db_ankizy.csv", ["#808080", "#ff1e1e"])
    st.session_state.dashboard_shown = True
if st.button("Zaza Minono"):
    display_class_data("Zaza Minono", "ivandry_ss_db_zazaminono.csv", f"{base_url}ivandry_ss_db_zazaminono.csv", f"{local_dir}ivandry_ss_db_zazaminono.csv", ["#808080", "#ff1e1e"])
    st.session_state.dashboard_shown = True
if st.button("Zaza Bodo"):
    display_class_data("Zaza Bodo", "ivandry_ss_db_zazabodo.csv", f"{base_url}ivandry_ss_db_zazabodo.csv", f"{local_dir}ivandry_ss_db_zazabodo.csv", ["#808080", "#ff1e1e"])
    st.session_state.dashboard_shown = True
