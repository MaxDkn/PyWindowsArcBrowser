import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt

class UrlBar(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: black; color: white; border-radius: 2px;')
        self.setPlaceholderText("Enter web address")
        self.clicked_once = False

    def mousePressEvent(self, event):
        if not self.clicked_once:
            self.selectAll()
            self.clicked_once = True

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Barre d\'URL avec sélection automatique')
        self.setGeometry(100, 100, 400, 100)

        # Créez une barre d'URL personnalisée
        self.url_bar = UrlBar()

        # Mise en page avec QVBoxLayout
        layout = QVBoxLayout()
        layout.addWidget(self.url_bar)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
