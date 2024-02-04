import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(452, 36, 900, 650)

        rectangle = ShadowRectangle()
        rectangle.setGeometry(2, 5, 100, 400)
        self.setCentralWidget(rectangle)


class ShadowRectangle(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Rectangle avec effet de drop shadow')

        container_widget = QWidget()
        container_widget.setStyleSheet('background-color: blue; border-radius: 13px')
        container_layout = QHBoxLayout()
        container_widget.setLayout(container_layout)

        for i in range(4):
            button = QPushButton(str(i + 1))
            button.setStyleSheet('background-color: red; border-radius:3px')
            container_layout.addWidget(button)

        # Créer un effet d'ombre portée pour le rectangle
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(5, 5)
        self.setGraphicsEffect(shadow)

        main_layout = QVBoxLayout()
        main_layout.addWidget(container_widget)
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
