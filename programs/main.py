from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
import window, sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = window.MyWindow()
    window.setWindowTitle('MBrowser')
    window.setWindowIcon(QIcon(r'./ressources/logo.ico'))
    window.show()
    sys.exit(app.exec_())