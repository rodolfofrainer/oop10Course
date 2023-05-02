from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests
import os

Builder.load_file('frontend.kv')


class MainScreen(Screen):
    def get_image_link(self):
        # get user query from text input field
        query = self.manager.current_screen.ids.user_query.text
        # get wikipedia page and first image link
        page = wikipedia.page(query, auto_suggest=False)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        # download image
        req = requests.get(self.get_image_link())
        filepath = 'images/image.jpeg'
        with open(filepath, 'wb') as file:
            file.write(req.content)

    def set_image(self):
        # set image in image widget
        self.manager.current_screen.ids.img.source = self.download_image()
        self.manager.current_screen.ids.img.reload()


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
