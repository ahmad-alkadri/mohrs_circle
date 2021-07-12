# streamlit_app_bokeh.py
"""
A streamlit app to draw a Mohr's Circle based on user input
using the Bokeh plotting library
"""

#%% Import packages
import numpy as np
import streamlit as st
from bokeh.plotting import figure
from user_funcs import mohr_c, c_array, X_Y

#%% Main Code
# Make the title
st.title("Mohr's Circle App")

# Make the sidebar with the inputs
stress_x = st.sidebar.number_input("stress in x", value=2.0, step=0.5)
stress_y = st.sidebar.number_input("stress in y", value=5.0, step=0.5)
shear = st.sidebar.number_input("shear xy", value=4.0, step=0.5)

# find center and radius
C, R = mohr_c(stress_x, stress_y, shear)

# build arrays plot circle
circle_x, circle_y = c_array(C, R)

# build arrays to plot line through the circle
X, Y = X_Y(stress_x, stress_y, shear)

st.sidebar.markdown(f"max stress = {round(C+R,2)}")
st.sidebar.markdown(f"min stress = {round(C-R,2)}")
st.sidebar.markdown(f"max shear = {round(R,2)}")

#%% Make the main page
# Make the plot
p = figure(
    title="Mohr's Circle",
    x_axis_label="stress",
    y_axis_label="shear",
    match_aspect=True,
    sizing_mode='stretch_both',
    tools="pan,reset,save,wheel_zoom",
)

p.line(circle_x, circle_y, color="#1f77b4", line_width=3, line_alpha=0.6)
p.line(X, Y, color="#ff7f0e", line_width=3, line_alpha=0.6)

p.xaxis.fixed_location = 0
p.yaxis.fixed_location = 0

st.bokeh_chart(p)
