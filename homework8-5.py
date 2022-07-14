"""
Project : Homework 8-5
Author : Hyung-Jun Ahn
Date of last update: May 3, 2022 
Update list:
    ‐ v1.0 : May. 3, 2022
       pandas를 이용한 excel 입출력
"""
import pandas as pd
df= pd.read_excel("student_scores.xlsx", index_col=0) #0번째 열을 인덱스로
print(df)
avgs_per_student= df.mean(1) #행(학생)의 평균 구하기
df.loc[:,'Avg'] = avgs_per_student #열 추가하기

avgs_per_class= df.mean() #열(과목)의 평균 구하기
print("\navgs_per_class")
print(avgs_per_class)
print("\ndf_sorted_with_avg =")
sorted_df=df.sort_values(by='Avg', ascending=False) #Avg기준으로 내림차순 정렬

sorted_df.loc[len(sorted_df)] = avgs_per_class #w정렬된 파일에 행 추가하기
sorted_df.at[len(sorted_df)-1, 'st_name'] = 'Total_Avg'
print(sorted_df)
print("Writing df to excel file")
with pd.ExcelWriter("student_scores.xlsx") as excel_writer:
    sorted_df.to_excel(excel_writer, sheet_name='Student Records')