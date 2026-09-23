
import pandas as pd
from pathlib import Path
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="부산항 노선별 항만물류지표 분석 대시보드",
    page_icon='📊',
    layout="wide",
)


st.title('북항/신항 환적 효율성 KPI 대시보드')
st.caption('data:부산항만공사_외내항컨테이너통합집계정보, 2024년')


## KPI card
st.subheader('핵심지표')
# st.caption('필터와는 무관합니다')

col1,col2,col3,col4, = st.columns(4)

with col1 :
    st.metric(
        '환적 TEU Factor (신항)',
        value=f'aa',
        border=True,
        height=250,
    )
with col2 :
    st.metric(
        '신/북항 환적 TEU Factor 격차',
        # value=f'{kpi_teu_factor_gap:.2f}%',
        value=f'aa',
        border=True,
        height=250,
    )
with col3 :
    st.metric(
        '환적 공컨비율 격차',
#         value=f'{kpi_empty_gap:.2f}%p',
        value=f'aa',
        border=True,
        height=250,
        delta='',
    )
with col4 :
    st.metric(
        '물동량-TEU Factor 상관계수',
#         value=f'신항 {kpi_corr_sinhang:.2f} / 북항 {kpi_corr_bukhang:.2f}',
        value=f'aa',
        border=True,
        height=250,
    )


with st.sidebar :
    st.header('검색조건')

    st.subheader('도착항별')

    select_dest = st.selectbox(
        '도착지명',
        ['전체','가','나','다',]
    )

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.subheader('월별')

    select_mon = st.slider(
        '월 범위',
        min_value=1,
        max_value=12,
        value=(1,12)
    )
