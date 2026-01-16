import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform # 운영체제 확인을 위해 추가

# [추가] 한글 폰트 깨짐 방지 설정
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    plt.rc('font', family='AppleGothic')
else: # Linux (구글 코랩 등)
    plt.rc('font', family='NanumGothic')

# [추가] 마이너스 기호가 깨지는 것 방지
plt.rcParams['axes.unicode_minus'] = False

st.title('국세청 근로소득 데이터 분석')

# 데이터 불러오기
file_path = 'data/국세청_근로소득.csv'

try:
    # 한글 엑셀 파일 읽기 위해 encoding='cp949' 유지
    df = pd.read_csv(file_path, encoding='cp949')
    st.success('데이터가 성공적으로 로드했습니다!')
    
    # 데이터 미리 보기
    st.subheader('데이터 미리 보기')
    st.dataframe(df.head()) 
    
    # 데이터 분석 그래프 그리기
    st.subheader('근로소득 분포 그래프')
    
    # 분석할 열 선택
    column_names = df.columns.tolist()
    
    # 숫자형 데이터만 선택해야 오류가 적으므로, 사용자가 선택할 때 주의 필요
    selected_column = st.selectbox('분석할 열을 선택하세요', column_names)
    
    if selected_column:
        # 그래프 그리기(seaborn 사용)
        fig, ax = plt.subplots(figsize=(10,5)) 
        
        # 데이터에 NaN(빈값)이 있으면 오류가 날 수 있어 dropna()로 제거 후 그리기
        # 숫자형 데이터가 아닌 경우 오류가 날 수 있음 (try-except로 잡힘)
        sns.histplot(df[selected_column].dropna(), kde=True, ax=ax, color='#87CEFA')
        
        ax.set_title(f'{selected_column} 분포 그래프')
        ax.set_xlabel(selected_column) 
        ax.set_ylabel('빈도수') 
        
        # 스트림릿 웹 화면에 그래프 표시
        st.pyplot(fig) 

except FileNotFoundError:
    st.error(f'파일을 확인해주세요 : {file_path}')
except ValueError:
    st.error("선택한 열은 그래프로 그릴 수 없는 문자열 데이터일 가능성이 큽니다. 숫자 데이터(급여 등)를 선택해주세요.")
except Exception as e:
    st.error(f'오류가 발생했습니다: {e}')