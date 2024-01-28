import sys
import os
from PyQt5 import QtWidgets, QtCore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    widget.resize(800, 600)
    widget.setWindowTitle("芒果工具")
    widget.show()

    sys.exit(app.exec_())