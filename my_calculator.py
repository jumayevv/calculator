import sys
from PyQt6.QtGui import QIcon,QKeyEvent
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QGridLayout,QLineEdit
from tkinter import messagebox
class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(600,200,300,300)
        self.setWindowIcon(QIcon('calculator.png'))
        self.setStyleSheet("font-family: 'Book Antiqua'; font-size: 20px;")
        self.g_box = QGridLayout()
    
        self.label = QLineEdit()
        self.label.setStyleSheet('border: 2px solid grey')
        self.label.setFixedSize(300,40)
        self.g_box.addWidget(self.label,0,0,1,4)

        self.setStyleSheet("""
                            QPushButton {    
                                font-size: 25px;
                                background-color: orange;
                                color: black;
                                border: 2px solid black;
                                border-radius: 16px;
                            } 
                            
                            QPushButton:pressed {
                                background-color: yellow;
                            }
                        """)
        names = ['7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '.','0', '=', '+']

        positions = [(i, j) for i in range(1, 5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '=':
                btn = QPushButton(name)
                btn.clicked.connect(self.final)
                self.g_box.addWidget(btn, *position)
            else:
                btn = QPushButton(name)
                btn.clicked.connect(lambda x,b=name:self.append_number(b))
                self.g_box.addWidget(btn, *position)

        self.setLayout(self.g_box)
        
    def append_number(self, b):
        self.label.setText(self.label.text() + b)
        
    def final(self):        
        try:
            result = eval(self.label.text())
            self.label.setText(str(result))
        except ZeroDivisionError:
            messagebox.showerror(title="Error",message="CAN'T DIVIDE BY ZERO !?")
        except Exception:
            messagebox.showerror(title="Error",message="SOMETHING WENT WRONG !?")
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Return:
            self.final()



app = QApplication([])
win = MainWindow()
win.show()
sys.exit(app.exec())