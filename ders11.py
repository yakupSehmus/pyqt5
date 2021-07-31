import sys

from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow

class Menu(QMainWindow):

    def __init__(self):

        super().__init__()

        menubar = self.menuBar()

        dosya = menubar.addMenu("dosya")
        duzenle = menubar.addMenu("düzenle")

        dosya_ac = QAction("dosya aç",self)
        dosya_ac.setShortcut("Ctrl+O")
        dosya_kaydet = QAction("dosya kaydet", self)
        dosya_kaydet.setShortcut("Ctrl+S")
        cikis = QAction("çıkış", self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)

        ara_ve_degistir = duzenle.addMenu("ara ve değiştir")

        ara = QAction("ara",self)
        degistir = QAction("değiştir",self)

        temizle = QAction("temizle",self)

        ara_ve_degistir.addAction(ara)
        ara_ve_degistir.addAction(degistir)

        duzenle.addAction(temizle)

        cikis.triggered.connect(self.cikis_yap)

        dosya.triggered.connect(self.response)


        self.setWindowTitle("menüler")
        self.show()
    def cikis_yap(self):
        qApp.quit()

    def response(self,action):
        if action.text() == "dosya aç":
            print("dosya aça basıldı")
        if action.text() == "dosya kaydet":
            print("dosya kaydete basıldı")
        if action.text() == "çıkış":
            print("çıkışa basıldı")













app = QApplication(sys.argv)

menu = Menu()


sys.exit(app.exec_())