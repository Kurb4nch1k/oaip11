class Widget:
    def __init__(self, name):
        self.name = name

    def display(self):
        pass

class Label(Widget):
    def __init__(self, name, text):
        super().__init__(name)
        self.text = text

    def display(self):
        print(f'Label: {self.name}, Text: {self.text}')

class LineEdit(Widget):
    def __init__(self, name, placeholder_text):
        super().__init__(name)
        self.placeholder_text = placeholder_text

    def display(self):
        print(f'LineEdit: {self.name}, Placeholder Text: {self.placeholder_text}')

class TextEdit(Widget):
    def __init__(self, name, text):
        super().__init__(name)
        self.text = text

    def display(self):
        print(f'TextEdit: {self.name}, Text: {self.text}')

class Button(Widget):
    def __init__(self, name, text):
        super().__init__(name)
        self.text = text

    def display(self):
        print(f'Button: {self.name}, Text: {self.text}')

class CheckBox(Widget):
    def __init__(self, name, checked=False):
        super().__init__(name)
        self.checked = checked

    def display(self):
        print(f'CheckBox: {self.name}, Checked: {self.checked}')
