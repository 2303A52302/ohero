import streamlit as st
import math

# Function to calculate electrical power parameters
def Elec_Power(V, I, PF):
    # Convert power factor to angle in radians
    theta = math.acos(PF)  
    
    # Calculate Active Power (P)
    P = V * I * math.cos(theta)
    
    # Calculate Reactive Power (Q)
    Q = V * I * math.sin(theta)
    
    # Calculate Apparent Power (S)
    S = V * I
    
    return P, Q, S

# Streamlit Web Application
st.title("02341A0259-PS2: Electrical Power Calculator")

st.write("This application calculates Active Power (P), Reactive Power (Q), and Apparent Power (S) based on voltage, current, and power factor.")

# Input Fields
voltage = st.number_input("Enter Voltage (V) in Volts:", min_value=0.0, format="%.2f")
current = st.number_input("Enter Current (I) in Amperes:", min_value=0.0, format="%.2f")
power_factor = st.slider("Select Power Factor (PF):", min_value=0.0, max_value=1.0, step=0.01)

# Compute Button
if st.button("Compute"):
    # Validate inputs
    if voltage <= 0 or current <= 0:
        st.error("Please enter valid Voltage and Current values greater than 0.")
    elif power_factor < 0 or power_factor > 1:
        st.error("Power Factor must be between 0 and 1.")
    else:
        # Calculate values
        P, Q, S = Elec_Power(voltage, current, power_factor)
        
        # Display results
        st.write(f"**Active Power (P):** {P:.2f} Watts")
        st.write(f"**Reactive Power (Q):** {Q:.2f} Vars")
        st.write(f"**Apparent Power (S):** {S:.2f} Volt-Amperes")
