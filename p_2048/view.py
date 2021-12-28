import sys
from PySide2 import QtGui, QtCore, QtWidgets
import random
from math import cos


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("2048")
        self.setGeometry(300, 200, 610, 610)
        self.create_ui()

        self.show()

    def resizeEvent(self, event:QtGui.QResizeEvent) -> None:
        self.view.scene().setSceneRect(0, 0, self.size().width() - 10, self.size().height() - 10)
        a = self.view.scene().items()[0]

    def create_ui(self):
        spacing = 5
        scene = QtWidgets.QGraphicsScene(self)
        scene.setSceneRect(0, 0, self.size().width() - 10, self.size().height() - 10)
        brush = QtGui.QBrush(QtCore.Qt.green)
        pen = QtGui.QPen(QtCore.Qt.black)
        pen.setWidth(2)

        for i in range(4):
            for j in range(4):
                rect_x = j * 600 // 4 + spacing
                rect_y = i * 600 // 4 + spacing
                rect_w = 600 // 4 - 2 * spacing
                rect_h = 600 // 4 - 2 * spacing
                scene.addRect(QtCore.QRectF(rect_x, rect_y, rect_w, rect_h)).setBrush(brush)
                scene.addText("0", QtGui.QFont("Arial", 20)).setPos(rect_x + rect_w // 2 - 20, rect_y + rect_h // 2 - 20,)


        self.view = QtWidgets.QGraphicsView(scene, self)
        self.setCentralWidget(self.view)


    def keyPressEvent(self, event:QtGui.QKeyEvent) -> None:
        event.key()
        if event.key() == QtCore.Qt.Key_W:
            a = self.view.scene().items()[0]
            print(self.view.scene().items())
            a.moveBy(100, 100)
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())