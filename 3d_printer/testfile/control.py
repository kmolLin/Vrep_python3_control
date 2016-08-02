import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
#from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

from tkinter import Frame, Tk, BOTH, Text, Menu, END
import numpy as np
import json
import urllib
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import serial
import sys
import vrep




LARGE_FONT = ("Verdana",12)
NORM_FONT = ("Verdana",10)
SMALL_FONT = ("Verdana",8)
style.use("ggplot")

f = plt.figure()
#a = f.add_subplot(111)

exchange = "BTC"
DatCounter = 9000
programName = "btc"
resampleSize = "15Min"
DataPace = "tick"
candleWidth = 0.008

paneCount = 1
topIndicator = "None"
bottomIndicator = "None"
middleIndicator = "None"
chartLoad = True
EMAs = []
SMAs = []


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

def loadChart(run):
    global chartLoad
    if run =="start":
        chartLoad = True
    elif run =="stop":
        chartLoad = False


def addMiddleIndicator(what):
    global middleIndicator
    global DatCounter

    if DataPace == "tick":
        popimsg("Indicator")

    if what != "none":
        if middleIndicator =="none":
            if what =="sma":
                midIQ = tk.Tk()
                midIQ.wm_title("periods")
                label = ttk.Label(midIQ,text = "chose")
                label.pack(side = "top",fill = "x",pady = 10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()
                def callback():
                    global middleIndicator
                    global DatCounter
                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))                    
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middle set indicator to ",middleIndicator)
                    midIQ.destroy()
                b = ttk.Button(midIQ,texxt = "Submit",width = 10,command = callback)
                b.pack()
                tk.mainloop()                

            if what =="ema":
                midIQ = tk.Tk()
                midIQ.wm_title("periods")
                label = ttk.Label(midIQ,text = "chose")
                label.pack(side = "top",fill = "x",pady = 10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()
                def callback():
                    global middleIndicator
                    global DatCounter
                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))                    
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middle set indicator to ",middleIndicator)
                    midIQ.destroy()
                b = ttk.Button(midIQ,texxt = "Submit",width = 10,command = callback)
                b.pack()
                tk.mainloop()
            
        else:
                if what == "ema":
                    midIQ = tk.Tk()
                    midIQ.wm_title("periods")
                    label = ttk.Label(midIQ,text = "chose")
                    label.pack(side = "top",fill = "x",pady = 10)
                    e = ttk.Entry(midIQ)
                    e.insert(0,10)
                    e.pack()
                    e.focus_set()
                    def callback():
                        global middleIndicator
                        global DatCounter
                      #  middleIndicator = []
                        periods = (e.get())
                        group = []
                        group.append("ema")
                        group.append(int(periods))                    
                        middleIndicator.append(group)
                        DatCounter = 9000
                        print("middle set indicator to ",middleIndicator)
                        midIQ.destroy()
                    b = ttk.Button(midIQ,text = "Submit",width = 10,command = callback)
                    b.pack()
                    tk.mainloop()
    else:
        middleIndicator = "none"

def addTopIndicator(what):
    global topIndicator
    global DatCounter

    if DataPace == "tick":
        popimsg("Indicator")
    elif what =="none":
        topIndicator = what
        DatCounter = 9000

    elif what =="rsi":
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")
        label = ttk.Label(rsiQ,text = "chosse a small time to consider.")
        label.pack(side = "top",fill = "x",pady = 10)
        
        e = ttk.Entry(rsiQ)
        e.insert(0,14)
        e.pack()
        e.focus_set()
        def callback():
            global topIndicator
            global DatCounter
            periods = (e.get())
            group = []
            group.append("rsi")
            group.append(periods)
            
            topIndicator = group
            DatCounter = 9000
            print("set top indicator to ",group)
            rsiQ.destroy()


        b = ttk.Button(rsiQ,text = "Submit",width = 10,command=callback)
        b.pack()
        tk.mainloop()


    elif what =="macd":
        global topIndicator
        global DatCounter
        topIndicator = "macd"
        DatCounter = 9000

