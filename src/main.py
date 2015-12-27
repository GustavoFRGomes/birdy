"""
	This will be the main script to build the GUI and it will also have the
	screen manager.
"""
from kivy.app import App
from kivy.ux.floatinglayout import FloatingLayout

class MainApp(FloatingLayout):
	def build(self):
		return 