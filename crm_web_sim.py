# -*- coding: utf-8 -*-
__author__ = "Y. WU"
__copyright__ = "Copyright 2022, PKUTECH"
__credits__ = ["Y. WU"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Y. WU"
__email__ = "wuyilang@pkutech.co.jp"
__status__ = "Dev-Ops"


import streamlit as st

# import datetime
import numpy as np

# import plotly.figure_factory as ff


st.set_page_config(layout="wide")

# Hid logo
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Hide index and header in Table
st.markdown(
    # Inject CSS with Markdown
    """
    <style>
    thead tr th:first-child {display:none}
    tbody th {display:none}
    </style>
    """,
    unsafe_allow_html=True,
)


(tab_sim_result_report, tab_sim_result_cashflow, tab_sim_result_ar) = st.tabs(
    [
        "Diagnosis",
        "Cash Flow Simulation",
        "AR",
    ],
)

with st.container():
    with tab_sim_result_report:
        (
            col_sim_risk_macro,
            col_sim_risk_micro,
        ) = st.columns(2)

    with tab_sim_result_cashflow:
        with st.expander("Cash Flow Simulation", expanded=True):
            pass
            # # Add histogram data
            # x1 = np.random.randn(200) - 2
            # x2 = np.random.randn(200)
            # x3 = np.random.randn(200) + 2

            # # Group data together
            # hist_data = [x1, x2, x3]

            # group_labels = ["Group 1", "Group 2", "Group 3"]

            # # Create distplot with custom bin_size
            # fig = ff.create_distplot(
            #     hist_data,
            #     group_labels,
            #     bin_size=[0.1, 0.25, 0.5],
            # )

            # # Plot!
            # st.plotly_chart(
            #     fig,
            #     use_container_width=True,
            # )

    with tab_sim_result_ar:
        with st.expander("AR", expanded=True):
            pass
            # st.components.v1.iframe(
            #     "https://localhost:40443/gui/crm_avatar/",
            #     width=None,
            #     height=800,
            #     scrolling=False,
            # )

with st.sidebar:
    st.sidebar.header("Life Simulation")
