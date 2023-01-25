from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

import real_time_arabic_kv as arkv

# logger = ""
class MainApp(App):
    def build(self):
        self.text_input = TextInput(text_language='ar', font_name='Arial',multiline=True,halign='center')
        self.text_input.bind(text=self.change_text,cursor=self.change_text)
        return self.text_input

    def change_text(self,vvvv,key,*args):
       self.text_input.text,lgo=arkv.arabi_txt_in(self.text_input.text)
       print(self.text_input.text)
       
    ###################################################################
    

if __name__ == '__main__':
    MainApp().run()
