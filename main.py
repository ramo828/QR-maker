from windows.home import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
import qrcode
import sys
import os


class Pencere(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.but.clicked.connect(self.make_qr)

    def make_qr(self):
        file_name = "output/qr_code.png"
        data = self.inp.text()
        img = qrcode.make(data)
        img.save(file_name)
        resim = QPixmap(file_name).scaled(251, 221)
        if os.path.exists(file_name):
            self.qr.setPixmap(resim)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Pencere()
    window.show()
    sys.exit(app.exec())
