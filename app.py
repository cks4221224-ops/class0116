import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm # 폰트 관리용
import os

st.title('국세청 근로소득 데이터 분석')

# -----------------------------------------------------------
# [1] 폰트 설정 (가장 확실한 방법: 로컬 파일 직접 지정)
# -----------------------------------------------------------
def setup_custom_font():
    # 현재 파일(app.py)이 있는 위치를 기준으로 폰트 경로 찾기
    current_dir = os.path.dirname(__file__)
    font_path = os.path.join(current_dir, 'fonts', 'NanumGothic.ttf')
    
    # 폰트 파일이 실제로 있는지 확인
    if os.path.exists(font_path):
        # 폰트 매니저에 이 경로의 폰트를 추가
        fm.fontManager.addfont(font_path)
        # 추가된 폰트의 이름을 알아내서 설정
        font_prop = fm.FontProperties(fname=font_path)
        font_name = font_prop.get_name()
        
        plt.rc('font', family=font_name)
        plt.rcParams['axes.unicode_minus'] = False # 마이너스 깨짐 방지
        # st.success(f"폰트가 성공적으로 로드되었습니다: {font_name}") # 테스트용
    else:
        st.error(f"폰트 파일을 찾을 수 없습니다: {font_path}")
        st.warning("fonts 폴더 안에 NanumGothic.ttf 파일이 있는지 확인해주세요.")

# 함수 실행
setup_custom_font()
# -----------------------------------------------------------


# 데이터 불러오기
file_path = 'data/국세청_근로소득.csv'

try:
    df = pd.read_csv(file_path, encoding='cp949')
    st.success('데이터를 성공적으로 로드했습니다!')
    
    st.subheader('데이터 미리 보기')
    st.dataframe(df.head()) 
    
    st.subheader('근로소득 분포 그래프')
    column_names = df.columns.tolist()
    selected_column = st.selectbox('분석할 열을 선택하세요', column_names)
    
    if selected_column:
        fig, ax = plt.subplots(figsize=(10, 5)) 
        
        # 데이터 시각화
        sns.histplot(df[selected_column].dropna(), kde=True, ax=ax, color='#87CEFA')
        
        ax.set_title(f'{selected_column} 분포 그래프')
        ax.set_xlabel(selected_column) 
        ax.set_ylabel('빈도수') 
        
        st.pyplot(fig) 

except FileNotFoundError:
    st.error('파일을 찾을 수 없습니다.')
except Exception as e:
    st.error(f'오류가 발생했습니다: {e}')