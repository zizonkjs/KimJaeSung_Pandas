#----------------------------------------------------------------------
# 클래스
# - 객체지향언어(OOP)에서 데이터를 정의하는 자료형 프리미티브타입(int,str,float)
# - 데이터를 정의할 수 있는 데이터가 가진 속성과 기능을 명시
# - 구성요소 : 속성/attribute/field + 기능/method
#----------------------------------------------------------------------
# 클래스 정의: 햄버거를 나타내는 Class
# 클래스 이름: 버거
# 클래스 속성: 반, 패티, 야채, 종류
# 클래스 기능: 햄버거 설명 기능.
class Bugger:
    # 객체 생성 코드를 작성해야지 hip에 메모리가 할당됨
    # 여기선 클래스 속성 만들 수 있음.
    def __init__(self, bread, patty, veg, kind): # 힙 영역에 객체생성시 속성 값을 저장하는 역할.
        # 인스턴스속성
        self.bread=bread
        self.patty=patty
        self.veg=veg # 매개변수 저장해주기.
        self.kind=kind

    # 클래스의 기능, 메서드
    def printinfo(self): # 반드시 self들어가야함, self에는 객체의 주소가 들어감.
        print(f'빵종류 : {self.bread}')
        print(f'패  티 : {self.patty}')
        print(f'야  채 : {self.veg}')
        print(f'브랜드 : {self.kind}')

    # 속성을 변경하거나 읽어오는 메서드 -> getter/setter method (선택사항)
    def get_bread(self):
        return self.bread # 읽어오는 브레드 get
    
    def set_bread(self, bread): # 속성을 변경해주는 set
        self.bread=bread #새로운 브레드를 저장

# 객체 생성
# 불고기 버거 객체생성
bugger1=Bugger('브리오슈','불고기', '양상추 양파 토마토', '롯데리아')

# 치즈버거 객체생성
bugger2=Bugger('참깨빵','순쇠고기패티2장', '치즈양상추 양파 토마토', '맥도날드')


# 버거 정보확인
bugger1.printinfo()

#속성읽는 방법
print( bugger1.bread, bugger1.get_bread()) # (직접읽어오기, 메서드통한 간접접근해서읽어오기) - getter 메서드 사용

#속성변경 방법 setter
bugger1.bread='들깨빵' # 직접접근해서 속성변경
bugger1.set_bread('올리브빵') # 간접접근해서 속성변경
bugger2.printinfo()



