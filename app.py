import streamlit as st
import plotly.express as px
from data_loader import load_gdp_data

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="UK GDP Dashboard",
    layout="wide"
)

# --------------------------------------------------
# Title & source
# --------------------------------------------------
st.title("📊 UK GDP Quarterly Growth Dashboard")
st.caption("Source: Office for National Statistics (ONS)")

# --------------------------------------------------
# Load data
# --------------------------------------------------
df = load_gdp_data("series-040226.csv")

# --------------------------------------------------
# Time range slider
# --------------------------------------------------
st.subheader("📅 Select Time Period")

min_date = df["Date"].min().to_pydatetime()
max_date = df["Date"].max().to_pydatetime()

date_range = st.slider(
    "Time range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)
)

# Filter data based on slider
filtered_df = df[
    (df["Date"] >= date_range[0]) &
    (df["Date"] <= date_range[1])
].copy()

# --------------------------------------------------
# Rolling average (4-quarter)
# --------------------------------------------------
filtered_df["Rolling_4Q"] = (
    filtered_df["GDP_Growth"]
    .rolling(window=4)
    .mean()
)

# --------------------------------------------------
# Recession detection
# Definition: ≥2 consecutive quarters of negative growth
# --------------------------------------------------
filtered_df["Negative"] = filtered_df["GDP_Growth"] < 0
filtered_df["Recession_Group"] = (
    filtered_df["Negative"] != filtered_df["Negative"].shift()
).cumsum()

recessions = (
    filtered_df[filtered_df["Negative"]]
    .groupby("Recession_Group")
    .filter(lambda x: len(x) >= 2)
)

# --------------------------------------------------
# KPI Metrics
# --------------------------------------------------
latest = filtered_df.iloc[-1]["GDP_Growth"]
average = filtered_df["GDP_Growth"].mean()
volatility = filtered_df["GDP_Growth"].std()

col1, col2, col3 = st.columns(3)

col1.metric("Latest Quarter (%)", f"{latest:.2f}")
col2.metric("Average Growth (%)", f"{average:.2f}")
col3.metric("Volatility (Std Dev)", f"{volatility:.2f}")

# --------------------------------------------------
# Line chart
# --------------------------------------------------
fig = px.line(
    filtered_df,
    x="Date",
    y="GDP_Growth",
    markers=True,
    title="Quarter-on-Quarter GDP Growth (%)"
)

# Rolling average line
fig.add_scatter(
    x=filtered_df["Date"],
    y=filtered_df["Rolling_4Q"],
    mode="lines",
    name="4-Quarter Rolling Average",
    line=dict(width=3)
)

# Zero-growth reference
fig.add_hline(
    y=0,
    line_dash="dash",
    annotation_text="Zero growth"
)

# Recession shading
for _, group in recessions.groupby("Recession_Group"):
    fig.add_vrect(
        x0=group["Date"].min(),
        x1=group["Date"].max(),
        fillcolor="red",
        opacity=0.15,
        layer="below",
        line_width=0
    )

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="GDP Growth (%)",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Automated Insights
# --------------------------------------------------
st.subheader("🧠 Automated Insights")

num_recessions = recessions["Recession_Group"].nunique()

worst_quarter = filtered_df.loc[
    filtered_df["GDP_Growth"].idxmin()
]

latest_trend = filtered_df["Rolling_4Q"].iloc[-1]

st.markdown(f"""
- **{num_recessions} recession periods** detected (≥2 consecutive quarters of contraction).
- The worst quarter was **{worst_quarter['Quarter']}**, with GDP growth of **{worst_quarter['GDP_Growth']:.1f}%**.
- The latest 4-quarter rolling average is **{latest_trend:.2f}%**, indicating the current economic trend.
""")
