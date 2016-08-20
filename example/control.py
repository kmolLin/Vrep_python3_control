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
import math
 
LARGE_FONT = ("Verdana",12)
NORM_FONT = ("Verdana",10)
SMALL_FONT = ("Verdana",8)
style.use("ggplot")
 
f = Figure(figsize = (5,5),dpi = 100)
a = f.add_subplot(111)
 

def tutorial():
 #   def leavmini(what)
#        what.destroy

    def page2():
        tut.destroy()
        tut2 = tk.Tk()

        def page3():
            tut2.destroy()
            tut3 = tk.Tk()
            
            tut3.wm_title("part 3!")
            label = ttk.Label(tut3,text = "Part 3",font =NORM_FONT )
            label.pack(side = "top",fill = "x",pady = 10)
            B1 = ttk.Button(tut3,text = "Done!",command = tut3.destroy)
            B1.pack()
            tut3.mainloop()

        tut2.wm_title("part 2!")
        label = ttk.Label(tut2,text = "Part 2",font =NORM_FONT )
        label.pack(side = "top",fill = "x",pady = 10)
        B1 =ttk.Button(tut2,text = "Next",command = page3)
        B1.pack()
        tut2.mainloop()

    tut = tk.Tk()
    tut.wm_title("Tutorial")
    label = ttk.Label(tut,text = "what do you want to help",font =NORM_FONT )
    label.pack(side = "top",fill = "x",pady = 10)

    B1 = ttk.Button(tut,text = "Overview the app",command = lambda:popupmsg("Not yet"))
    B1.pack()
    B2 = ttk.Button(tut,text = "test",command = page2)
    B2.pack()
    B3 = ttk.Button(tut,text = "Questione",command = lambda:popupmsg("Not yet"))
    B3.pack()
    
    tut.mainloop()


def popupmsg(msg):
    popup = tk.Tk()
    def leavemini():
        popup.destroy()
    popup.wm_title("!")
    label = ttk.Label(popup,text=msg,font=NORM_FONT)
    label.pack(side ="top",fill="x",pady=10)
    B1 = ttk.Button(popup,text="Okay",command = leavemini)
    B1.pack()
    popup.mainloop()


def animate(i):
     
    pullData = open(i,"r").read()
    print(pullData)
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine)>1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))

    a.clear()
    a.plot(xList,yList)



def home():


    vrep.simxFinish(-1)
    clientID = vrep.simxStart('127.0.0.1', 19998, True, True, 5000, 5)
    if clientID!= -1:
        print("Connected to remote server")
    else:
        print('Connection not successful')
        sys.exit('Could not connect')
    errorCode,plate=vrep.simxGetObjectHandle(clientID,'plate',vrep.simx_opmode_oneshot_wait)
    if errorCode == -1:
        print('Can not find plate')
        sys.exit()                
    errorCode=vrep.simxSetObjectPosition(clientID,plate,-1,[0,0,0.4465], vrep.simx_opmode_oneshot)


def speed1():

    vrep.simxFinish(-1)
    clientID = vrep.simxStart('127.0.0.1', 19998, True, True, 5000, 5)
    if clientID!= -1:
        print("Connected to remote server")
    else:
        print('Connection not successful')
        sys.exit('Could not connect')
    errorCode,fan=vrep.simxGetObjectHandle(clientID,'fan',vrep.simx_opmode_oneshot_wait)
    if errorCode == -1:
        print('Can not find fan')
        sys.exit()                
    errorCode=vrep.simxSetJointTargetVelocity(clientID,fan,9, vrep.simx_opmode_oneshot)




 
class Seaofbt(tk.Tk):
 
    def __init__(self, *args, **kwargs):  #程式執行時先預載入的參數或者動作
        tk.Tk.__init__(self, *args, **kwargs)
 
  #      tk.Tk.iconbitmap(self,default = "client.ico")  改變左上角的圖示
        tk.Tk.wm_title(self,"My works")
 
        container = tk.Frame(self)        
        container.pack(side="top",fill="both",expand = True)
        container.grid_rowconfigure(0,weigh=1)
        container.grid_columnconfigure(0,weigh=1)
 
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar,tearoff =0)
        filemenu.add_command(label="read file",command = lambda: popupmsg(self))
        filemenu.add_separator()
        filemenu.add_command(label = "Exit",command=quit)
        menubar.add_cascade(label="File",menu=filemenu)
    

        helpmenu = tk.Menu(menubar,tearoff=1)
        helpmenu.add_command(label = "Tutorial",command = tutorial)
        menubar.add_cascade(label = "HELP",menu=helpmenu)

        Printer = tk.Menu(menubar,tearoff=2)
        Printer.add_command(label = "Home All",command = home)
        menubar.add_cascade(label = "3D_Printer",menu=Printer)
        
        fanmenu = tk.Menu(Printer)

        fanmenu.add_command(label = "0 %",command = speed1)
        Printer.add_cascade(label='Fan_speed', menu=fanmenu)

        tk.Tk.config(self,menu=menubar)
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
        label = tk.Label(self,text="Vrep control",font = LARGE_FONT)
        label.pack(pady = 10,padx = 10)

        button1 = ttk.Button(self,text = "Vrep 手臂控制",
                                    command = lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self,text = "Vrep 3D列印控制",
                                    command = lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self,text = "Graph Page",
                                    command = lambda: controller.show_frame(PageThree))
        button3.pack()

 
