import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.browser = QWebEngineView()

        self.browser.setUrl(QUrl('https://youtube.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        navbar = QToolBar()
        self.addToolBar(navbar)

        return_btn = QAction('Retour', self)
        return_btn.triggered.connect(self.browser.back)
        navbar.addAction(return_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigation)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigation(self):
        url = self.url_bar.text()
        self.navigation.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())
    
        
app = QApplication(sys.argv)
QApplication.setApplicationName('GoAngelBrowser')
window = MainWindow()
app.exec()