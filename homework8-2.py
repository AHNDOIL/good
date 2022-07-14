"""
Project : Homework 8-2
Author : Hyung-Jun Ahn
Date of last update: April 30, 2022 
Update list:
    ‐ v1.0 : April. 30, 2022
       텍스트 파일을 이용한 학생 정보 입출력
"""
f1= open("student_records.txt", 'r')  #읽기 모드로 파일열기
list_name= []
list_kor= []
list_eng= []
list_math= []
list_sci= []
list_sum= []
list_avg= []
for line in f1.readlines(): #텍스트 파일을 줄로 읽어서 각 리스트에 원소 저장
    name, kor, eng, math, sci= line.split()
    list_name.append(name)
    list_kor.append(int(kor))
    list_eng.append(int(eng))
    list_math.append(int(math))
    list_sci.append(int(sci))
f1.close()
for i in range(len(list_name)): #점수의 합과 평균을 list_sum, list_avg에 append
    
    list_sum.append(list_kor[i] + list_eng[i] + list_math[i] + list_sci[i])
    list_avg.append((list_kor[i] + list_eng[i] + list_math[i] + list_sci[i])/4)
student_records= list(zip(list_name, list_kor, list_eng, list_math, list_sci, list_sum, list_avg)) #zip함수를 이용해 학생들의 정보를 담은 리스트 생성
for i in range(len(student_records)): #학생 정보 리스트 출력
    print("{}".format(student_records[i]))
    
print("")
print("After calculate_scores(students)")
print("===========================================")
print("{:<5}:   {:5} {:5} {:5} {:5} {:5} {:5}".format("name","kor","eng","math","sci","sum","avg"))
print("-------------------------------------------")
for i in range(len(student_records)): #format을 통한 문자열 정렬 출력
    print("{:<5}: {:5} {:5} {:5} {:5} {:5} {:5.2f}".format(student_records[i][0], student_records[i][1], student_records[i][2], student_records[i][3], student_records[i][4], student_records[i][5], student_records[i][6]))
print("===========================================")
print("")
print("Average score of each class  :") #각 과목의 리스트의 점수를 sum해서 사람수로 나눔
print("{:<7}= {:5.2f}".format("Kor avg", sum(list_kor)/len(student_records)))
print("{:<7}= {:5.2f}".format("Eng avg", sum(list_eng)/len(student_records)))
print("{:<7}= {:5.2f}".format("Math", sum(list_math)/len(student_records)))
print("{:<7}= {:5.2f}".format("Sci", sum(list_sci)/len(student_records)))

with open("output.txt", "w") as f2: #output 파일 f2 쓰기 모드로 생성
    f2.write("name,     kor     eng     math     sum     avg\n")
    f2.write("-------------------------------------------------------\n")
    for student in student_records: #문자를 담는 변수 s에 문자열을 정렬하여 더하면서 마지막에 파일에 쓰기
        s= "{:<7}".format(student[0])
        s+= ":"
        s+= "{:7},".format(student[1])
        s+= "{:7},".format(student[2])
        s+= "{:7},".format(student[3])
        s+= "{:7},".format(student[4])
        s+= "{:7},".format(student[5])
        s+= "{:7.2f},".format(student[6])
        s+= '\n'
        f2.write(s)
f2.close()