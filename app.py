import streamlit as st

st.set_page_config(
    page_title="NEARBUY",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ NEARBUY")
st.subheader("Your Neighbourhood, Your Marketplace")

st.write(
    "Discover products available at shops near you."
)

menu = st.sidebar.selectbox(
    "Choose your dashboard",
    ["Home", "Customer", "Shopkeeper", "About"]
)

if menu == "Home":
    st.header("Welcome to NEARBUY!")
    st.write("Find what you need, right around the corner.")

elif menu == "Customer":
    st.header("Find Products")
    product = st.text_input("Enter product name")

    if st.button("Search"):
        st.info(f"Searching for {product}...")

elif menu == "Shopkeeper":
    st.header("Shopkeeper Dashboard")

    shop = st.text_input("Shop Name")
    product = st.text_input("Product Name")
    price = st.number_input("Product Price (₹)", min_value=0.0)
    quantity = st.number_input("Available Quantity", min_value=0)

    if st.button("Add Product"):
        st.success("Product added successfully!")

elif menu == "About":
    st.header("About NEARBUY")
    st.write(
        "NEARBUY connects local customers "
        "with nearby shopkeepers."
    )
