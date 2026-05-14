import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# إعداد الصفحة
# =========================
st.set_page_config(
    page_title="Interactive Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# =========================
# تحميل البيانات
# =========================
df = pd.read_csv("sales_data.csv")
# =========================
# عنوان المشروع
# =========================
st.title("📊 Interactive Sales Dashboard")

st.markdown("Dashboard تفاعلي لتحليل المبيعات والأرباح والكميات")

# =========================
# Sidebar Filter
# =========================
st.sidebar.header("🔍 Filter Data")

country = st.sidebar.selectbox(
    "اختر الدولة",
    options=df["country"].unique()
)

# =========================
# فلترة البيانات
# =========================
filtered_df = df[df["country"] == country]

# =========================
# KPIs
# =========================
total_sales = filtered_df["sales"].sum()
total_profit = filtered_df["profit"].sum()
total_quantity = filtered_df["quantity"].sum()

st.subheader(f"📌 KPIs for {country}")

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"${total_sales}")
col2.metric("📈 Total Profit", f"${total_profit}")
col3.metric("📦 Quantity Sold", total_quantity)

# =========================
# Charts
# =========================
st.subheader("📊 Charts")

chart_col1, chart_col2 = st.columns(2)

# Bar Chart
bar_fig = px.bar(
    filtered_df,
    x="product",
    y="sales",
    color="product",
    title="Sales by Product"
)

chart_col1.plotly_chart(bar_fig, use_container_width=True)

# Pie Chart
pie_fig = px.pie(
    filtered_df,
    names="product",
    values="profit",
    title="Profit Distribution"
)

chart_col2.plotly_chart(pie_fig, use_container_width=True)

# Line Chart
line_fig = px.line(
    filtered_df,
    x="product",
    y="quantity",
    markers=True,
    title="Quantity Sold"
)

st.plotly_chart(line_fig, use_container_width=True)

# =========================
# Data Table
# =========================
st.subheader("📋 Filtered Data")

st.dataframe(filtered_df, use_container_width=True)
if st.button("Show Data"):
    st.write(df)

# =========================
# Footer
# =========================
st.markdown("---")
st.markdown("✅ Built with Streamlit & Plotly")