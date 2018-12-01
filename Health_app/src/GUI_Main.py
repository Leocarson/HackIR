'''
Created on 2018 M12 1

@author: brian
''' 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.uix.button import Button


Window.clearcolor = (.2, .2, .2, 1) #sets background colour to dark grey
class Health(GridLayout):
    def __init__(self, **kwargs):
        super(Health, self).__init__(**kwargs)
        
        
        
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        layout.add_widget(CheckBox(active = False))
        layout.add_widget(Label(text = "Water"))
        layout.add_widget(CheckBox(active = False))
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
        layout.add_widget(CheckBox(active = False))
        layout.add_widget(Label(text = "Standup/stretch"))
        layout.add_widget(CheckBox(active = False))
        layout.add_widget(Label(text = "Rest your eyes"))
        layout.add_widget(Label())
       

        layout2 = GridLayout(rows=2, row_force_default=True, row_default_height=40)
        layout2.add_widget(Label(text = "Alerts", font_size = 50, bold = True, shorten = True))
        layout2.add_widget(layout)
       
        layout3 = GridLayout(cols=2, row_force_default=True, row_default_height=40) 
        layout3.add_widget(Label(text = "Blocked Websites (seperated by comma)"))
        self.blocked = TextInput(multiline = False)
        layout3.add_widget(self.blocked)
        layout3.add_widget(Button(text = "Start Timer! (Enter in Hours:Minutes)"))
        self.timer = TextInput(multiline = False)
        layout3.add_widget(self.timer)
        layout3.add_widget(Label(text = "short break"))
        self.short = TextInput(multiline = False)
        layout3.add_widget(self.short)
        layout3.add_widget(Label(text = "long break"))
        self.long = TextInput(multiline = False)
        layout3.add_widget(self.long)
        
        self.rows = 5
        self.add_widget(layout2)
        self.add_widget(Label())
        self.add_widget(Label(text = "Work", font_size = 50, bold = True, shorten = True))
        self.add_widget(layout3)
        
        
        
    
class HealthApp(App):
    
    def build(self):
        return Health()

if __name__ == '__main__':

    HealthApp().run() 