def addBottomIndicator(what):
    global bottomIndicator
    global DatCounter

    if DataPace == "tick":
        popimsg("Indicator")
    elif what =="none":
        bottomIndicator = what
        DatCounter = 9000

    elif what =="rsi":
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")
        label = ttk.Label(rsiQ,text = "chosse a small time to consider.")
        label.pack(side = "top",fill = "x",pady = 10)
        
        e = ttk.Entry(rsiQ)
        e.insert(0,14)
        e.pack()
        e.focus_set()
        def callback():
            global bottomIndicator
            global DatCounter
            periods = (e.get())
            group = []
            group.append("rsi")
            group.append(periods)
            
            bottomIndicator = group
            DatCounter = 9000
            print("set BOT indicator to ",group)
            rsiQ.destroy()


        b = ttk.Button(rsiQ,text = "Submit",width = 10,command=callback)
        b.pack()
        tk.mainloop()


    elif what =="macd":
        global bottomIndicator
        global DatCounter
        bottomIndicator = "macd"
        DatCounter = 9000

            


def changeTimeFrame(tf):
    global resampleSize
    global dataPace
    if tf =="7d" and resampleSize =="1Min":
        popupmsg("Not yet")
    else:
        DataPace = tf
        DatCounter = 9000

def changeSampleSize(size,width):
    global resampleSize
    global DatCounter
    global candleWidth
    if DataPace =="7d" and resampleSize =="1Min":
        popupmsg("Not yet")
    
    elif DataPace =="tick":
        popupmsg("you're currently")
    
    else:
        resampleSize = size
        DatCounter = 9000
        candleWidth = width




def changeExchange(toWhat,pn):
    global exchange
    global DatCounter
    global programName

    exchange = toWhat
    programName = pn
    DatCounter = 9000

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

#def onOpen(getv):

    #ftypes = [('Python files', '*.py'), ('All files', '*')]
    #dlg = filedialog.Open(getv, filetypes = ftypes)
    #fl = dlg.show()

  #  if fl != '':
    
        #text = getv.readFile(fl).
        #getv.txt.insert(END, text)
        
        
        #pullData = open(fl,"r").read()
        

