from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    pass


class PasswordManagerApp(App):
    def __init__(self):
        super(PasswordManagerApp, self).__init__()
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(main_screen)

    def build(self):
        return self.screen_manager


if __name__ == '__main__':
    main_screen = MainScreen(name="main")

    password_manager = PasswordManagerApp()
    password_manager.run()
