def mycircle(red, green, blue):
    import turtle
    t=turtle.Pen()
    t.reset()
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(100)
    t.end_fill()
mycircle(0.9,0.5,0.15)
