from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager,Screen
import instructions

all_results = dict()

class NewApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(NewScreen(name = 'window'))
        sm.add_widget(SecondScreeen(name = 'second_window'))
        sm.add_widget(TheerdScreeen(name = 'theerd_window'))
        sm.add_widget(ForthScreen(name = 'forth_window'))
        sm.add_widget(FivethScreen(name = 'fiveth_window'))
        return sm
class NewScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation = 'vertical')
        self.new_button = Button(text = 'начать',height = "80px",size_hint = (1, None))  
        label = Label(text = instructions.txt_instruction)
        self.text_name = TextInput(hint_text = 'Введите имя', size_hint = (1, None), height = "50px", multiline = False)
        self.text_age = TextInput(hint_text = 'Введите возраст', size_hint = (1, None), height = "50px", multiline = False)
        self.add_widget(layout)
        layout.add_widget(label)
        layout.add_widget(self.text_name)
        layout.add_widget(self.text_age)
        layout.add_widget(self.new_button)
        self.new_button.on_press = self.switch 
    
    def switch(self):
        try: 
            self.result = int(self.text_age.text)
            all_results['age_result'] = self.result
            self.manager.current = 'second_window'
        except ValueError:
            self.text_age.hint_text = 'Здесь можно вводить только цифры'

    

class SecondScreeen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        second_layout = BoxLayout(orientation = 'vertical')
        second_label = Label(text = instructions.txt_test1)
        self.second_button = Button(text = 'продолжить',height = "80px",size_hint = (1, None))
        self.text_result = TextInput(hint_text = 'Введите результат', size_hint = (1, None), height = "50px", multiline = False)
        self.add_widget(second_layout)
        second_layout.add_widget(second_label)
        second_layout.add_widget(self.text_result)
        second_layout.add_widget(self.second_button)
        self.second_button.on_press = self.switch 
    def switch(self):
        try:
            self.text_result = int(self.text_result.text)
            all_results['first_results'] = self.text_result 
            self.manager.current = 'theerd_window'
        except ValueError:
            self.text_result.hint_text = 'Здесь можно вводить только цифры'
           



    

class TheerdScreeen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        theerd_layout = BoxLayout(orientation = 'vertical')
        theerd_label = Label(text = instructions.txt_test2)
        self.theerd_button = Button(text = 'продолжить',height = "80px",size_hint = (1, None))
        self.add_widget(theerd_layout)
        theerd_layout.add_widget(theerd_label)
        theerd_layout.add_widget(self.theerd_button)
        self.theerd_button.on_press = self.switch 
    def switch(self):
        self.manager.current = 'forth_window'
        

class ForthScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        forth_layout = BoxLayout(orientation = 'vertical')
        self.forth_button = Button(text = 'завершить',height = "80px",size_hint = (1, None))  
        forth_label = Label(text = instructions.txt_test3)
        self.text_old_result = TextInput(hint_text = 'Результат', size_hint = (1, None), height = "50px", multiline = False)
        self.text_new_result = TextInput(hint_text = 'Результат после отдыха', size_hint = (1, None), height = "50px", multiline = False)
        self.add_widget(forth_layout)
        forth_layout.add_widget(forth_label)
        forth_layout.add_widget(self.text_old_result)
        forth_layout.add_widget(self.text_new_result)
        forth_layout.add_widget(self.forth_button)
        self.forth_button.on_press = self.switch 
    def switch(self):
        try:
            self.text_new_result = int(self.text_new_result.text)
            self.text_old_result = int(self.text_old_result.text)
            all_results['new_second_results'] = self.text_new_result
            all_results['old_second_results'] = self.text_old_result
            self.manager.current = 'fiveth_window'
        except ValueError:
            self.text_old_result.hint_text = 'Здесь можно вводить только цифры'
            self.text_new_result.hint_text = 'Здесь можно вводить только цифры'

class FivethScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        fiveth_layout = BoxLayout(orientation = 'vertical')
        self.add_widget(fiveth_layout)



        

       

app = NewApp()
app.run()