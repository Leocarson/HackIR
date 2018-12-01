from win10toast import ToastNotifier
from datetime import datetime

AppName = ("Test App")

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

LookAtTime = [CurrentTime[0], CurrentTime[1] + 20]
if LookAtTime[1] > 59:
    LookAtTime[1] = LookAtTime[1] - 60
    LookAtTime[0] += 1
if LookAtTime[0] > 24:
    LookAtTime[0] = LookAtTime[0] - 24
LookAtSet = False

PomTime = [datetime.now().time().hour,datetime.now().time().minute]
PomInterval = 2
ShortBreak = 2
LongBreak = 5
PomCount = 0
PomStatus = 0

PomNotifier = ToastNotifier()


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
        PomeTime[0] += 1
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

def NotifyAtTime(Time, ToastVar, ToastText, TimeSet, TimeInterval):
    if Time[0] == datetime.now().time().hour and Time[1] == datetime.now().time().minute and TimeSet == False:
        ToastVar.show_toast(AppName, ToastText)
        TimeSet = True
        Time = TimeReset(Time,TimeInterval)
        TimeSet = False
        return TimeSet,Time

PomSet(PomInterval)

while True:
    CurrentTime = [datetime.now().time().hour,datetime.now().time().minute]
    WaterSet, WaterTime = NotifyAtTime(WaterTime, Water, "Drink Water", WaterSet, WaterInterval)
    BreakfastSet, BreakfastTime = NotifyAtTime(BreakfastTime, Breakfast, "Eat Breakfast", BreakfastSet, BreakfastInterval)
    LunchSet, LunchTime = NotifyAtTime(LunchTime, Lunch, "Eat Lunch", LunchSet, LunchInterval)
    DinnerSet, DinnerTime = NotifyAtTime(DinnerTime, Dinner, "Eat Dinner", DinnerSet, DinnerInterval)
    StandUpSet, StandUpTime = NotifyAtTime(StandUpTime, StandUp, "Stand Up and Stretch", StandUpSet, StandUpInterval)
    LookAtSet, LookAtTime = NotifyAtTime(LookAtTime, LookAtSpot, "Look at a Spot 20ft Away for 20 Minutes", LookAtSet, LookAtInterval)
    Pomodoro()
##Water.show_toast(AppName, "Drink Water!")
##Food.show_toast(AppName, "It's Time to Eat " + Meal)
##StandUp.show_toast(AppName, "Stand up and Stretch!")
##LookAtSpot.show_toast(AppName, "Look at a Spot 20ft Away for 20 Seconds")



