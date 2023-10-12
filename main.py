import tkinter as tk
import math

flag1 = False
list_dot = list()
s0 = list()
def draw(event):
    global list_dot, s0
    if flag1:
        list_dot.append([event.x, event.y])
        list_dot = sorted(list_dot, key=lambda x: x[1], reverse=True)
        if len(s0) != 0:
            canvas.create_oval(s0[0] - 4, s0[1] - 4, s0[0] + 4, s0[1] + 4, fill="white", outline='green')
        s0 = list_dot[0]

        canvas.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill="white", outline='green')
        canvas.create_oval(s0[0] - 4, s0[1] - 4, s0[0] + 4, s0[1] + 4, fill="red", outline='green')

def add_dot():
    global flag1
    flag1 = True
def clear_canvas():
    global flag1, list_dot
    list_dot.clear()
    flag1 = False
    s0.clear()
    canvas.delete("all")

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def create_shell():
    global flag1, s0, list_dot
    canvas.delete("rt")
    # print(list_dot)
    for now in range(len(list_dot)):
        list_dot[now].append((math.sqrt((list_dot[0][0] - list_dot[now][0])**2 + (list_dot[0][1] - list_dot[now][1])**2)))
        list_dot[now].append((math.degrees(math.atan2(list_dot[now][1] - list_dot[0][1], list_dot[now][0] - list_dot[0][0]))))

    list_dot = sorted(list_dot, key=lambda x: (x[-1], -x[-2]), reverse=True)
    print(list_dot)
    # canvas.create_oval(s0[0] - 4, s0[1] - 4, s0[0] + 4, s0[1] + 4, fill="red", outline='green')
    stack = list()
    print(s0)
    print([list_dot[1][0], list_dot[1][1]])
    stack.append([s0[0], s0[1]])
    stack.append([list_dot[1][0], list_dot[1][1]])
    canvas.create_line(stack[0][0], stack[0][1], stack[1][0], stack[1][1], tags="rt")

    for i in range(2, len(list_dot)):
        while len(stack) > 1 and cross_product(list_dot[i], stack[-1], stack[-2]) <= 0:
            stack.pop()
        stack.append([list_dot[i][0], list_dot[i][1]])
    # print(stack)
    for now1 in range(1, len(stack) - 1):
        canvas.create_line(stack[now1][0], stack[now1][1], stack[now1 + 1][0], stack[now1 + 1][1], tags="rt")
    canvas.create_line(stack[0][0], stack[0][1], stack[-1][0], stack[-1][1], tags="rt")
    flag1 = False

root = tk.Tk()
root.title("Индивидуальное задание. Алгоритм Грэхема")

canvas = tk.Canvas(root, width=800, height=700, bg="#2E2E2E")
canvas.pack()

canvas.bind("<Button-1>", draw)

btn1 = tk.Button(root, text="Задать точки", command=add_dot)
btn1.pack(side="left")

btn2 = tk.Button(root, text="Создать оболочку", command=create_shell)
btn2.pack(side="left")

btn3 = tk.Button(root, text="Очистить холст", command=clear_canvas)
btn3.pack(side="left")

root.mainloop()
