from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivymd.app import MDApp

Window.size=(480,800)
class MainInterface(RelativeLayout):
    pass

class TextAnalyzerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        return 0
        # return super().build()

TextAnalyzerApp().run()