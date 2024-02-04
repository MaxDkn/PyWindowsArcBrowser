from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#  from drop_shadow import drop_shadow



class NavBar(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #D9D9D9;')
        self.setMinimumSize(200, 200)
        self.setMaximumWidth(300)

        self.layout = QVBoxLayout()
        
        self.top = TopBar()
        self.layout.addWidget(self.top, 0)
        
        self.shortcut = Shortcut()
        self.layout.addWidget(self.shortcut, 0)
        
        self.tab = VerticalTab()
        self.layout.addWidget(self.tab, 2)    
        
        self.url = UrlBar()
        self.layout.addWidget(self.url, 0)
        
        self.setLayout(self.layout)


class TopBar(QFrame):
    def __init__(self):
        super().__init__()
        #  button = QPushButton('Bouton stylisé', self)
        #  button.setGeometry(50, 50, 150, 30)
        self.setStyleSheet('background-color: red')
        self.layout = QHBoxLayout()

        self.back = QPushButton('<')
        self.back.setStyleSheet('background-color: green')
        self.forward = QPushButton('>')
        self.forward.setStyleSheet('background-color: green')
        self.home = QPushButton('🏠')
        self.home.setStyleSheet('background-color: green')
        self.new = QPushButton('+')
        self.new.setStyleSheet('background-color: green')
        
        self.layout.addWidget(self.back)
        self.layout.addWidget(self.forward)
        self.layout.addWidget(self.home)
        self.layout.addWidget(self.new)
        self.setFixedHeight(40)

        self.setLayout(self.layout)


class Shortcut(QFrame):
    def __init__(self):
        super().__init__()
        #  button = QPushButton('Bouton stylisé', self)
        #  button.setGeometry(50, 50, 150, 30)
        #  button.setStyleSheet('background-color: blue; color: white;')
        self.setStyleSheet('background-color: blue')
        self.layout = QGridLayout()

        self.netflix = QPushButton('1')
        self.netflix.setStyleSheet('background-color: green')
        #  self.netflix.setGraphicsEffect(drop_shadow())
        self.google = QPushButton('2')
        self.google.setStyleSheet('background-color: green')
        #  self.google.setGraphicsEffect(drop_shadow())
        self.discord = QPushButton('3')
        self.discord.setStyleSheet('background-color: green')
        #  self.discord.setGraphicsEffect(drop_shadow())
        self.twitter = QPushButton('4')
        self.twitter.setStyleSheet('background-color: green')
        #  self.twitter.setGraphicsEffect(drop_shadow())
        self.youtube = QPushButton('5')
        self.youtube.setStyleSheet('background-color: green')
        #  self.youtube.setGraphicsEffect(drop_shadow())
        self.github = QPushButton('6')
        self.github.setStyleSheet('background-color: green')
        #  self.github.setGraphicsEffect(drop_shadow())

        self.layout.addWidget(self.netflix, 0, 0)
        self.layout.addWidget(self.google, 0, 1)
        self.layout.addWidget(self.discord, 0, 2)
        self.layout.addWidget(self.twitter, 1, 0)
        self.layout.addWidget(self.youtube, 1, 1)
        self.layout.addWidget(self.github, 1, 2)

        self.setLayout(self.layout)


class ShortCutButton(QPushButton):
    def __init__(self, destination):
        self.icon = QIcon(rf'./ressources/icon/{destination}.png')
        self.icon = self.icon.pixmap(40, 40)
        self.setIcon(self.icon)
    

class VerticalTab(QWidget):
    def __init__(self):
        super().__init__()
        scroll_area = QScrollArea()
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)

        self.scroll_layout = QVBoxLayout(scroll_widget)


        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

        self.scroll_area = scroll_area

    def new_button_tab(self, id):
        button = TabButton(id)
        self.scroll_layout.addWidget(button, 0)

    def remove_tab(self, tab):
        pass
    '''
    def eventFilter(self, obj, event):
        if event.type() == Qt.MouseMove:
            if obj == self.scroll_area.viewport():
                delta = event.angleDelta().y()
                v_bar = self.scroll_area.verticalScrollBar()
                v_bar.setValue(v_bar.value() - delta)
                return True
        return super().eventFilter(obj, event)
    '''

class TabButton(QPushButton):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.setText('Nouvel Onglet')
        self.setStyleSheet('color: yellow; background-color: red')
        #  self.setFlat(True)


class UrlBar(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: black; color: white; border-radius: 2px;')
        self.setPlaceholderText("Enter web address")
