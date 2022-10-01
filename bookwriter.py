# 새로운 파일을 생성하고 쓰기모드로 열기
file = open('phonebook.txt', 'w')

while True: # 무한 반복: 사용자가 "exit"을 입력하기 전까지 무한 반복
    name = input('name >> ')    # 이름을 입력받아 name 변수에 저장
    if(name == "exit"):         # exit을 입력하는 경우
        break                   # 프로그램 종료
    else:
        tel = input('tel >> ')  # exit 입력이 아닌 경우 전화번호를 입력받음
        file.write(name + ",")
        file.write(tel + "\n")  # 파일에 이름과 전화번호를 입력한 후 라인 개행
file.close()    #파일 닫기
