import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm # 폰트 관리자
import os

# [수정] 폰트 설정 (koreanize_matplotlib 제거 후 수동 설정)
def unique_font_path(font_name='NanumGothic'):
    # 리눅스(스트림릿 클라우드) 경로
    font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
    # 윈도우/맥 개발 환경 경로 (혹시 모르니 예비용)
    if not os.path.exists(font_path):
        # 윈도우의 경우 보통 여기에 있음 (환경에 따라 다를 수 있음)
        font_path = 'C:/Windows/Fonts/NanumGothic.ttf' 
    return font_path

# 폰트 적용
font_path = unique_font_path()
if os.path.exists(font_path):
    fe = fm.FontEntry(
        fname=font_path,
        name='NanumGothic'
    )
    fm.fontManager.ttflist.insert(0, fe)
    plt.rc('font', family='NanumGothic')
else:
    st.warning("나눔고딕 폰트를 찾을 수 없습니다. packages.txt를 확인하세요.")

# 마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

st.title('국세청 근로소득 데이터 분석')
# ... (이하 코드는 동일) ...