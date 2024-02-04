import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
#  from drop_shadow import drop_shadow


class MainDisplay(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: black; border-radius: 2px; border: 4px')
        self.setMinimumSize(600, 50)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(1, 1, 1, 1)

        self.browser = WebDisplay('fzefqdz')
        self.homedisplay = HomeDisplay()

        self.current_display = self.browser
        self.browsers = {}
        
        
        #  self.browser.setPage(WebPage(self.browser))

        self.layout.addWidget(self.browser)
        self.layout.addWidget(self.homedisplay)
        self.toggleFrame()
        self.setLayout(self.layout)

    def go_site(self, sitename):
        self.browser.setUrl(QUrl(f'https://www.{sitename}.com'))
        
    def toggleFrame(self):
        if self.current_display == self.browser:
            self.current_display = self.homedisplay
        else:
            self.current_display = self.browser

        self.homedisplay.setVisible(self.current_display == self.homedisplay)
        self.browser.setVisible(self.current_display == self.browser)

    def new_web_window(self, id):
        self.browsers[id] = WebDisplay(id)
    
    def change_actif_browser(self, id):
        self.browser = self.browsers[id]

class WebDisplay(QWebEngineView):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.setStyleSheet('border-radius: 20px; background-color: black')
        self.setUrl(QUrl('https://www.duckduckgo.com'))
        

class HomeDisplay(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('border-radius: 20px; background-color: black')
        
