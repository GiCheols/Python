# phonebook.txt파일을 읽기모드로 열기
file = open('phonebook.txt', 'r')

dict = {}   # 이름과 전화번호를 저장할 딕셔너리 생성: 검색을 위한 딕셔너리

for i in file.readlines():  # 텍스트 파일을 한 줄씩 읽어옴
    # ','로 구분되어 있는 첫 번째 값은 이름이므로 key에 저장
    # ','로 구분되어 있는 두 번째 값은 번호이므로 strip함수를 사용해 '\n'값을 지운 후에 딕셔너리의 값으로 저장
    dict[i.split(",")[0]] = i.split(",")[1].strip()


while True: #사용자가 'exit'을 입력하기 전까지 무한 반복
    searchName = input("검색할 이름 >> ")    # 입력한 값을 찾을 이름으로서 변수에 저장함
    if(searchName == "exit"):
        break   # 'exit'을 입력하는 경우 반복문 탈출 및 프로그램 종료
    else:
        # 아닐경우 찾고자 하는 이름을 딕셔너리에서 찾아 해당하는 값을 출력함
        # 예외 처리로 찾고자 하는 이름이 해당 텍스트 파일에 없는 경우 "저장되어 있지 않습니다."라는 문구를 출력
        print(searchName + "의 전화번호는 " + dict.get(searchName, "저장되어 있지 않습니다."))


# 파일 닫기
file.close()
