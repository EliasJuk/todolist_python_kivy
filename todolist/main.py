from kivy.app import App
from kivy.uix.button import Button

class HelloWorld(App):
  def build(self):
    return Button(text='Hello World!')

HelloWorld().run()