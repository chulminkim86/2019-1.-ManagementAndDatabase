#[거북이 띄우기#3]

#클릭해서 움직이는 거북이 띄우기

import turtle as t #turtle 패키지 호출

t.shape("turtle") #turtle 모양 설정
t.speed(5) #속도 5

t.pensize(2) #펜 사이즈 2
t.onscreenclick(t.goto) #클릭하면 t.goto 함수 호출
