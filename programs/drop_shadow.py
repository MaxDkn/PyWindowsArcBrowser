
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

class ShadowRectangleExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Exemple de rectangle avec effet de drop shadow')
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        shadow_widget = ShadowWidget()
        layout.addWidget(shadow_widget)

        central_widget.setLayout(layout)

        self.show()

class ShadowWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(40)
        shadow_effect.setColor(QColor(0, 0, 0, 150))
        shadow_effect.setOffset(5, 5)

        self.setGraphicsEffect(shadow_effect)

        inner_widget = QWidget()
        self.layout.addWidget(inner_widget)

        inner_layout = QVBoxLayout()
        inner_widget.setLayout(inner_layout)

        # Boutons à l'intérieur du rectangle
        button_layout = QHBoxLayout()
        inner_layout.addLayout(button_layout)

        button1 = QPushButton('Bouton 1')
        button1.setStyleSheet('color: red')

        button2 = QPushButton('Bouton 2')
        button3 = QPushButton('Bouton 3')
        button4 = QPushButton('Bouton 4')

        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)
        button_layout.addWidget(button4)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShadowRectangleExample()
    sys.exit(app.exec_())
"""


'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ImageButton(QPushButton):
    def __init__(self, path):
        super().__init__()

        button = QPushButton(self)
        icon = QIcon(path)
        button.setIcon(icon)
        #  image_button.setIconSize(pixmap.size())

      

class ImageButtonExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Exemple de bouton avec image')
        self.setGeometry(100, 100, 300, 200)

        image_button = QPushButton(self)
        pixmap = QIcon('ressources/icon/TopBar/Back.png')
        image_button.setIcon(pixmap)
        #  image_button.setIconSize(pixmap.size())

        self.setCentralWidget(image_button)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageButtonExample()
    sys.exit(app.exec_())
'''