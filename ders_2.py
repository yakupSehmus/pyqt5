import sys
from PyQt5 import QtWidgets,QtGui


def pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 ders 2")

    etiket1 = QtWidgets.QLabel(pencere)

    etiket2 = QtWidgets.QLabel(pencere)

    etiket2.setPixmap(QtGui.QPixmap("download.png"))

    etiket1.setText("burası bir yazıdır.")

    etiket1.move(200,35)
    etiket2.move(140,120)

    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())


pencere()