# phonebook.txt파일을 읽기모드로 열기
file = open('phonebook.txt', 'r')

for i in file.readlines():  # 텍스트 파일을 한 줄씩 구분하여 읽어옴
    # ','로 구분되어 있는 첫 번째 값은 이름, 두 번째 값은 전화번호로서 새로운 변수에 저장
    name = i.split(",")[0]
    tel = i.split(",")[1]
    # 이름과 번호를 출력하되, 전화번호의 마지막에는 개행문자인 '\n'이 포함되어 있으므로 strip()함수를 사용해 개행문자를 지움
    print("이름은 " + name + ", 전화번호는 " + tel.strip())

# 파일 닫기
file.close()
