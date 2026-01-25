from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen

class NewApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(NewScreen(name = 'window'))
        return sm
class NewScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
       

app = NewApp()
app.run()