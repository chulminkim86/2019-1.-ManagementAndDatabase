#[거북이 띄우기#1]

#거북이를 파이썬쉘에 띄워보기
import turtle as t
t.shape("turtle")

#거북이를 움직여보기
t.forward(50) #50픽셀 앞으로 이동
t.right(90)   #오른쪽으로 90도 회전 
t.forward(50) #50픽셀 앞으로 이동

#거북이로 그림 그리기
t.circle(50) #반지름이 50픽셀인 원 그리기

#거북이로 그림 그리기2
colors=["red", "yellow", "purple"]
t.tracer(0.0)
t.speed(1)
for x in range(100):
    t.circle(x)
    t.color(colors[x%3])
    t.left(60)
