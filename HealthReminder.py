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


WaterInterval = [0,1]
WaterTime = [CurrentTime[0] + WaterInterval[0],CurrentTime[1] + WaterInterval[1]]
if WaterTime[1] > 59:
    WaterTime[1] = WaterTime[1] - 60
    WaterTime[0] += 1
if WaterTime[0] > 24:
    WaterTime[0] = WaterTime[0] - 24
print(WaterTime)
WaterSet = True

FoodSet = False
BreakfastTimeInput = input("Input what time you eat Breakfast (24-hour): ")
BreakfastTime = [0,0]
BreakfastTime[0] = int(BreakfastTimeInput.split(":")[0])
BreakfastTime[1] = int(BreakfastTimeInput.split(":")[1])


LunchTimeInput = input("Input what time you eat Lunch (24-hour): ")
LunchTime = [0,0]
LunchTime[0] = int(LunchTimeInput.split(":")[0])
LunchTime[1] = int(LunchTimeInput.split(":")[1])


DinnerTimeInput = input("Input what time you eat Dinner (24-Hour): ")
DinnerTime = [0,0]
DinnerTime[0] = int(DinnerTimeInput.split(":")[0])
DinnerTime[1] = int(DinnerTimeInput.split(":")[1])


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

PomTime = [datetime.now().time().hour,datetime.now().time().minute]
PomInterval = 25
ShortBreak = 5
LongBreak = 20
PomCount = 0
PomStatus = 0

PomNotifier = ToastNotifier()

website_list=["facebook.com","www.facebook.com","twitter.com","www.twitter.com"]
hosts_file = r"C:\Windows\System32\Drivers\etc\hosts"
redirect = "172.217.10.238"

workTime = True
blockOn = False
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
        ToastVar.show_toast(AppName, ToastText)
        
        Time = TimerReset(Time,TimeInterval)
        
        return Time
    return Time
PomSet(PomInterval)



while True:
    CurrentTime = [datetime.now().time().hour,datetime.now().time().minute]
    if WaterSet:
        WaterTime = NotifyAtTime(WaterTime, Water, "Drink Water", WaterInterval)
    if FoodSet:
        BreakfastTime = NotifyAtTime(BreakfastTime, Breakfast, "Eat Breakfast", [0,1])
        LunchTime = NotifyAtTime(LunchTime, Lunch, "Eat Lunch", [0,-1])
        DinnerTime = NotifyAtTime(DinnerTime, Dinner, "Eat Dinner", [0,-1])
    if StandUpSet:
        StandUpTime = NotifyAtTime(StandUpTime, StandUp, "Stand Up and Stretch", StandUpInterval)
    if LookAtSet:
        LookAtTime = NotifyAtTime(LookAtTime, LookAtSpot, "Look at a Spot 20ft Away for 20 Minutes", LookAtInterval)
    
    Pomodoro()
    
    if PomStatus == 0 and blockOn != True:
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
                
    if PomStatus == 1 and blockOn == True:
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




