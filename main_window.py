import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pickle
from PyQt5 import QtCore, QtWidgets, QtGui
from ui_main import Ui_MainWindow


class MainApp(Ui_MainWindow):
    def __init__(self, parent):
        self.setupUi(parent)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainApp(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
