import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFrame

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Changement de cadre')
        self.setGeometry(100, 100, 400, 300)

        # Création des cadres
        self.blue_frame = QFrame(self)
        self.blue_frame.setStyleSheet("background-color: blue;")
        self.red_frame = QFrame(self)
        self.red_frame.setStyleSheet("background-color: red;")

        # Cadre actif initial
        self.current_frame = self.blue_frame

        # Création du bouton de basculement
        self.toggle_button = QPushButton('Basculer de cadre', self)
        self.toggle_button.clicked.connect(self.toggleFrame)

        # Mise en page avec QVBoxLayout
        layout = QVBoxLayout()
        layout.addWidget(self.toggle_button)
        layout.addWidget(self.blue_frame)
        layout.addWidget(self.red_frame)
        self.toggleFrame()
        self.setLayout(layout)

    def toggleFrame(self):
        # Basculement entre les cadres
        if self.current_frame == self.blue_frame:
            self.current_frame = self.red_frame
        else:
            self.current_frame = self.blue_frame

        # Affichage du cadre actif
        self.blue_frame.setVisible(self.current_frame == self.blue_frame)
        self.red_frame.setVisible(self.current_frame == self.red_frame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
