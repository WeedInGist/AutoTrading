import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import pykorbit
from PyQt5.QtCore import *

class MySignal(QObject):
    signal_1 = pyqtSignal()
    signal_2 = pyqtSignal(int, int)
    def run(self):
        self.signal_1.emit()
        self.signal_2.emit(1,2)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        mysignal = MySignal()
        mysignal.signal_1.connect(self.signal_1_emitted)
        mysignal.signal_2.connect(self.signal_2_emitted)
        mysignal.run()

    @pyqtSlot()
    def signal_1_emitted(self):
        print("signal_1 emitted")

    @pyqtSlot(int, int)
    def signal_2_emitted(self, arg1, arg2):
        print("signal_2 emitted", arg1, arg2)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()