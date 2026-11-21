import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="NEARBUY",
    page_icon="🛍️",
    layout="wide"
)

# Temporary inventory storage
if "products" not in st.session_state:
    st.session_state.products = []

st.markdown("""
<style>
.main {
    background-color: #f7faf7;
}
h1 {
    color: #176b45;
}
</style>
""", unsafe_allow_html=True)

st.title("🛍️ NEARBUY")
st.caption("Your Neighbourhood, Your Marketplace")

menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Customer", "Shopkeeper", "About"]
)

# HOME
if menu == "Home":

    st.title("Welcome to NEARBUY!")
    st.subheader("Find products available near you.")

    st.info("Discover local shops and compare product prices.")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Listed Products", len(st.session_state.products))

    with col2:
        st.metric(
            "Available Products",
            sum(p["Quantity"] > 0 for p in st.session_state.products)
        )

# SHOPKEEPER
elif menu == "Shopkeeper":

    st.header("🏪 Shopkeeper Dashboard")

    st.subheader("Add Your Product")

    with st.form("product_form"):

        shop = st.text_input("Shop Name")
        address = st.text_input("Shop Address")

        product = st.text_input("Product Name")

        category = st.selectbox(
            "Category",
            ["Grocery", "Electronics", "Stationery",
             "Clothing", "Personal Care", "Other"]
        )

        col1, col2 = st.columns(2)

        with col1:
            price = st.number_input(
                "Price (₹)",
                min_value=0.0,
                step=1.0
            )

        with col2:
            quantity = st.number_input(
                "Available Quantity",
                min_value=0,
                step=1
            )

        submitted = st.form_submit_button("Add Product")

        if submitted:

            if shop and product and address and price > 0:

                st.session_state.products.append({
                    "Shop": shop,
                    "Address": address,
                    "Product": product,
                    "Category": category,
                    "Price": price,
                    "Quantity": quantity
                })

                st.success("Product added successfully!")

            else:
                st.error("Please fill in all required fields.")

    st.divider()

    st.subheader("📦 Your Inventory")

    if st.session_state.products:

        df = pd.DataFrame(st.session_state.products)

        st.dataframe(df, use_container_width=True)

        if st.button("Clear Inventory"):
            st.session_state.products = []
            st.rerun()

    else:
        st.info("No products listed yet.")

# CUSTOMER
elif menu == "Customer":

    st.header("🔍 Find Products Near You")

    search = st.text_input("Search for a product")

    if search:

        results = [
            p for p in st.session_state.products
            if search.lower() in p["Product"].lower()
            and p["Quantity"] > 0
        ]

        if results:

            results = sorted(results, key=lambda x: x["Price"])

            st.subheader("Available Shops")

            for p in results:

                with st.container(border=True):

                    st.subheader(p["Shop"])
                    st.write("Product:", p["Product"])
                    st.write("Category:", p["Category"])
                    st.write("Price: ₹", p["Price"])
                    st.write("Quantity:", p["Quantity"])
                    st.write("Address:", p["Address"])

        else:
            st.warning("No matching products found.")

# ABOUT
elif menu == "About":

    st.header("About NEARBUY")

    st.write("""
    NEARBUY is a hyperlocal product discovery platform.

    It connects customers with nearby shopkeepers
    and helps them find products, compare prices
    and check availability.
    """)
