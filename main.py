
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.expression = ""
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.display = TextInput(
            text="0",
            font_size=45,
            readonly=True,
            halign="right",
            multiline=False,
            size_hint_y=0.25
        )
        layout.add_widget(self.display)

        grid = GridLayout(cols=4, spacing=8)

        buttons = [
            "C", "⌫", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "="
        ]

        for item in buttons:
            btn = Button(text=item, font_size=28)
            btn.bind(on_press=self.press)
            grid.add_widget(btn)

        layout.add_widget(grid)
        return layout

    def press(self, button):
        value = button.text

        if value == "C":
            self.expression = ""
        elif value == "⌫":
            self.expression = self.expression[:-1]
        elif value == "=":
            try:
                result = eval(self.expression)
                self.expression = str(result)
            except Exception:
                self.expression = ""
                self.display.text = "Xato"
                return
        elif value == "%":
            try:
                self.expression = str(float(self.expression) / 100)
            except Exception:
                return
        else:
            if self.expression == "0":
                self.expression = ""
            self.expression += value

        self.display.text = self.expression or "0"


if __name__ == "__main__":
    CalculatorApp().run()
