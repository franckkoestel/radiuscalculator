import streamlit as st

# Helper function to convert fractional inputs
def fraction_to_decimal(fraction):
    fractions = {
        '⅛"': 1/8, '¼"': 1/4, '⅜"': 3/8, '½"': 1/2,
        '⅝"': 5/8, '¾"': 3/4, '⅞"': 7/8, '0"': 0
    }
    return fractions[fraction]

# Helper function to round to the nearest 1/8 inch
def round_to_nearest_eighth(value):
    # Round to the nearest 1/8
    rounded_value = round(value * 8) / 8
    whole_inches = int(rounded_value)
    fraction_part = rounded_value - whole_inches
    
    # Determine the nearest fraction
    fractions = {
        0: '',
        1/8: '⅛', 1/4: '¼', 3/8: '⅜', 1/2: '½', 
        5/8: '⅝', 3/4: '¾', 7/8: '⅞'
    }
    fraction_display = fractions.get(fraction_part, '')
    
    if whole_inches == 0 and fraction_display != '':
        return f"{fraction_display} inches"
    elif fraction_display:
        return f"{whole_inches} {fraction_display} inches"
    else:
        return f"{whole_inches} inches"

# Input section
st.title("Arch Cornice Radius Calculator")

# WINDOW WIDTH (side by side)
st.subheader("Window Width")
col1, col2 = st.columns(2)
with col1:
    window_width_whole = st.number_input("Whole inches", min_value=1, step=1, key="window_width_whole")
with col2:
    window_width_fraction = st.selectbox("Fraction", ['0"', '⅛"', '¼"', '⅜"', '½"', '⅝"', '¾"', '⅞"'], key="window_width_fraction")
window_width = window_width_whole + fraction_to_decimal(window_width_fraction)

# WINDOW HEIGHT (side by side)
st.subheader("Window Height")
col3, col4 = st.columns(2)
with col3:
    window_height_whole = st.number_input("Whole inches", min_value=1, step=1, key="window_height_whole")
with col4:
    window_height_fraction = st.selectbox("Fraction", ['0"', '⅛"', '¼"', '⅜"', '½"', '⅝"', '¾"', '⅞"'], key="window_height_fraction")
window_height = window_height_whole + fraction_to_decimal(window_height_fraction)

# MOUNT type
st.subheader("Mount Type")
mount = st.selectbox("Select the Mount type:", ["Inside Mount", "Outside Mount"])

# Calculation and Output section
calculate = st.button("CALCULATE")

# Ensure the calculation runs only when the button is clicked
if calculate:
    # Adjusting Arch Width and Arch Height based on mount type
    if mount == "Inside Mount":
        arch_width = window_width - 0.25  # Deduct ¼” from width
        arch_height = window_height - 1/8  # Deduct ⅛” from height
    else:
        arch_width = window_width
        arch_height = window_height
    
    # Calculate Arch Radius
    arch_radius = ((arch_width / 2) ** 2 + arch_height ** 2) / (2 * arch_height)
    
    # Displaying the results rounded to the nearest 1/8"
    st.subheader("Results")
    st.write(f"Final Width: {round_to_nearest_eighth(arch_width)}")
    st.write(f"Final Height: {round_to_nearest_eighth(arch_height)}")
    st.write(f"Arch Radius: {round_to_nearest_eighth(arch_radius)}")
