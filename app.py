import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib  # [핵심] 이걸 import하면 한글 설정 코드 10줄을 안 써도 됩니다!

# [삭제됨] platform 임포트 및 복잡한 OS별 폰트 설정 코드 제거
# [삭제됨] 마이너스 깨짐 방지 코드도 koreanize_matplotlib가 알아서 해줍니다.

st.title('국세청 근로소득 데이터 분석')

# 데이터 불러오기
file_path = 'data/국세청_근로소득.csv'

try:
    # 한글 엑셀 파일 읽기 위해 encoding='cp949' 유지
    df = pd.read_csv(file_path, encoding='cp949')
    st.success('데이터를 성공적으로 로드했습니다!')
    
    # 데이터 미리 보기
    st.subheader('데이터 미리 보기')
    st.dataframe(df.head()) 
    
    # 데이터 분석 그래프 그리기
    st.subheader('근로소득 분포 그래프')
    
    # 분석할 열 선택
    column_names = df.columns.tolist()
    
    # 사용자 선택
    selected_column = st.selectbox('분석할 열을 선택하세요', column_names)
    
    if selected_column:
        # 그래프 그리기
        fig, ax = plt.subplots(figsize=(10, 5)) 
        
        # 데이터 시각화 (NaN 제거)
        sns.histplot(df[selected_column].dropna(), kde=True, ax=ax, color='#87CEFA')
        
        ax.set_title(f'{selected_column} 분포 그래프')
        ax.set_xlabel(selected_column) 
        ax.set_ylabel('빈도수') 
        
        # 스트림릿 웹 화면에 그래프 표시
        st.pyplot(fig) 

except FileNotFoundError:
    st.error(f'파일을 찾을 수 없습니다. 다음 경로를 확인해주세요: {file_path}')
    st.warning('TIP: app.py와 같은 위치에 data 폴더가 있고, 그 안에 파일이 있는지 확인하세요.')
except ValueError:
    st.error("선택한 열은 그래프로 그릴 수 없는 문자열 데이터일 가능성이 큽니다. 숫자 데이터(급여 등)를 선택해주세요.")
except Exception as e:
    st.error(f'오류가 발생했습니다: {e}')