from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from tools import new_id
from display import MainDisplay
from menu import NavBar


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #  self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.main_widget = QWidget(self)
        self.main_widget.setStyleSheet('background-color: blue')
        self.setCentralWidget(self.main_widget)

        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        

        self.menu = NavBar()
        self.display = MainDisplay()
        
        #  Connect Button from TopBar to Action
        self.menu.top.back.clicked.connect(self.display.browser.back)
        self.menu.top.forward.clicked.connect(self.display.browser.forward)
        self.menu.top.home.clicked.connect(self.display.toggleFrame)
        self.menu.top.new.clicked.connect(lambda: self.display.go_site('google'))
        
        #  Connect Button from ShortCut to Action
        self.menu.shortcut.netflix.clicked.connect(lambda: self.display.go_site('netflix'))
        self.menu.shortcut.google.clicked.connect(lambda: self.display.go_site('google'))
        self.menu.shortcut.discord.clicked.connect(lambda: self.display.go_site('discord'))
        self.menu.shortcut.twitter.clicked.connect(lambda: self.display.go_site('twitter'))
        self.menu.shortcut.youtube.clicked.connect(lambda: self.display.go_site('youtube'))
        self.menu.shortcut.github.clicked.connect(lambda: self.display.go_site('github'))

        self.new_tab()

        #  Connect Button from UrlBar to Action
        self.menu.url.returnPressed.connect(self.search)

        self.main_layout.addWidget(self.menu, 0)
        self.main_layout.addWidget(self.display, 2)

        self.display.browser.urlChanged.connect(self.update_url)

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Left:    
            
            self.main_layout.removeWidget(self.menu)
            self.menu.hide()
            self.main_layout.setStretch(0, 0)  # Reduce the size of NavBar
            self.main_layout.setStretch(2, 1)  # Expand the size of MainDisplay
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Right:
            
            #  self.main_layout.addWidget(self.menu, 0)
            self.main_layout.insertWidget(0, self.menu)
            self.menu.show()
            self.main_layout.setStretch(0, 1)  # Expand the size of NavBar
            self.main_layout.setStretch(2, 2)  # Reduce the size of MainDisplay
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_R:
            self.display.browser.reload()
    
    def search(self):
        self.display.browser.setUrl(QUrl(self.menu.url.text()))
        
    def update_url(self, url):
        self.menu.url.setText(url.toString())

    def new_tab(self):
        tab_id = new_id()
        self.display.new_web_window(tab_id)
        self.menu.tab.new_button_tab(tab_id)
