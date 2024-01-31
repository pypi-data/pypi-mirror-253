#!/usr/bin/python

from tkinter import *
from tkinter import ttk
import networkx as nx

import sys

from .pace import read_graph

CPAD = 5
RPAD = 20
LDIST = 200
HDIST = 0
RECT_SIZE = 25

w = 2

graph = None
order = {}
order_reverse = {}

def resize(event):
    print("widget", event.widget)
    print("height", event.height, "width", event.width)
    
def load_graph():
    global graph
    global order
    global order_reverse
    graph = read_graph(sys.argv[1])
    # draw_graph(graph)

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

Canvas.create_circle = _create_circle

def draw_graph_force():
    canvas.delete('all')
    hrs = RECT_SIZE/2.0
    pos = nx.spring_layout(graph.G)

    minx, miny, maxx, maxy = float('inf'), float('inf'), float('-inf'), float('-inf')
    for v in graph.G.nodes:
        if pos[v][0] > maxx:
            maxx = pos[v][0]
        if pos[v][0] < minx:
            minx = pos[v][0]
        if pos[v][1] > maxy:
            maxy = pos[v][1]
        if pos[v][1] < miny:
            miny = pos[v][1]

    newpos = {}

    for p in pos:
        newpos[p] = ((pos[p][0]-minx)*(300/(maxx-minx))+50, (pos[p][1]-miny)*(300/(maxy-miny))+50)

    for e in graph.G.edges:
        s = tuple(newpos[e[0]])
        t = tuple(newpos[e[1]])

        # print(e, s, t)

        canvas.create_line(*s, *t, fill="#AAA", width=w+0.5)
        canvas.create_line(*s, *t, width=w)

    for v in graph.G.nodes:
        if v < graph.a:
            color = "#9fc0de"
        else:
            color = "#f2c894"
        canvas.create_circle(*newpos[v], hrs, width=w+0.5, outline="#AAA")
        canvas.create_circle(*newpos[v], hrs, width=w, fill=color)
        canvas.create_text(*newpos[v], text=f"{v}", fill="black")

def reorder():
    global order
    global order_reverse
    order = {}
    with open(sys.argv[2]) as file:
        lines = file.readlines()
        counter = 0
        for line in lines:
            order[int(line)] = counter
            order_reverse[counter] = int(line)
            counter += 1
    print(order)
    print(order_reverse)


def draw_graph_with_order():
    canvas.delete('all')
    hrs = RECT_SIZE/2.0
    lcenters = [(CPAD + hrs + (RPAD + RECT_SIZE + HDIST) * i, CPAD + hrs) for i in range(0, graph.a)]
    rcenters = [(CPAD + hrs + (RPAD + RECT_SIZE + HDIST) * i, CPAD + hrs + LDIST) for i in range(0, graph.b)]
        
    for e in graph.G.edges:
        s = lcenters[e[0]]
        t = rcenters[order[e[1]]]
        
        canvas.create_line(*s, *t, fill="#AAA", width=w+0.5)
        canvas.create_line(*s, *t, width=w)
        
    for i, c in enumerate(lcenters + rcenters):
        # canvas.create_rectangle(c[0] - hrs, c[1] - hrs, c[0] + hrs, c[1] + hrs, fill="black")
        if i < graph.a:
            color = "#9fc0de"
            canvas.create_circle(c[0], c[1], hrs, width=w+0.5, outline="#AAA")
            canvas.create_circle(c[0], c[1], hrs, width=w, fill=color)
            canvas.create_text(c, text=f"{i}", fill="black")
        else:
            color = "#f2c894"
            canvas.create_circle(c[0], c[1], hrs, width=w+0.5, outline="#AAA")
            canvas.create_circle(c[0], c[1], hrs, width=w, fill=color)
            canvas.create_text(c, text=f"{order_reverse[i-graph.a]}", fill="black")

def draw_graph():
    canvas.delete('all')
    hrs = RECT_SIZE/2.0
    lcenters = [(CPAD + hrs + (RPAD + RECT_SIZE + HDIST) * i, CPAD + hrs) for i in range(0, graph.a)]
    rcenters = [(CPAD + hrs + (RPAD + RECT_SIZE + HDIST) * i, CPAD + hrs + LDIST) for i in range(0, graph.b)]
        
    for e in graph.G.edges:
        s = lcenters[e[0]]
        t = rcenters[e[1] - graph.a]
        
        canvas.create_line(*s, *t, fill="#AAA", width=w+0.5)
        canvas.create_line(*s, *t, width=w)
        
    for i, c in enumerate(lcenters + rcenters):
        # canvas.create_rectangle(c[0] - hrs, c[1] - hrs, c[0] + hrs, c[1] + hrs, fill="black")
        if i < graph.a:
            color = "#9fc0de"
        else:
            color = "#f2c894"
        canvas.create_circle(c[0], c[1], hrs, width=w+0.5, outline="#AAA")
        canvas.create_circle(c[0], c[1], hrs, width=w, fill=color)
        canvas.create_text(c, text=f"{i}", fill="black")

# def select_file():
#     filetypes = (('instance files', '*.gr'))
#     filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
#     showinfo(title='Selected File', message=filename)

def visualize():
    root = Tk()
    root.title("Pace 2024")

    mainframe = ttk.Frame(root, width=600, height=400, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.columnconfigure(0, weight=1)

    global canvas 
    canvas = Canvas(mainframe, width=600, height=400, bg="white")
    canvas.grid(column=0, row=0, sticky=W, columnspan=5)
    canvas.rowconfigure(0, weight=1)
    canvas.columnconfigure(0, weight=1)

    loadbutton = ttk.Button(mainframe, text="Load graph", command=load_graph)
    loadbutton.grid(column=0, row=1, sticky=W)
    loadbutton.rowconfigure(1, weight=1)
    loadbutton.columnconfigure(0, weight=1)

    orderbutton = ttk.Button(mainframe, text="Load solution", command=reorder)
    orderbutton.grid(column=1, row=1, sticky=W)
    orderbutton.rowconfigure(1, weight=1)
    orderbutton.columnconfigure(1, weight=1)

    drawbutton = ttk.Button(mainframe, text="Draw 2-sided", command=draw_graph)
    drawbutton.grid(column=2, row=1, sticky=W)
    drawbutton.rowconfigure(1, weight=1)
    drawbutton.columnconfigure(2, weight=1)

    drawsolbutton = ttk.Button(mainframe, text="Draw 2-sided solved", command=draw_graph_with_order)
    drawsolbutton.grid(column=3, row=1, sticky=W)
    drawsolbutton.rowconfigure(1, weight=1)
    drawsolbutton.columnconfigure(3, weight=1)

    drawforcebutton = ttk.Button(mainframe, text="Draw force", command=draw_graph_force)
    drawforcebutton.grid(column=4, row=1, sticky=W)
    drawforcebutton.rowconfigure(1, weight=1)
    drawforcebutton.columnconfigure(4, weight=1)

    # canvas.bind("<Configure>", resize)
    load_graph()
    reorder()

    root.mainloop()