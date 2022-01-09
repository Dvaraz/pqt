import sys
from PySide2 import QtGui, QtCore, QtWidgets
import engine
import random
from math import cos
import itertools


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setWindowTitle(f"2048 Score: {self.score}")
        self.setGeometry(300, 200, 610, 610)
        self.mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.grid = engine.Move(self.mas)
        self.create_ui()

        self.show()

    def resizeEvent(self, event:QtGui.QResizeEvent) -> None:
        self.view.scene().setSceneRect(0, 0, self.size().width() - 10, self.size().height() - 10)
        a = self.view.scene().items()[0]

    def create_ui(self):
        spacing = 5
        scene = QtWidgets.QGraphicsScene(self)
        scene.setSceneRect(0, 0, self.size().width() - 10, self.size().height() - 10)
        brush = QtGui.QBrush(QtCore.Qt.lightGray)
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
                # scene.addRect().setBrush()
                # scene.addText().toPlainText()


        self.view = QtWidgets.QGraphicsView(scene, self)
        self.setCentralWidget(self.view)

    @staticmethod
    def paint_rect(text, rects):
        for k, i in enumerate(text):
            if i.toPlainText() == "0":
                rects[k].setBrush(QtGui.QBrush(QtCore.Qt.lightGray))
            if i.toPlainText() == "2":
                rects[k].setBrush(QtGui.QBrush(QtCore.Qt.green))
            if i.toPlainText() == "4":
                rects[k].setBrush(QtGui.QBrush(QtCore.Qt.yellow))
            if i.toPlainText() == "8":
                rects[k].setBrush(QtGui.QBrush(QtCore.Qt.blue))
            if i.toPlainText() == "16":
                rects[k].setBrush(QtGui.QBrush(QtCore.Qt.cyan))
            if i.toPlainText() == "32":
                rects[k].setBrush(QtGui.QBrush(QtCore.Qt.magenta))
            if i.toPlainText() == "64":
                rects[k].setBrush(QtGui.QBrush(QtCore.Qt.darkCyan))
            if i.toPlainText() == "128":
                rects[k].setBrush(QtGui.QBrush(QtCore.Qt.darkGreen))
            if i.toPlainText() == "256":
                rects[k].setBrush(QtGui.QBrush(QtCore.Qt.darkRed))
            if i.toPlainText() == "512":
                rects[k].setBrush(QtGui.QBrush(QtCore.Qt.red))
            if i.toPlainText() == "1024":
                rects[k].setBrush(QtGui.QBrush(QtCore.Qt.darkBlue))
            if i.toPlainText() == "2048":
                rects[k].setBrush(QtGui.QBrush(QtCore.Qt.black))
        return rects

    def win_case(self):
        if self.score >= 2048:
            self.view.scene().addText("YOU WIN!!!!", QtGui.QFont("Arial", 60)).setPos(0, 200)


    def keyPressEvent(self, event:QtGui.QKeyEvent) -> None:

        if len(self.grid.get_empty_list()) != 0:
            a = self.grid.get_index_from_number(random.choice(self.grid.get_empty_list()))
            self.grid.insert_2_or_4(a[0], a[1])
        rects = [value for index, value in enumerate(self.view.scene().items()) if index % 2 == 1]
        texts = [value for index, value in enumerate(self.view.scene().items()) if index % 2 == 0]
        self.paint_rect(texts, rects)
        # Game start
        if event.key() == QtCore.Qt.Key_P:
            test, delta = self.grid.move_up()
            for k, j in enumerate(reversed(texts)):
                x, y = self.grid.get_index_from_number(k + 1)
                j.setPlainText(str(test[x][y]))
                self.paint_rect(texts, rects)

        if event.key() == QtCore.Qt.Key_W:
            test, delta = self.grid.move_up()
            for k, j in enumerate(reversed(texts)):
                x, y = engine.Move.get_index_from_number(k + 1)
                j.setPlainText(str(test[x][y]))
                self.paint_rect(texts, rects)
            self.score += delta
            self.setWindowTitle(f"2048 Score: {self.score}")

        if event.key() == QtCore.Qt.Key_S:
            test, delta = self.grid.move_down()
            for k, j in enumerate(reversed(texts)):
                x, y = engine.Move.get_index_from_number(k + 1)
                j.setPlainText(str(test[x][y]))
                self.paint_rect(texts, rects)
            self.score += delta
            self.setWindowTitle(f"2048 Score: {self.score}")

        if event.key() == QtCore.Qt.Key_A:
            test, delta = self.grid.move_left()
            for k, j in enumerate(reversed(texts)):
                x, y = engine.Move.get_index_from_number(k + 1)
                j.setPlainText(str(test[x][y]))
                self.paint_rect(texts, rects)
            self.score += delta
            self.setWindowTitle(f"2048 Score: {self.score}")

        if event.key() == QtCore.Qt.Key_D:
            test, delta = self.grid.move_right()
            for k, j in enumerate(reversed(texts)):
                x, y = engine.Move.get_index_from_number(k + 1)
                j.setPlainText(str(test[x][y]))
                self.paint_rect(texts, rects)
            self.score += delta
            self.setWindowTitle(f"2048 Score: {self.score}")
        self.win_case()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())