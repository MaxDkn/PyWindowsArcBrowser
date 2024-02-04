import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *


class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        
        self.new_tab_button = QPushButton("Nouvel onglet")
        self.tab_counter = 1

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        central_widget.setStyleSheet('background-color: red')
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.new_tab_button)
        layout.addWidget(self.tabs)

        self.setCentralWidget(central_widget)
        self.setWindowTitle("Navigateur Web")

        self.new_tab_button.clicked.connect(self.add_new_tab)

    def add_new_tab(self):
        new_tab = QWidget()
        new_tab.setStyleSheet('background-color: blue')
        tab_layout = QVBoxLayout(new_tab)
        tab_layout.setContentsMargins(0, 0, 0, 0)

        url_input = QLineEdit()
        url_input.setPlaceholderText("Entrez l'URL ici et appuyez sur Entrée")
        url_input.returnPressed.connect(lambda: self.load_url(url_input, new_tab))

        webview = QWebEngineView()

        tab_layout.addWidget(url_input)
        tab_layout.addWidget(webview)
        new_tab.setLayout(tab_layout)

        self.tabs.addTab(new_tab, f"Onglet {self.tab_counter}")
        self.tab_counter += 1

    def load_url(self, url_input, tab):
        url = url_input.text()
        index = self.tabs.indexOf(tab)
        if index != -1:
            webview = self.tabs.widget(index).findChild(QWebEngineView)
            if webview:
                webview.setUrl(QUrl(url))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.show()
    sys.exit(app.exec_())
