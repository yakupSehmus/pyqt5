import sys

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout


class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.checkbox = QCheckBox("python severmisiniz?")
        self.yazı_alanı = QLabel("")
        self.buton = QPushButton("tıkla")

        v_box = QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.setWindowTitle("checkbox")

        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(), self.yazı_alanı))
        self.show()

    def click(self, checkbox, yazı_alanı):
        if checkbox:
            yazı_alanı.setText("pythonu seviyorsun")

        else:
            yazı_alanı.setText("niye sevmiyorsun")

app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
