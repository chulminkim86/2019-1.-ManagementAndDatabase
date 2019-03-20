##[거북이 띄우기#2]

#랜덤으로 움직이는 거북이

$ import turtle as t #turtle 패키지 호출
$ import random #random 패키지 호출

$ t.shape("turtle") #turtle 모양 설정
$ t.speed(3) #속도 3

$ for x in range(500): 
      a = random.randint(1, 360)
      t.setheading(a)
      t.forward(10)



