#------------------------------------------------------
# Series/DataFrmae 에서 사용되는 사용자 정의 함수들
#------------------------------------------------------
# 함수기능 : DataFrame의 기본정보와 속성 확인 기능
# 함수이름 : checkDataFrame
# 매개변수 : DataFrame 인스턴스 변수명, DataFrame의 인스턴스 이름
# 리턴값/반환값: 없음.
#------------------------------------------------------ > 함수의 대한 설명을 독스트린이라 부름.
def checkDataFrame(object, name):
    print(f'\n[{name}]')
    print()
    object.info()
    print()
    print(f'index : {object.index}')
    print()
    print(f'columns : {object.columns}')
    print()
    print(f'ndim : {object.ndim}')

def kor_font(font_path): # font_path에다가 파일경로 넣기.
    from matplotlib import font_manager as fm
    from matplotlib import rc

    #폰트 패밀리 이름 가져오기
    font_name=fm.FontProperties(fname=font_path).get_name()

    # 새로운 폰트 패밀리 이름 지정
    rc('font', family=font_name)

# 그래프 그리기.
import pandas as pd
import matplotlib.pyplot as plt
import df_dfutil as util
def drawlinegrape(dataframe, title, columns, labels, xlabel, ylabel): # 타이틀, 열이름, 라벨로 사용할 열이름, 엑스라벨쓸 이름, 와이라벨쓸이름
    for col in columns:
        plt.plot(dataframe.loc[col], label=f'{col}')
    
    plt.title(f'---[{title}]---' )
    plt.ylabel(xlabel)
    plt.xlabel(ylabel)
    plt.legend(labels)
    plt.show()