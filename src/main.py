"""
	This will be the main script to build the GUI and it will also have the
	screen manager.
"""
from kivy.app import App
from kivy.uix.floatinglayout import FloatingLayout
from kivy.uix.screenmanager import Screen

class MainApp(FloatingLayout):
	def build(self):
		pass

if __name__ == '__main__':
	MainApp().run()