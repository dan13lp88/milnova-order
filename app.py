import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Online Ordering Demo",
    page_icon="🛍️",
    layout="centered"
)

st.title("Sample Business Online Ordering")
st.caption("A simple demo for online pickup and delivery orders.")

products = [
    {"name": "Classic Sandwich", "price": 9.99},
    {"name": "Chicken Wrap", "price": 10.99},
    {"name": "Garden Salad", "price": 7.99},
    {"name": "Fresh Lemonade", "price": 3.49},
]

if "cart" not in st.session_state:
    st.session_state.cart = []

st.header("Menu")

for product in products:
    left_column, right_column = st.columns([4, 1])

    with left_column:
        st.write(f"**{product['name']}**")
        st.write(f"${product['price']:.2f}")

    with right_column:
        if st.button("Add", key=product["name"]):
            st.session_state.cart.append(product)
            st.success(f"Added {product['name']}.")

st.divider()
st.header("Your Cart")

if not st.session_state.cart:
    st.info("Your cart is empty.")
else:
    cart_df = pd.DataFrame(st.session_state.cart)
    st.dataframe(cart_df, hide_index=True, use_container_width=True)

    total = sum(item["price"] for item in st.session_state.cart)
    st.subheader(f"Total: ${total:.2f}")

    if st.button("Clear Cart"):
        st.session_state.cart = []
        st.rerun()

st.divider()
st.header("Checkout")

with st.form("checkout_form"):
    customer_name = st.text_input("Name")
    phone = st.text_input("Phone number")
    fulfillment = st.radio("Order type", ["Pickup", "Delivery"])
    notes = st.text_area("Order notes")
    submit_order = st.form_submit_button("Place Demo Order")

if submit_order:
    if not st.session_state.cart:
        st.warning("Please add at least one item to your cart.")
    elif not customer_name.strip() or not phone.strip():
        st.warning("Please enter your name and phone number.")
    else:
        st.success("Thank you. Your demo order has been received.")
        st.write(f"**Order for:** {customer_name}")
        st.write(f"**Fulfillment:** {fulfillment}")
        st.write(f"**Total:** ${total:.2f}")
        st.session_state.cart = []
