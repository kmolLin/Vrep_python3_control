import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import matplotlib.animation as animation
from matplotlib import style

import numpy as np

import tkinter as tk
from tkinter import ttk

from matplotlib import pyplot, rcParams
import serial
import sys
import vrep


LARGE_FONT = ("Verdana",12)
style.use("ggplot")

f = Figure(figsize = (5,5),dpi = 100)
a = f.add_subplot(111)



#def animate(i):
    









   # pullData = open("sampleData.txt","r").read()
   # dataList = pullData.split('\n')
   # xList = []
   # yList = []
   # for eachLine in dataList:
    #    if len(eachLine)>1:
     #       x, y = eachLine.split(',')
      #      xList.append(int(x))
       #     yList.append(int(y))

   # a.clear()
   # a.plot(xList,yList)

class Seaofbt(tk.Tk):

    def __init__(self, *args, **kwargs):  #程式執行時先預載入的參數或者動作
        tk.Tk.__init__(self, *args, **kwargs)

  #      tk.Tk.iconbitmap(self,default = "client.ico")  改變左上角的圖示
        tk.Tk.wm_title(self,"My works")

        container = tk.Frame(self)        
        container.pack(side="top",fill="both",expand = True)
        container.grid_rowconfigure(0,weigh=1)
        container.grid_columnconfigure(0,weigh=1)

        self.frames = {}

        for F in (StartPage, PageOne,PageTwo,PageThree):
        
            frame = F(container,self)

            self.frames[F] = frame

            frame.grid(row=0, column = 0, sticky="nsew")

        self.show_frame(StartPage)


    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

def qf(param):
    print(param)


class StartPage(tk.Frame):
    
    def __init__(self,parent,controller):

        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="PageOne",font = LARGE_FONT)
        label.pack(pady = 10,padx = 10)

        button1 = ttk.Button(self,text = "Visit Page 1",
                                    command = lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self,text = "Visit Page 2",
                                    command = lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self,text = "Graph Page",
                                    command = lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):
        
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Start Page",font = LARGE_FONT)
        label.pack(pady = 10,padx = 10)
        
        
        button1 = ttk.Button(self,text = "Back to Home",
                                    command = lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self,text = "Visit Page2",
                                    command = lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(tk.Frame):
        
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)

        self.createWidgets()
        self.getNumber1 = 0
        self.getNumber2 = 0
        self.getNumber3 = 0

        label1 = tk.Label(self,text="").grid(column=0, row=1)
        label2 = tk.Label(self,text="X").grid(column=0, row=2)
        label3 = tk.Label(self,text="").grid(column=0, row=3)
        label4 = tk.Label(self,text="Y").grid(column=0, row=4)
        label5 = tk.Label(self,text="").grid(column=0, row=5)
        label6 = tk.Label(self,text="Z").grid(column=0, row=6)


        button1 = ttk.Button(self,text = "Back",
                                    command = lambda: controller.show_frame(StartPage))
        button1.grid(row = 20,column = 3)

        button2 = ttk.Button(self, text='Quit', width=5, command=self.quit)
        button2.grid(row = 20,column = 2)

        button3 = ttk.Button(self, text='Go', width=5, command =lambda:self.show_entry_fields())
        button3.grid(row = 20,column = 1)


    def createWidgets(self):
        self.entry1 = tk.Entry(self)
        self.entry1["width"] = 12
        self.entry1.grid(row=2, column=1)
        self.entry2 = tk.Entry(self)
        self.entry2["width"] = 12
        self.entry2.grid(row=4, column=1)
        self.entry3 = tk.Entry(self)
        self.entry3["width"] = 12
        self.entry3.grid(row=6, column=1)

        

 
    def show_entry_fields(self):

        self.getNumber1 = self.entry1.get()
        self.getNumber2 = self.entry2.get()
        self.getNumber3 = self.entry3.get()
  
        x = self.getNumber1
        y = self.getNumber2
        z = self.getNumber3
 
        if x =='' or y==''or z =='':
            x = 0
            y = 0
            z = 0
            print("Error")
 
        else:
            x = float(self.getNumber1)
            y = float(self.getNumber2)
            z = float(self.getNumber3)
 
 
            if float(x) >= 100:   # set x&y&z limit 
                x = 100
            if float(y) >= 100:
                y = 100
            if float(z) >= 400:
                z = 400
            if float(x) <= -100:
                x = -100
            if float(y) <= -100:
                y = -100
            if float(z) <= 0:
                z = 0
            e=x/1222
            r=y/1222
            t=z/889
            if t <= 0.11656:
                t = t+0.11656
 
 
            vrep.simxFinish(-1)
            clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
            if clientID!= -1:
                print("Connected to remote server")
            else:
                print('Connection not successful')
                sys.exit('Could not connect')
            errorCode,plate=vrep.simxGetObjectHandle(clientID,'plate',vrep.simx_opmode_oneshot_wait)
            if errorCode == -1:
                print('Can not find left or right motor')
                sys.exit()                
            errorCode=vrep.simxSetObjectPosition(clientID,plate,-1,[e,r,t], vrep.simx_opmode_oneshot)
            print(x,y,z)
  

 


class PageThree(tk.Frame):
        
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Graph Pages",font = LARGE_FONT)
        label.pack(pady = 10,padx = 10)
        button1 = ttk.Button(self,text = "Back to Home",
                                    command = lambda: controller.show_frame(StartPage))
        button1.pack()
        
    
        


        #f = Figure(figsize = (5,5),dpi = 100)
        #a = f.add_subplot(111)
        #a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        
        canvas = FigureCanvasTkAgg(f,self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP , fill=tk.BOTH,expand=True)
        
        toolbar = NavigationToolbar2TkAgg(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side = tk.TOP,fill = tk.BOTH,expand =True)


        


app  = Seaofbt()
#ani = animation.FuncAnimation(f,animate,interval = 1000)
app.mainloop()