class PageOne(tk.Frame):
 
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)

        self.createWidgets()
        self.getNumber1 = 0
        self.getNumber2 = 0
        self.getNumber3 = 0
        self.getNumber4 = 0
        self.getNumber5 = 0

        label0 = tk.Label(self,text="Position").grid(column=1, row=0)
        label1 = tk.Label(self,text="").grid(column=0, row=1)
        label2 = tk.Label(self,text="齒輪軸").grid(column=0, row=2)
        label3 = tk.Label(self,text="").grid(column=0, row=3)
        label4 = tk.Label(self,text="大軸").grid(column=0, row=4)
        label5 = tk.Label(self,text="").grid(column=0, row=5)
        label6 = tk.Label(self,text="小軸").grid(column=0, row=6)
        label7 = tk.Label(self,text="").grid(column=0, row=7)
        label8 = tk.Label(self,text="").grid(column=0, row=9)
        label9 = tk.Label(self,text="夾子轉軸").grid(column=0, row=8)
        label10 = tk.Label(self,text="夾子").grid(column=0, row=10)
        label11 = tk.Label(self,text="Uint").grid(column=2, row=0)
        label12 = tk.Label(self,text="degree").grid(column=2, row=2)
        label13 = tk.Label(self,text="degree").grid(column=2, row=4)
        label14 = tk.Label(self,text="degree").grid(column=2, row=6)
        label15 = tk.Label(self,text="degree").grid(column=2, row=8)
        label16 = tk.Label(self,text="degree").grid(column=2, row=10)


        button1 = ttk.Button(self,text = "Back",
                                    command = lambda: controller.show_frame(StartPage))
        button1.grid(row = 20,column = 2)

        button2 = ttk.Button(self, text='Quit', width=5, command=self.quit)
        button2.grid(row = 20,column = 1)

        button3 = ttk.Button(self, text='Go', width=5, command =lambda:self.show_entry_fields())
        button3.grid(row = 20,column = 0)


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
        self.entry4 = tk.Entry(self)
        self.entry4["width"] = 12
        self.entry4.grid(row=8, column=1)
        self.entry5 = tk.Entry(self)
        self.entry5["width"] = 12
        self.entry5.grid(row=10, column=1)
        

 
    def show_entry_fields(self):
        deg = math.pi/180
        self.getNumber1 = self.entry1.get()
        self.getNumber2 = self.entry2.get()
        self.getNumber3 = self.entry3.get()
        self.getNumber4 = self.entry4.get()
        self.getNumber5 = self.entry5.get()



        x = self.getNumber1
        y = self.getNumber2
        z = self.getNumber3
        a = self.getNumber3
        b = self.getNumber3
        if x =='' or y==''or z =='' or a=='' or b=='':
            x = 0
            y = 0
            z = 0
            a = 0
            b = 0
            print("Error")
 
        else:
            x = float(self.getNumber1)
            y = float(self.getNumber2)
            z = float(self.getNumber3)
            a = float(self.getNumber4)
            b = float(self.getNumber5)

            if float(y) <= 0:
                y = y*(-1)
 
            if float(z) <= 0:
                z = z*(-1)
            
            #x = x/0.4583


 
            vrep.simxFinish(-1)
            clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
            if clientID!= -1:
                print("Connected to remote server")
            else:
                print('Connection not successful')
                sys.exit('Could not connect')

            errorCode1,Joint1=vrep.simxGetObjectHandle(clientID,'joint1',vrep.simx_opmode_oneshot_wait)
            errorCode2,Joint2=vrep.simxGetObjectHandle(clientID,'joint2',vrep.simx_opmode_oneshot_wait)
            errorCode3,Joint3=vrep.simxGetObjectHandle(clientID,'joint3',vrep.simx_opmode_oneshot_wait)
            errorCode4,Super=vrep.simxGetObjectHandle(clientID,'super',vrep.simx_opmode_oneshot_wait)
            errorCode5,Catch=vrep.simxGetObjectHandle(clientID,'catch',vrep.simx_opmode_oneshot_wait)

            if errorCode1 == -1:
                print('Can not find joint1')
                sys.exit()            
            if errorCode2 == -1:
                print('Can not find joint2')
                sys.exit()            
            if errorCode3 == -1:
                print('Can not find joint3')
                sys.exit()            
            if errorCode4 == -1:
                print('Can not find super')
                sys.exit()            
            if errorCode5 == -1:
                print('Can not find catch')
                sys.exit()   
    
            errorCode1=vrep.simxSetJointTargetPosition(clientID,Joint1,x*deg, vrep.simx_opmode_oneshot)
            errorCode2=vrep.simxSetJointTargetPosition(clientID,Joint2,y*deg, vrep.simx_opmode_oneshot)
            errorCode3=vrep.simxSetJointTargetPosition(clientID,Joint3,z*deg, vrep.simx_opmode_oneshot)
            errorCode4=vrep.simxSetJointTargetPosition(clientID,Super,a*deg, vrep.simx_opmode_oneshot)
            errorCode5=vrep.simxSetJointTargetPosition(clientID,Catch,b*deg, vrep.simx_opmode_oneshot)

            print(x,y,z,a,b)

 
