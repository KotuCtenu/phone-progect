from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen

class NewApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(NewScreen(name = 'window'))
        sm.add_widget(One_Bscreen(name = 'second_window'))
        return sm
class NewScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.button = Button(text = "кнопка")
        second_button = Button(text = "кнoпкa№2")
        layout = BoxLayout(orientation = 'vertical')
        layout.add_widget(self.button)
        layout.add_widget(second_button)
        self.add_widget(layout)
        self.button.on_press = self.switch 
        second_button.on_press = self.switch 
    def switch(self):
        self.manager.current = 'second_window'
        self.button.text = 'уже не та кнопка'


class One_Bscreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        button = Button(text = "кнопка")
        layout = BoxLayout()
        layout.add_widget(button)
        self.add_widget(layout)
        button.on_press = self.switch 
    def switch(self):
        self.manager.current = 'window'



app = NewApp()
app.run()