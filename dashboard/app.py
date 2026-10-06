
import streamlit as st
import pandas as pd


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Nassau Candy Shipping Analysis",
    page_icon="🍬",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

DATA_PATH = "data/Nassau_Candy_Cleaned.csv"

df = pd.read_csv(DATA_PATH)


# ============================================================
# PAGE TITLE
# ============================================================

st.title("🍬 Nassau Candy Distributor")
st.subheader("Factory-to-Customer Shipping Route Efficiency Analysis")

st.markdown(
    """
    This interactive dashboard analyzes shipping performance across
    factories, regions, ship modes, products, and customer routes.
    """
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("🔎 Dashboard Filters")


# Factory filter
factory_options = ["All"] + sorted(
    df["Factory"].dropna().unique().tolist()
)

selected_factory = st.sidebar.selectbox(
    "Select Factory",
    factory_options
)


# Region filter
region_options = ["All"] + sorted(
    df["Region"].dropna().unique().tolist()
)

selected_region = st.sidebar.selectbox(
    "Select Region",
    region_options
)


# Ship Mode filter
ship_mode_options = ["All"] + sorted(
    df["Ship Mode"].dropna().unique().tolist()
)

selected_ship_mode = st.sidebar.selectbox(
    "Select Ship Mode",
    ship_mode_options
)


# Route filter
route_options = ["All"] + sorted(
    df["Route"].dropna().unique().tolist()
)

selected_route = st.sidebar.selectbox(
    "Select Route",
    route_options
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if selected_factory != "All":
    filtered_df = filtered_df[
        filtered_df["Factory"] == selected_factory
    ]


if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]


if selected_ship_mode != "All":
    filtered_df = filtered_df[
        filtered_df["Ship Mode"] == selected_ship_mode
    ]


if selected_route != "All":
    filtered_df = filtered_df[
        filtered_df["Route"] == selected_route
    ]


# ============================================================
# CHECK FILTER RESULT
# ============================================================

if filtered_df.empty:

    st.warning(
        "⚠️ No records match the selected filters. "
        "Please change the filters."
    )

    st.stop()


# ============================================================
# KPI SECTION
# ============================================================

st.markdown("---")
st.header("📊 Key Performance Indicators")


total_shipments = len(filtered_df)

average_lead_time = filtered_df[
    "Shipping Lead Time"
].mean()

factory_count = filtered_df[
    "Factory"
].nunique()

region_count = filtered_df[
    "Region"
].nunique()


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Total Shipments",
        f"{total_shipments:,}"
    )


with col2:
    st.metric(
        "Average Lead Time",
        f"{average_lead_time:.1f} days"
    )


with col3:
    st.metric(
        "Factories",
        factory_count
    )


with col4:
    st.metric(
        "Regions",
        region_count
    )


# ============================================================
# REGION ANALYSIS
# ============================================================

st.markdown("---")
st.header("🌎 Regional Shipping Performance")


region_summary = (
    filtered_df
    .groupby("Region")
    .agg(
        Total_Shipments=("Region", "size"),
        Average_Lead_Time=("Shipping Lead Time", "mean")
    )
    .reset_index()
)


col1, col2 = st.columns(2)


with col1:

    st.subheader("Shipments by Region")

    st.bar_chart(
        region_summary.set_index("Region")[
            "Total_Shipments"
        ]
    )


with col2:

    st.subheader("Average Lead Time by Region")

    st.bar_chart(
        region_summary.set_index("Region")[
            "Average_Lead_Time"
        ]
    )


# ============================================================
# SHIP MODE ANALYSIS
# ============================================================

st.markdown("---")
st.header("🚚 Shipping Mode Performance")


ship_mode_summary = (
    filtered_df
    .groupby("Ship Mode")
    .agg(
        Total_Shipments=("Ship Mode", "size"),
        Average_Lead_Time=("Shipping Lead Time", "mean")
    )
    .reset_index()
)


st.subheader("Shipments by Ship Mode")

st.bar_chart(
    ship_mode_summary.set_index("Ship Mode")[
        "Total_Shipments"
    ]
)


# ============================================================
# FACTORY ANALYSIS
# ============================================================

st.markdown("---")
st.header("🏭 Factory Performance")


factory_summary = (
    filtered_df
    .groupby("Factory")
    .agg(
        Total_Shipments=("Factory", "size"),
        Average_Lead_Time=("Shipping Lead Time", "mean")
    )
    .reset_index()
)


col1, col2 = st.columns(2)


with col1:

    st.subheader("Average Lead Time by Factory")

    st.bar_chart(
        factory_summary.set_index("Factory")[
            "Average_Lead_Time"
        ]
    )


with col2:

    st.subheader("Factory Shipment Contribution")

    factory_contribution = (
        filtered_df
        .groupby("Factory")
        .size()
        .reset_index(name="Shipments")
    )

    st.bar_chart(
        factory_contribution.set_index("Factory")[
            "Shipments"
        ]
    )


# ============================================================
# PRODUCT ANALYSIS
# ============================================================

st.markdown("---")
st.header("🍫 Product Shipping Performance")


product_summary = (
    filtered_df
    .groupby("Product Name")
    .agg(
        Total_Shipments=("Product Name", "size"),
        Average_Lead_Time=("Shipping Lead Time", "mean")
    )
    .reset_index()
    .sort_values(
        "Total_Shipments",
        ascending=False
    )
)


col1, col2 = st.columns(2)


with col1:

    st.subheader("Shipments by Product")

    st.bar_chart(
        product_summary
        .set_index("Product Name")[
            "Total_Shipments"
        ]
    )


with col2:

    st.subheader("Average Lead Time by Product")

    st.bar_chart(
        product_summary
        .set_index("Product Name")[
            "Average_Lead_Time"
        ]
    )


# ============================================================
# ROUTE PERFORMANCE
# ============================================================

st.markdown("---")
st.header("🛣️ Route Performance")


route_summary = (
    filtered_df
    .groupby("Route")
    .agg(
        Total_Shipments=("Route", "size"),
        Average_Lead_Time=("Shipping Lead Time", "mean"),
        Median_Lead_Time=("Shipping Lead Time", "median"),
        Lead_Time_Std=("Shipping Lead Time", "std")
    )
    .reset_index()
)


route_summary["Lead_Time_Std"] = (
    route_summary["Lead_Time_Std"].fillna(0)
)


route_summary = route_summary.sort_values(
    "Average_Lead_Time",
    ascending=False
)


st.dataframe(
    route_summary,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# FILTERED DATA
# ============================================================

st.markdown("---")
st.header("📋 Filtered Shipment Data")


st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# DOWNLOAD BUTTON
# ============================================================

csv_data = filtered_df.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    label="⬇️ Download Filtered Data",
    data=csv_data,
    file_name="Nassau_Candy_Filtered_Data.csv",
    mime="text/csv"
)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Nassau Candy Distributor | "
    "Factory-to-Customer Shipping Route Efficiency Analysis"
)
