'''
Created on 2018 M12 1

@author: brian
''' 
#imports needed methods from libraries

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.uix.button import Button
from win10toast import ToastNotifier
from datetime import datetime
AppName = ("Hack Your Health")
#sets background colour to dark grey
Window.clearcolor = (.2, .2, .2, 1) 

class Health(GridLayout):
    
     
    def __init__(self, **kwargs):
        from kivy.clock import Clock
        from functools import partial
        #constructor calls the super class and names it health
        super(Health, self).__init__(**kwargs)
        
        def on_checkbox_active(checkbox, value):
            if value:
                print('The checkbox', checkbox, 'is active')
            else:
                print('The checkbox', checkbox, 'is inactive')
        
        def update(dt):
            
            def Pomodoro():
                global PomTime
                global PomStatus
                global PomCount
                if PomStatus == 0:
                    
                    if CurrentTime == PomTime and PomCount != 4:
                        PomNotifier.show_toast(AppName, "Take a Short Break!")
                        PomStatus = 1
                        PomSet(ShortBreak)
                    elif CurrentTime == PomTime and PomCount == 4:
                        PomNotifier.show_toast(AppName, "Take a Long Break!")
                        PomSet(ShortBreak)
                else:
                    if CurrentTime == PomTime and PomCount != 4:
                        PomNotifier.show_toast(AppName, "Time to Work!")
                        PomStatus = 0
                        PomCount += 1
                        PomSet(PomInterval)
                    elif CurrentTime == PomTime and PomCount == 4:
                        PomNotifier.show_toast(AppName, "Time to Work!")
                        PomStatus = 0
                        PomCount = 0
                        PomSet(PomInterval)
                        
            def PomSet(PomIncrease):
                global PomTime
                
                PomTime = [PomTime[0], PomTime[1] + PomIncrease]
                if PomTime[1] > 59:
                    PomTime[1] = PomTime[1] - 60
                    PomTime[0] += 1
                if PomTime[0] > 24:
                    PomTime[0] = PomTime[0] - 24

            def TimerReset(Timer,TimeInterval):
                CurrentTime = [datetime.now().time().hour,datetime.now().time().minute]
                Timer = [CurrentTime[0] + TimeInterval[0],CurrentTime[1] + TimeInterval[1]]
                if Timer[1] > 59:
                    Timer[1] = Timer[1] - 60
                    Timer[0] += 1
                if Timer[0] > 24:
                    Timer[0] = Timer[0] - 24
                return Timer

            def NotifyAtTime(Time, ToastVar, ToastText, TimeInterval):
                if Time[0] == datetime.now().time().hour and Time[1] == datetime.now().time().minute :
                    print("Drink Water!")
                    ToastVar.show_toast(AppName, ToastText)
                    
                    Time = TimerReset(Time,TimeInterval)
                    
                    return Time
                return Time
            global Water
            global Breakfast
            global Lunch
            global Dinner
            global StandUp
            global LookAtSpot
            
            global CurrentTime
            
            global WaterInterval
            global WaterTime
            global WaterSet

            global FoodSet
            global BreakfastTime
            global LunchTime
            global DinnerTime

            global StandUpInterval
            global StandUpTime

            global LookAtInterval
            global LookAtTime

            global PomTime
            global PomInterval
            global ShortBreak
            global LongBreak
            global PomCount
            global PomStatus

            global WebsiteList
            global hosts_file
            global redirect

            global workTime
            global blockOn
            PomSet(PomInterval)
            CurrentTime = [datetime.now().time().hour,datetime.now().time().minute]
            if Health().CheckWater:
                WaterTime = NotifyAtTime(WaterTime, Water, "Drink Water", WaterInterval)
            if Health().CheckFood:
                BreakfastTime = NotifyAtTime(BreakfastTime, Breakfast, "Eat Breakfast", [0,1])
                LunchTime = NotifyAtTime(LunchTime, Lunch, "Eat Lunch", [0,-1])
                DinnerTime = NotifyAtTime(DinnerTime, Dinner, "Eat Dinner", [0,-1])
            if Health().CheckStretch: 
                StandUpTime = NotifyAtTime(StandUpTime, StandUp, "Stand Up and Stretch", StandUpInterval)
            if Health().CheckRest:
                LookAtTime = NotifyAtTime(LookAtTime, LookAtSpot, "Look at a Spot 20ft Away for 20 Minutes", LookAtInterval)
                
            Pomodoro()
            try:
                if blockOn == False:
                    print("Yee")
            except NameError:
                blockOn = False
            if PomStatus == 0 and blockOn == True:
                f = open(hosts_file, mode = 'a+')
                content=f.read()
                i = 0
                f.seek(22,0)
                for website in website_list:
                    f.write(redirect+" "+ website + "\n")
                    print("Written Line")
                blockOn = True
                f.close()
                print("Closed File")
                     
            if PomStatus == 1 and blockOn == False:
                with open(hosts_file,'r+') as f:
                    content=f.readlines()
                    f.seek(0)
                    for line in content:
                        if not any(website in line for website in website_list):
                            f.write(line)
                      
                    f.truncate()
                    blockOn = False
                    f.close()
                    print("Closed File")
        
        Clock.schedule_interval(update, 20)
        #first layout of buttons and labels for the alert tab
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        
        self.CheckWater = CheckBox(active=False)
        self.CheckWater.bind(active=on_checkbox_active)
        layout.add_widget(self.CheckWater)
        layout.add_widget(Label(text = "Water"))
        
        self.CheckFood = CheckBox()
        self.CheckFood.bind(active=on_checkbox_active)
        layout.add_widget(self.CheckFood)
        layout.add_widget(Label(text = "Food (Enter in Hours:Minutes)"))
        
        layout.add_widget(Label(text = "Breakfast"))
        self.breakfast = TextInput(multiline=False)
        layout.add_widget(self.breakfast)
        layout.add_widget(Label(text = "Lunch"))
        self.lunch = TextInput(multiline=False)
        layout.add_widget(self.lunch)
        layout.add_widget(Label(text = "Dinner"))
        self.dinner = TextInput(multiline=False)
        layout.add_widget(self.dinner)
        
        self.CheckStretch = CheckBox(active = False)
        self.CheckStretch.bind(active=on_checkbox_active)
        layout.add_widget(self.CheckStretch)
        layout.add_widget(Label(text = "Standup/stretch"))

        self.CheckRest = CheckBox(active = False)
        self.CheckRest.bind(active=on_checkbox_active)
        layout.add_widget(self.CheckRest)
        layout.add_widget(Label(text = "Rest your eyes"))
        layout.add_widget(Label())
       
        
        #adding the first layout to the Title Alert
        layout2 = GridLayout(rows=2, row_force_default=True, row_default_height=40)
        layout2.add_widget(Label(text = "Alerts", font_size = 50, bold = True, shorten = True))
        layout2.add_widget(layout)
       
    
        #3rd grid has the layout of the buttons and labels for the work tab
        layout3 = GridLayout(cols=2, row_force_default=True, row_default_height=40)
