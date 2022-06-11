def MyFunction(self):
    text = "Этот текст должен быть в окне приложение, а не консоли"
    print(text)
    self.ui.text_print.setText(text)