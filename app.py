from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton
)
from instr import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()

        self.setWindowTitle("Ruffier App v1.0")
        self.resize(win_width, win_height)
        self.show()

    def initUI(self):
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def next_click(self):
        print("Click!")

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

app = QApplication([])
win = MainWin()
app.exec_()