##        self.CheckBlock = CheckBox(active = False)
##        self.CheckBlock.bind(active=on_checkbox_active)
        layout3.add_widget(Label(text = "Blocked Websites (seperated by comma)"))
        self.blocked = TextInput(multiline = False)
        layout3.add_widget(self.blocked)
        layout3.add_widget(Label(text = "Start Timer! (Enter in Hours:Minutes)"))
        self.timer = TextInput(multiline = False)
        layout3.add_widget(self.timer)
        layout3.add_widget(Label(text = "short break"))
        self.short = TextInput(multiline = False)
        layout3.add_widget(self.short)
        layout3.add_widget(Label(text = "long break"))
        self.long = TextInput(multiline = False)
        layout3.add_widget(self.long)
        
        
        #piecing all the components to one frame
        self.rows = 5
        self.add_widget(layout2)
        self.add_widget(Label())
        self.add_widget(Label(text = "Work", font_size = 50, bold = True, shorten = True))
        self.add_widget(layout3)
       

        
        
    
class HealthApp(App):
    #health App class takes App component and calls Health() function from build
    def build(self):
        
    
        return Health()

    
        
                
if __name__ == '__main__':
    Water = ToastNotifier()
    Breakfast = ToastNotifier()
    Lunch = ToastNotifier()
    Dinner = ToastNotifier()
    StandUp = ToastNotifier()
    LookAtSpot = ToastNotifier()

    CurrentTime = [datetime.now().time().hour,datetime.now().time().minute]


    WaterInterval = [0,30]
    WaterTime = [CurrentTime[0] + WaterInterval[0],CurrentTime[1] + WaterInterval[1]]
    if WaterTime[1] > 59:
        WaterTime[1] = WaterTime[1] - 60
        WaterTime[0] += 1
    if WaterTime[0] > 24:
        WaterTime[0] = WaterTime[0] - 24
    print(WaterTime)
    WaterSet = False

    BreakfastTimeInput = "7:00"
    BreakfastTime = [0,0]
    BreakfastTime[0] = int(BreakfastTimeInput.split(":")[0])
    BreakfastTime[1] = int(BreakfastTimeInput.split(":")[1])
    BreakfastSet = False

    LunchTimeInput = "12:00"
    LunchTime = [0,0]
    LunchTime[0] = int(LunchTimeInput.split(":")[0])
    LunchTime[1] = int(LunchTimeInput.split(":")[1])
    LunchSet = False

    DinnerTimeInput = "19:00"
    DinnerTime = [0,0]
    DinnerTime[0] = int(DinnerTimeInput.split(":")[0])
    DinnerTime[1] = int(DinnerTimeInput.split(":")[1])
    DinnerSet = False

    StandUpInterval = [0,15]
    StandUpTime = [CurrentTime[0] + StandUpInterval[0], CurrentTime[1] + StandUpInterval[1]]
    if StandUpTime[1] > 59:
        StandUpTime[1] = StandUpTime[1] - 60
        StandUpTime[0] += 1
    if StandUpTime[0] > 24:
        StandUpTime[0] = StandUpTime[0] - 24
    StandUpSet = False

    LookAtInterval = [0,20]
    LookAtTime = [CurrentTime[0], CurrentTime[1] + 20]
    if LookAtTime[1] > 59:
        LookAtTime[1] = LookAtTime[1] - 60
        LookAtTime[0] += 1
    if LookAtTime[0] > 24:
        LookAtTime[0] = LookAtTime[0] - 24
    LookAtSet = False

    PomTime = [0,0]
    PomTime = [datetime.now().time().hour,datetime.now().time().minute]
    PomInterval = 1
    ShortBreak = 2
    LongBreak = 5
    PomCount = 0
    PomStatus = 0

    PomNotifier = ToastNotifier()

    website_list=["facebook.com","www.facebook.com","twitter.com","www.twitter.com"]
    hosts_file = r"C:\Windows\System32\Drivers\etc\hosts"
    redirect = "172.217.10.238"

    workTime = True
    blockOn = True
    HealthApp().run() 
    
