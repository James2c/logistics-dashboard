import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_BASE_URL = "http://127.0.0.1:8000"

st.title("📦 Logistics & Procurement Dashboard")


# -----------------------------
# 1. API CALLS
# -----------------------------
vendors_response = requests.get(f"{API_BASE_URL}/vendors")
po_response = requests.get(f"{API_BASE_URL}/purchase-orders")
inventory_response = requests.get(f"{API_BASE_URL}/inventory")


tab1, tab2, tab3 = st.tabs(["Overview", "Procurement", "Inventory"])

with tab1:

    st.header("Overview")

    # -------------------------
    # KPIs
    # -------------------------
    vendor_count = len(vendors_response.json()) if vendors_response.status_code == 200 else 0
    po_count = len(po_response.json()) if po_response.status_code == 200 else 0
    inventory_data = inventory_response.json() if inventory_response.status_code == 200 else []

    low_stock_items = [
        i for i in inventory_data
        if i["stock_level"] <= i["reorder_point"]
    ]

    col1, col2, col3 = st.columns(3)

    col1.metric("Vendors", vendor_count)
    col2.metric("Purchase Orders", po_count)
    col3.metric("Low Stock Items", len(low_stock_items))


    # -------------------------
    # LOW STOCK ALERT PANEL
    # -------------------------
    st.subheader("🚨 Low Stock Alerts")

    if low_stock_items:
        for item in low_stock_items:
            st.error(
                f"{item['item_name']} | Stock: {item['stock_level']} | Reorder Point: {item['reorder_point']}"
            )
    else:
        st.success("No low stock alerts 🎉")



with tab2:

    st.header("Procurement Analytics")

    po_data = po_response.json() if po_response.status_code == 200 else []
    po_df = pd.DataFrame(po_data)

    if not po_df.empty:

        # -------------------------
        # FILTER: STATUS
        # -------------------------
        status_filter = st.selectbox(
            "Filter by Status",
            ["All"] + list(po_df["status"].unique())
        )

        if status_filter != "All":
            po_df = po_df[po_df["status"] == status_filter]


        # -------------------------
        # CHART: PO STATUS
        # -------------------------
        st.subheader("Purchase Orders by Status")

        fig = px.bar(
            po_df,
            x="status",
            color="status"
        )

        st.plotly_chart(fig, use_container_width=True)


        # -------------------------
        # TABLE
        # -------------------------
        st.subheader("All Purchase Orders")

        st.dataframe(po_df, use_container_width=True)



with tab3:

    st.header("Inventory Intelligence")

    inv_data = inventory_response.json() if inventory_response.status_code == 200 else []
    inv_df = pd.DataFrame(inv_data)

    if not inv_df.empty:

        # -------------------------
        # STOCK VS REORDER
        # -------------------------
        st.subheader("Stock vs Reorder Point")

        fig1 = px.bar(
            inv_df,
            x="item_name",
            y=["stock_level", "reorder_point"],
            barmode="group"
        )

        st.plotly_chart(fig1, use_container_width=True)


        # -------------------------
        # INVENTORY VALUE
        # -------------------------
        inv_df["total_value"] = inv_df["stock_level"] * inv_df["unit_cost"]

        st.subheader("Inventory Value")

        fig2 = px.bar(
            inv_df,
            x="item_name",
            y="total_value"
        )

        st.plotly_chart(fig2, use_container_width=True)


        # -------------------------
        # TABLE
        # -------------------------
        st.subheader("Inventory Table")

        st.dataframe(inv_df, use_container_width=True)