class PageTwo(tk.Frame):
        
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)

        self.createWidgets()
        self.getNumber1 = 0
        self.getNumber2 = 0
        self.getNumber3 = 0
  


        label1 = tk.Label(self,text="Axis").grid(column=0, row=0)
        label2 = tk.Label(self,text="X").grid(column=0, row=2)
        label3 = tk.Label(self,text="").grid(column=0, row=3)
        label4 = tk.Label(self,text="Y").grid(column=0, row=4)
        label5 = tk.Label(self,text="").grid(column=0, row=5)
        label6 = tk.Label(self,text="Z").grid(column=0, row=6)
        label7 = tk.Label(self,text="Position").grid(column=1, row=0)
        label8 = tk.Label(self,text="-125<=X<=125").grid(column=1, row=1)
        label9 = tk.Label(self,text="-125<=Y<=125").grid(column=1, row=3)
        label10 = tk.Label(self,text="0<=Z<=330").grid(column=1, row=5)
        label11 = tk.Label(self,text="Unit").grid(column=2, row=0)
        label12 = tk.Label(self,text="degree").grid(column=2, row=2)
        label13 = tk.Label(self,text="degree").grid(column=2, row=4)
        label14 = tk.Label(self,text="degree").grid(column=2, row=6)


        button1 = ttk.Button(self,text = "Back",
                                    command = lambda: controller.show_frame(StartPage))
        button1.grid(row = 10,column = 2)

        button2 = ttk.Button(self, text='Quit', width=5, command=self.quit)
        button2.grid(row = 10,column = 1)

        button3 = ttk.Button(self, text='Go', width=5, command =lambda:self.show_entry_fields())
        button3.grid(row = 10,column = 0)



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
        deg = math.pi/180
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
 
 
            if float(x) >= 125:
                x = 125
                print("X_axis is out of range")
            if float(y) >= 125:
                y = 125
                print("Y_axis is out of range")
            if float(z) >= 400:
                z = 400     
                print("Z_axis is out of range")
            if float(x) <= -125:
                x = -125
                print("X_axis is out of range")
            if float(y) <= -125:
                y = -125
                print("Y_axis is out of range")
            if float(z) < 0:
                z = 0
                print("Z_axis is out of range")

            if (float(x) <= -125*math.sin(30*deg)) & (float(y) >= 125*math.cos(30*deg)):
                x = -125*math.sin(30*deg)
                y = 125*math.cos(30*deg)

            if (float(x) <= -125*math.sin(30*deg)) & (float(y) <= -125*math.cos(30*deg)):
                x = -125*math.sin(30*deg)
                y = -125*math.cos(30*deg)

            if (float(x) >= 125*math.sin(30*deg)) & (float(y) >= 125*math.cos(30*deg)):
                x = 125*math.sin(30*deg)
                y = 125*math.cos(30*deg)

            if (float(x) >= -125*math.sin(30*deg)) & (float(y) <= -125*math.cos(30*deg)):
                x = 125*math.sin(30*deg)
                y = -125*math.cos(30*deg)

            if float(z) >= 330:
                z = 330

            e=x/1000     # v-rep world unit is meter  , 
            r=y/1000
            t=z/1000
            t = t+0.1165   # t = 0  , heater touch the heat bed  ( heat bed is 0.1165 high ) 
            if t <=0:
                t = 0
 
            vrep.simxFinish(-1)
            clientID = vrep.simxStart('127.0.0.1', 19998, True, True, 5000, 5)
            if clientID!= -1:
                print("Connected to remote server")
            else:
                print('Connection not successful')
                sys.exit('Could not connect')
            errorCode,plate=vrep.simxGetObjectHandle(clientID,'plate',vrep.simx_opmode_oneshot_wait)
            if errorCode == -1:
                print('Can not find plate')
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
