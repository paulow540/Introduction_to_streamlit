import streamlit as st
import time 

st.sidebar.json(st.session_state)

# user = st.text_input("Name", key="Name")


# if "Name" not in st.session_state:
#     st.session_state.Name = user




# if st.button("Click me"):
#     st.write(st.session_state["Name"])


def increment(id):
    st.session_state[f"num{id}"] +=1
    

def decrement(id):
    st.session_state[f"num{id}"] -=1
    

number = 0


@st.fragment
def count(id):
    with st.container(border=True):
        if f"num{id}" not in st.session_state:
            st.session_state[f"num{id}"] = number
        
        st.write(st.session_state[f"num{id}"])        
        st.button("Increment" ,
                    on_click=increment,
                    key=f"increment{id}", 
                    args = (id,))
            

        st.button("decrement", 
                    on_click=decrement,
                    key=f"decrement{id}",
                    args=(id,)
                    )
            

count("One")

count("Two")

