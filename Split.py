import streamlit as st

# st.navigation()
st.title("Srisailam Trip Expense Split")
st.markdown("""
### Rough Expense:
**Food**  
**Breakfast**: ₹1300  
**Lunch cum Dinner**: ₹2400  
**Darshan Ticket**: ₹2400  
**Commute**: *(User Input)*
""")

with st.expander("Major Expenses ₹", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        N_pet = st.number_input("Nikesh Bhai (Petrol) ₹", value=3600)
        Breakfast = st.number_input("Pushpesh Bhai (Breakfast) ₹", value=1300)
        Lunch_Dinner = st.number_input("Nikesh Bhai (Lun + Din) ₹", value=2400)
    with col2:
        s_pet = st.number_input("Sandeep Bhai (Petrol) ₹", value=3000)
        Darshan = st.number_input("Sandeep Bhai (Darshan Ticket) ₹", value=2400)
        B_pet = st.number_input("Biswa ₹", value=1000)

    calc = st.button("Calculate Expense Split", use_container_width=True)
if calc:
    total = N_pet + B_pet + s_pet + Darshan + Breakfast + Lunch_Dinner

    Sandeep = (Breakfast + Lunch_Dinner + Darshan)/4
    Nikesh = (Breakfast + Lunch_Dinner + Darshan)/4
    Pushpesh = (Breakfast + Lunch_Dinner + Darshan)/4
    Biswa = (Breakfast + Lunch_Dinner + Darshan)/4

    Sandeep = Sandeep + s_pet/2
    Pushpesh = Pushpesh + s_pet/2
    Biswa = Biswa + ((N_pet+B_pet)/2)
    Nikesh = Nikesh + ((N_pet+B_pet)/2)
    n_con = N_pet + Lunch_Dinner
    s_con = s_pet + Darshan
    p_con = Breakfast
    b_con = B_pet
    st.expander('Individual Splits', expanded=True)
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Nikesh Bhai", value=Nikesh)
        st.text_input("Pushpesh Bhai", value=Pushpesh)
    with col2:
        st.text_input("Sandeep Bhai", value=Sandeep)
        st.text_input("Biswajit", value=Biswa)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Contributions (Amount Paid)")

        st.markdown(f"**Sandeep contributed:** ₹{s_con}")
        st.markdown(f"**Nikesh contributed:** ₹{n_con}")
        st.markdown(f"**Pushpesh contributed:** ₹{p_con}")
        st.markdown(f"**Biswa contributed:** ₹{b_con}")

    # Optional: Net balance

    with col2:
        st.subheader("Net Settlement (Split - Contribution)")

        if Sandeep - s_con>0:
            st.markdown(f"**Sandeep Bhai needs to pay:** ₹{Sandeep - s_con:.2f}")
        else:
            st.markdown(f"**Sandeep Bhai owes:** ₹{-1*(Sandeep - s_con):.2f}")

        if Nikesh - n_con>0:
            st.markdown(f"**Nikesh Bhai needs to pay:** ₹{Nikesh - n_con:.2f}")
        else:
            st.markdown(f"**Nikesh Bhai owes:** ₹{-1*(Nikesh - n_con):.2f}" )

        if Pushpesh - p_con>0:
            st.markdown(f"**Pushpesh needs to pay:** ₹{(Pushpesh - p_con):.2f}")
        else:
            st.markdown(f"**Pushpesh Bhai owes:** ₹{-1*(Pushpesh - p_con):.2f}")
        if Biswa - b_con>0:
            st.markdown(f"**Biswa needs to pay:** ₹{Biswa - b_con:.2f}")

    st.markdown(f"**Pushpesh Bhai needs to Pay Sandeep Bhai:** {1*(Pushpesh - p_con):.2f}")
    st.markdown(f"**Biswa needs to Pay Nikesh Bhai:** {-1*(Nikesh - n_con):.2f} and Sandeep Bhai:** {(Sandeep - s_con)-(Pushpesh - p_con):.2f}")

if __name__=='__main__':
    pass








