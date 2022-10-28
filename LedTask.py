import time
import RPi.GPIO as GPIO
trig = 20
echo = 16
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)

def ledOnOff(led, onOff): # led 번호의 핀에 onOff(0/1) 값 출력하는 함수
        GPIO.output(led, onOff)

led20 = 5 # 핀 번호 GPIO5 의미, 20cm 이내에 있을 때 출력
GPIO.setup(led20, GPIO.OUT) # GPIO 5번 핀을 출력 선으로 지정.
onOff20 = 1

led10 = 6 # 핀 번호 GPIO6 의미, 10cm 이내에 있을 때 불 들어옴
GPIO.setup(led10, GPIO.OUT) # GPIO 6번 핀을 출력 선으로 지정.
onOff10 = 1

def measureDistance(trig, echo):
    time.sleep(1.0)     # 1초마다 거리를 재도록 설정
    GPIO.output(trig, True) # 신호 1
    GPIO.output(trig, False) # 신호가 1-> 0으로 떨어질 때 초음파발생

    while(GPIO.input(echo) == 0):
        pass

    pulse_start = time.time() # echo 신호가 1인 경우, 초음파 발사된 순간

    while(GPIO.input(echo) == 1):
        pass

    pulse_end = time.time() # 초음파 신호가 도착한 순간
    # echo 신호가 1->0으로 되면 보낸 초음파 수신 완료

    pulse_duration = pulse_end - pulse_start
    return 340*100/2*pulse_duration
    
while True :
    distance = measureDistance(trig, echo)
    print("물체와의 거리는 %fcm입니다" % distance)
    if(distance <= 10.0):    # 거리가 10cm 이하일 때
        onOff20 = 1
        onOff10 = 1
    elif(distance <= 20.0 and distance > 10.0):  # 거리가 10~20cm 사이일 때
        onOff20 = 0
        onOff10 = 1
    else:   # 거리가 20cm 이상인 경우
        onOff20 = 0
        onOff10 = 0

    ledOnOff(led20, onOff20)
    ledOnOff(led10, onOff10)