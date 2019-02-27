import turtle
t=turtle.Pen()
t.reset
def mystar(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    if filled == True:
        t.end_fill()
t.color(0.9, 0.75, 0)      
mystar(120, True)
t.color(0,0,0)
mystar(120, False)
mystar(121, False)
mystar(122, False)
mystar(123, False)
