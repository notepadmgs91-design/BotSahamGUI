from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        return Label(text='MT5 Copier Dashboard')

if __name__ == '__main__':
    MainApp().run()
