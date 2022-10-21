from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
from kivy.config import Config

Config.set('graphics', 'resizable', 0)

Window.size = (400, 500)
Window.clearcolor = (30/255, 30/255, 30/255, 1)
Window.title = "Calculator"

class MyApp(App):
	def update_label(self):
		self.label.text = self.formula

	def btn_pressed(self, instance):
		if(self.formula == "0"):
			self.formula = ""
		self.formula += str(instance.text)
		self.update_label()

	def add_operation(self, instance):
		if (str(instance.text).lower() == "x"):
			self.formula += "*"
		else:
			self.formula += str(instance.text)

		self.update_label()

	def res_pressed(self, instance):
		self.label.text = str(eval(self.label.text))
		self.formula = "0"

	def build(self):
		self.formula = "0"
		self.label = Label(text = "0", halign = "right", valign = "center", size_hint = (1, .4), font_size = 40, text_size = (400 - 50, 500 * .4 - 50))
		btn1 = Button(text = "1", on_press = self.btn_pressed)
		btn2 = Button(text = "2", on_press = self.btn_pressed)
		btn3 = Button(text = "3", on_press = self.btn_pressed)
		btn4 = Button(text = "4", on_press = self.btn_pressed)
		btn5 = Button(text = "5", on_press = self.btn_pressed)
		btn6 = Button(text = "6", on_press = self.btn_pressed)
		btn7 = Button(text = "7", on_press = self.btn_pressed)
		btn8 = Button(text = "8", on_press = self.btn_pressed)
		btn9 = Button(text = "9", on_press = self.btn_pressed)
		btn0 = Button(text = "0", on_press = self.btn_pressed)
		add = Button(text = "+", on_press = self.add_operation)
		minuse = Button(text = "-", on_press = self.add_operation)
		delite = Button(text = "/", on_press = self.add_operation)
		umnozit = Button(text = "X", on_press = self.add_operation)
		res = Button(text = "=", on_press = self.res_pressed)

		grid = GridLayout(cols = 3, size_hint = (1, .6))
		grid.add_widget(btn1)
		grid.add_widget(btn2)
		grid.add_widget(btn3)
		grid.add_widget(btn4)
		grid.add_widget(btn5)
		grid.add_widget(btn6)
		grid.add_widget(btn7)
		grid.add_widget(btn8)
		grid.add_widget(btn9)
		grid.add_widget(add)
		grid.add_widget(btn0)
		grid.add_widget(minuse)
		grid.add_widget(delite)
		grid.add_widget(res)
		grid.add_widget(umnozit)

		box = BoxLayout(orientation = 'vertical', padding = 2)
		box.add_widget(self.label)
		box.add_widget(grid)

		return box

if __name__ == "__main__":
	MyApp().run()
