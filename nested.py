from turtle import*

speed('fast')
pencolor('blue')

side = 5
for i in range(side):
    pensize(8)
    fd(100)
    for i in range(side):
        pensize(4)
        fd(50)
        fillcolor('pink')
        begin_fill()
        for i in range(side):
            pensize(2)
            fd(25)
            dot(10)
            lt(360/side)
        end_fill()
        rt(360/side)
    lt(360/side)

hideturtle()
mainloop()