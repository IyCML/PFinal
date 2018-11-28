# coding: utf-8
import numpy as np
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QPushButton,
                            QAction, QLineEdit, QMessageBox, QLabel, QGroupBox,
                            QGridLayout,QVBoxLayout, QFormLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QRectF
import pyqtgraph as pg
from PyQt5 import QtGui
class App_MovingCircle(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Moving circle'
        self.left = 300
        self.top = 30
        self.width = 700
        self.height = 700
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.window = QWidget() #defino nueva ventana para aplicar layout
        self.setCentralWidget(self.window)

        self.move_btn = QPushButton("move")
        self.move_btn.setSizePolicy(QtGui.QSizePolicy.Preferred,
                                    QtGui.QSizePolicy.Ignored)

        pg.setConfigOption('background', 'k')
        self.graphicsView = pg.PlotWidget(self.window)

        self.move_btn.clicked.connect(self.move_clk)

        grid = QGridLayout()

        grid.addWidget(self.createPropGroup(),0,0,1,1)
        grid.addWidget(self.move_btn,0,1,1,2)
        grid.addWidget(self.graphicsView,1,0,1,3)

        # grid.setColumnStretch(1,3)
        # grid.setColumnStretch(0,4)


        self.window.setLayout(grid)

        self.show()

    def move_clk(self):
        self.graphicsView.plotItem.clear()
        self.graphicsView.plotItem.hideAxis('bottom')
        self.graphicsView.plotItem.hideAxis('left')
        self.graphicsView.setRange(QRectF(0, 0, 30, 2))
        # x = np.array([float(self.xedit.text())])
        y = np.array([float(self.yedit.text())])
        x = np.array([np.random.randint(2,28)])

        radio = float(self.radioedit.text())

        self.p1 = self.graphicsView.plotItem.scatterPlot(x, y, pen='r',
                                                        symbol='o',
                                                        symbolSize=radio,
                                                        symbolPen = 'r',
                                                        symbolBrush='r')

        # self.p1.hideAxis('bottom')
        # ‘left’, ‘bottom’, ‘right’, or ‘top’

        return self.p1

    def createPropGroup(self):
        propBox = QGroupBox("circle properties")
        self.radio = QLabel('radio'); self.radioedit = QLineEdit('80')
        self.x = QLabel('pos x'); self.xedit = QLineEdit('0')
        self.y = QLabel('pos y'); self.yedit = QLineEdit('1')
        formin = QFormLayout()
        formin.addRow(self.radio,self.radioedit)
        formin.addRow(self.x,self.xedit)
        formin.addRow(self.y,self.yedit)
        propBox.setLayout(formin)
        return propBox


if __name__ == '__main__':
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    ex = App_MovingCircle()
    sys.exit(app.exec_())
