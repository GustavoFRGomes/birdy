"""
	This will be the main script to build the GUI and it will also have the
	screen manager.
"""
from kivy.app import App
from kivy.uix.floatinglayout import FloatingLayout
from kivy.uix.screenmanager import Screen

from kivy.properties import BooleanProperty

class MenuScreen(Screen):
	fullscreen = BooleanProperty(False)

class MainApp(FloatingLayout):
	def build(self):
		# Add a ScreenManager in the main app to handle all of the transitions
		# as well as all of the screens.
		self.manager = ScreenManager(transition=SlideTransition(duration=.10))

if __name__ == '__main__':
	MainApp().run()