"""
Project : Homework 8-3
Author : Hyung-Jun Ahn
Date of last update: April 30, 2022 
Update list:
    ‐ v1.0 : April. 30, 2022
       텍스트 파일을 이용한 행렬 출력
"""
class Mtrx:
    def __init__(self, name, n_row, n_col, L_data): 
        self.setName(name)
        self.n_row= n_row #행의 길이
        self.n_col= n_col #열의 길이
        
        self.mtrx=[[] for _ in range(self.n_row)] #행렬 기본 구조 리스트
        index= 0 #행렬 값의 인덱스
        for i in range(0, self.n_row): #2중 for문으로 행렬 구성
            for j in range(0, self.n_col):
                self.mtrx[i].append(L_data[index]) 
                index= index+ 1
           
    def setName(self, name): #변경자
        self.name= name
    def __str__(self): 
        s= "\n"
        s+= self.name+'=' #이름 출력
        s+= '\n'
        for i in range(0, self.n_row): 
#2중 for문으로 출력하는 행렬을 s에 저장
            for j in range(0, self.n_col):
                s+= "{:5.1f}".format(self.mtrx[i][j]) #float형태 소수점 1자리까지 출력
            s+= "\n"
        return s
    def __add__(self, other): # '+' 연산자 오버로딩 
        add_mtrx= [] # '+'연산을 시행한 mtrx
        for i in range(0, self.n_row):
            for j in range(0, self.n_col):
                add_ij= self.mtrx[i][j] + other.mtrx[i][j]
                add_mtrx.append(add_ij)
        return Mtrx("R", self.n_row, self.n_col, add_mtrx) #완성된 add_mtrx를 다시 Mtrx로
    def __sub__(self, other): # '-' 연산자 오버로딩
        sub_mtrx= [] # '-'연산을 시행한 mtrx
        for i in range(0, self.n_row):
            for j in range(0, self.n_col):
                sub_ij= self.mtrx[i][j] - other.mtrx[i][j]
                sub_mtrx.append(sub_ij)
        return Mtrx("R", self.n_row, self.n_col, sub_mtrx)
    def __mul__(self, other): # '*' 연산자 오버로딩
        mul_mtrx= [] # '*'연산을 시행한 mtrx
        for i in range(0, self.n_row):
            for j in range(0, other.n_col):
                mul_ij= 0 #값 초기화
                for k in range(0, self.n_col):
                    mul_ij= mul_ij+ self.mtrx[i][k] * other.mtrx[k][j] #이전 mul값에 더함
                mul_mtrx.append(mul_ij)
        return Mtrx("R", self.n_row, other.n_col, mul_mtrx)

if __name__== "__main__":
       
    f= open("matrix_data.txt", "r") #읽기 모드로 파일 열기
    LA= []
    LB= []
    LC= []
   
    n_row, n_col= map(int,f.readline().split()) #처음 줄 읽은 후 행렬 크기 변수에 저장
    for i in range(n_row): #행의 크기만큼 반복
        LA.append(list(map(float,f.readline().split()))) #float형태로 공백 기준으로 split해서 append
    mA= Mtrx("mA", n_row, n_col, sum(LA,[])) #2차원 리스트를 합쳐서 1차원 리스트로 바꾼 후 Mtrx로 넘겨줌
    print(mA)
    n_row, n_col= map(int,f.readline().split()) #그 다음 줄 읽은 후 행렬 크기 변수에 저장
    for i in range(n_row):
        LB.append(list(map(float,f.readline().split())))
    mB= Mtrx("mB", n_row, n_col, sum(LB,[])) 
    print(mB)
    n_row, n_col= map(int,f.readline().split())
    for i in range(n_row):
        LC.append(list(map(float,f.readline().split())))
    mC= Mtrx("mC", n_row, n_col, sum(LC,[])) 
    print(mC)
    mD= mA+ mB
    mD.setName("mD = mA + mB") 
    print(mD)
    mE= mA- mB
    mE.setName("mE = mA - mB") 
    print(mE)
    mF= mA* mC
    mF.setName("mF = mA * mC")
    print(mF)
