from PySide2.QtWidgets import (QApplication, )
from PySide2.QtQml import (QQmlApplicationEngine, )
from PySide2.QtGui import (QFont, )
from PySide2.QtCore import (QObject, QUrl, Slot, Qt, )


class Main(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.engine = QQmlApplicationEngine(self)
        self.engine.rootContext().setContextProperty("backend", self)
        self.engine.load(QUrl.fromLocalFile('app.qml'))

    @Slot(str)
    def create(self, string):
        print(string)


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
app = QApplication.instance()
if app is None:
    app = QApplication()
font = QFont()
font.setStyleStrategy(QFont.PreferQuality)
font.setFamily('DejaVu')
# font.setPointSize(10)
app.setFont(font)
main = Main()
app.exec_()
