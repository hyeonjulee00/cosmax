import pathlib

import streamlit as st

# ── 기본 페이지 설정 ─────────────────────────────────────────────
st.set_page_config(
    page_title="차세대 소재 기술 최신 동향 검색",
    page_icon="🧪",
    layout="wide",
)

# Streamlit 기본 여백/헤더를 최소화해서 원본 HTML 디자인이 그대로 보이게 함
st.markdown(
    """
    <style>
        .block-container {padding-top: 0rem; padding-bottom: 0rem; max-width: 100%;}
        header {visibility: hidden; height: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

# ── 원본 index.html 로드 및 렌더링 ─────────────────────────────
# 키워드 추가/삭제, 정렬 토글 등 모든 로직이 JS 안에 이미 구현되어 있어
# Streamlit 위젯으로 재구현하지 않고 그대로 iframe에 임베드하는 것이 가장 안전합니다.
HTML_PATH = pathlib.Path(__file__).parent / "index.html"
st.iframe(HTML_PATH, height=1400, width="stretch")
