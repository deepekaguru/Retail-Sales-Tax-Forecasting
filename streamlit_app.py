import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# Load your data
df = pd.read_csv("Quarterly_Retail_Sales_Tax_Data_by_County_and_City.csv")
df = df[['Quarter Ending', 'County', 'City', 'Computed Tax']].dropna()
df['ds'] = pd.to_datetime(df['Quarter Ending'])
df['y'] = df['Computed Tax']

st.set_page_config(page_title="Retail Tax Forecast", layout="wide")
st.title("📈 Retail Sales Tax Forecast App")

# Sidebar filters
selected_county = st.sidebar.selectbox("Select County", df['County'].unique())
filtered_cities = df[df['County'] == selected_county]['City'].unique()
selected_city = st.sidebar.selectbox("Select City", filtered_cities)

# Forecast horizon with tooltip
# 👇 This goes inside your sidebar
periods = st.sidebar.slider(
    "📆 Forecast Horizon",
    min_value=1,
    max_value=8,
    value=4,
    help="Each quarter represents 3 months. So 4 quarters = 1 year."
)


# Filter dataset
subset = df[(df['County'] == selected_county) & (df['City'] == selected_city)][['ds', 'y']].sort_values('ds')

# Run Prophet if enough data
if subset.shape[0] >= 12:
    model = Prophet(yearly_seasonality=True)
    model.fit(subset)

    future = model.make_future_dataframe(periods=periods, freq='QE')
    forecast = model.predict(future)

    # Plot forecast
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(subset['ds'], subset['y'], label='Historical', color='dodgerblue')
    ax.plot(forecast['ds'], forecast['yhat'], label='Forecast', color='orange')
    ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'],
                    alpha=0.3, color='orange')
    ax.set_title(f"Forecast for {selected_city}, {selected_county}")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Computed Tax")
    ax.legend()
    st.pyplot(fig)

else:
    st.warning("Not enough data for this city.")
