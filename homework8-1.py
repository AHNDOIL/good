"""
Project : Homework 8-1
Author : Hyung-Jun Ahn
Date of last update: April 30, 2022 
Update list:
    ‐ v1.0 : April. 30, 2022
       텍스트 파일을 이용한 국가 기본 정보 출력하기
"""
f1= open("demography.txt", 'r') #파일 읽기 모드로 open
list_country= [] 
list_capital= []
list_people= []
list_size= []
for line in f1.readlines():
    country, capital, people, size= line.split() #split으로 나누기
    list_country.append(country) #각 리스트에 추가
    list_capital.append(capital)
    list_people.append(int(people))
    list_size.append(int(size))
print("Input list of countries  :")
print("==========================================================")
print("{:2}: {:<15} {:<15} {:10} {}".format("No", "Name", "Capital", "Num_people", "Area[km2]"))
print("----------------------------------------------------------")
country_information= list(zip(list_country, list_capital, list_people, list_size)) #zip함수로 리스트의 같은 인덱스 원소들을 새로운 리스트에 묶음
for i in range(len(country_information)):
    print("{:2}: {:<15} {:<15} {:10} {:10}".format(i, country_information[i][0], country_information[i][1], country_information[i][2], country_information[i][3]))
#문자열은 왼쪽 정렬, 숫자는 오른쪽 정렬 
print("")
country_information.sort(key= lambda x:x[2], reverse=True) #lambda식을 이용해 2번째 인덱스 기준으로 내림차순 정렬
print("List of countries sorted by demography(number of people)  :")
print("==========================================================")
print("{:2}: {:<15} {:<15} {:10} {}".format("No", "Name", "Capital", "Num_people", "Area[km2]"))
print("----------------------------------------------------------")
for i in range(len(country_information)):
    print("{:2}: {:<15} {:<15} {:10} {:10}".format(i, country_information[i][0], country_information[i][1], country_information[i][2], country_information[i][3]))