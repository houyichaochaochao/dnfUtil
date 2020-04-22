#-*-coding:utf-8-*-
import time
from tkinter import*
tk = Tk()
canvas = Canvas(tk,width=400,height=200)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)  ##创建三角形
# canvas.create_polygon(10,10,10,60,50,35)  ##创建三角形


def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(1,0,-3)  ##第一个参数使画布上所画的形状的ID数字，第二个是对x（水平方向）坐标增加的值，第三个是对y（垂直方向）坐标增加的值
    elif event.keysym == 'Down':
        canvas.move(1,0,3)
    elif event.keysym == 'Left':
        canvas.move(1,-3,0)
    else:
        canvas.move(1,3,0)
canvas.bind_all('<KeyPress-Up>',movetriangle)  ##让tkinter监视KeyPress事件，当该事件发生时调用movetriangle函数
canvas.bind_all('<KeyPress-Down>',movetriangle)
canvas.bind_all('<KeyPress-Left>',movetriangle)
canvas.bind_all('<KeyPress-Right>',movetriangle)
tk.mainloop()