#def readFile(filename):


    #f = open(filename, "r").read()
   # text = f.read().decode("utf-8")
 #   #return f


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
   
 
    '''global DatCounter

    if chartLoad:
        if paneCount ==1:
            if DataPace =="tick":
                try:
                    a = plt.subplot2grid((6,4),(0,0),rowspan = 5,colspan = 4)
                    a2 = plt.subplot2grid((6,4),(0,0),rowspan = 1,colspan = 4,sharex = a)
                                
                    dataLink = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
                    data = urllib.request.urlopen(dataLink)

                    data = data.readall().decode("utf-8")
                    data = json.loads(data)

                    
                    data = data["btc_usd"]
                    data = pd.DataFrame(data)

                    data["datestamp"] = np.array(data["timestamp"]).astype("datetime64[s]")
                    allDates = data["datestamp"].tolist()
                    buys = data[(data['type']=="bid")]
                    #buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
                    buyDates = (buys["datestamp"]).tolist()

                    sells = data[(data['type']=="ask")]
                    #sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
                    sellDates = (sells["datestamp"]).tolist()

                    volume = data["amount"]

                    a.clear()
                    a.plot_date(buyDates,buys["price"],"#00A3E0",label = "buys")
                    a.plot_date(sellDates,sells["price"],"#183A54",label = "sells")

                    a2.fill_between(allDates,0,volume,facecolor = "#183A54")

                    a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                    a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:M:S"))

                    a.legend(bbox_to_anchor =(0,1.02,1,.102),loc = 3,
                                ncol = 2,borderaxespad=0)

                    title = "BTC price"
                    a.set_title(title)
                except Exception as e:
                    print("failue",e)
'''





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

        exchangeChoice = tk.Menu(menubar,tearoff=1)
        exchangeChoice.add_command(label = "BTC",command = lambda:changeExchange("BTC","btc"))
        exchangeChoice.add_command(label = "Bitstamp",command = lambda:changeExchange("Bitstamp","bITSTAMP"))
        exchangeChoice.add_command(label = "Huobi",command = lambda:changeExchange("Huobi","btc"))
        menubar.add_cascade(label="Exchange",menu=exchangeChoice)
        

        dataTF = tk.Menu(menubar,tearoff=1)
        dataTF.add_command(label = "1 Day",
                                    command = lambda: changeTimeFrame('1d'))
        dataTF.add_command(label = "3 Day",
                                    command = lambda: changeTimeFrame('3d'))
        dataTF.add_command(label = "1 Week",
                                    command = lambda: changeTimeFrame('7d'))
        menubar.add_cascade(label = "Data Time Frame",menu = dataTF)


        OHLCI = tk.Menu(menubar,tearoff=1)
        OHLCI.add_command(label = "Tick",
                                    command = lambda: changeSampleSize('tick'))
        OHLCI.add_command(label = "1 Minute",
                                    command = lambda: changeSampleSize('1Min',0.0005))
        OHLCI.add_command(label = "5 Minute",
                                    command = lambda: changeSampleSize('5Min',0.03))
        OHLCI.add_command(label = "15 Minute",
                                    command = lambda: changeSampleSize('15Min',0.08))
        OHLCI.add_command(label = "30 Minute",
                                    command = lambda: changeSampleSize('30Min',0.016))
        OHLCI.add_command(label = "1  Hour",
                                    command = lambda: changeSampleSize('1H',0.03))
        menubar.add_cascade(label = "OHLCI",menu = OHLCI)
        


        topIndi = tk.Menu(menubar,tearoff = 1)
        topIndi.add_command(label = "None",
                                    command = lambda: addTopIndicator('None'))
        topIndi.add_command(label = "RSI",
                                    command = lambda: addTopIndicator('rsi'))
        topIndi.add_command(label = "MACD",
                                    command = lambda: addTopIndicator('macd'))
        menubar.add_cascade(label = "Top Indicator",menu = topIndi)



        mainI = tk.Menu(menubar,tearoff = 1)
        mainI.add_command(label = "None",
                                    command = lambda: addMiddleIndicator('None'))
        mainI.add_command(label = "SMA",
                                    command = lambda: addMiddleIndicator('sma'))
        mainI.add_command(label = "EMA",
                                    command = lambda: addMiddleIndicator('ema'))
        menubar.add_cascade(label = "Main/middle Indicator",menu = mainI)



        bottomI = tk.Menu(menubar,tearoff = 1)
        bottomI.add_command(label = "None",
                                    command = lambda: addBottomIndicator('None'))
        bottomI.add_command(label = "RSI",
                                    command = lambda: addBottomIndicator('rsi'))
        bottomI.add_command(label = "MACD",
                                    command = lambda: addBottomIndicator('macd'))
        menubar.add_cascade(label = "Bottom Indicator",menu = bottomI)
        

        tradeButton = tk.Menu(menubar,tearoff = 1)
        tradeButton.add_command(label = "Manual Trading",
                                                command = lambda: popupmsg("this not yet"))
        tradeButton.add_command(label = "Automated Trading",
                                                command = lambda: popupmsg("Audomated not yet"))
        
        tradeButton.add_separator()
        tradeButton.add_command(label = "Quick buy",
                                                command = lambda: popupmsg("quick not yet"))
        tradeButton.add_command(label = "Quick sell",
                                                command = lambda: popupmsg("sell not yet"))

        tradeButton.add_separator()
        tradeButton.add_command(label = "Set up Quick buy",
                                                command = lambda: popupmsg("quick not yet"))

        menubar.add_cascade(label="Trading",menu = tradeButton)


        startStop = tk.Menu(menubar,tearoff = 1)
        
        startStop.add_command(label = "resume",
                                            command = lambda: loadChart('start'))
        startStop.add_command(label = "pause",
                                            command = lambda: loadChart('stop'))
        menubar.add_cascade(label = "Resume/Pause client",menu = startStop)

        helpmenu = tk.Menu(menubar,tearoff=1)
        helpmenu.add_command(label = "Tutorial",command = tutorial)
        menubar.add_cascade(label = "HELP",menu=helpmenu)


        
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

        label1 = tk.Label(self,text="").grid(column=0, row=1)
        label2 = tk.Label(self,text="手臂X").grid(column=0, row=2)
        label3 = tk.Label(self,text="").grid(column=0, row=3)
        label4 = tk.Label(self,text="手臂Y").grid(column=0, row=4)
        label5 = tk.Label(self,text="").grid(column=0, row=5)
        label6 = tk.Label(self,text="手臂Z").grid(column=0, row=6)


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


            e=x/1000
            r=y/1000
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


            e=x/1000
            r=y/1000
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
app.geometry("1280x720")
#ani = animation.FuncAnimation(f,animate,interval = 5000)
app.mainloop()



