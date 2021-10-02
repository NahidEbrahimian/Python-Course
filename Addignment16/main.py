import PySide6
import math
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from functools import partial

# run pyside6-designer

from PySide6.QtWidgets import QMainWindow
class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.flag = 0
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()

        self.ui.btn_0.clicked.connect(partial(self.function_num, 0))
        self.ui.btn_1.clicked.connect(partial(self.function_num, 1))
        self.ui.btn_2.clicked.connect(partial(self.function_num, 2))
        self.ui.btn_3.clicked.connect(partial(self.function_num, 3))
        self.ui.btn_4.clicked.connect(partial(self.function_num, 4))
        self.ui.btn_5.clicked.connect(partial(self.function_num, 5))
        self.ui.btn_6.clicked.connect(partial(self.function_num, 6))
        self.ui.btn_7.clicked.connect(partial(self.function_num, 7))
        self.ui.btn_8.clicked.connect(partial(self.function_num, 8))
        self.ui.btn_9.clicked.connect(partial(self.function_num, 9))
        self.ui.btn_dot.clicked.connect(partial(self.function_num, '.'))

        self.ui.btn_sum.clicked.connect(partial(self.opr, '+'))
        self.ui.btn_sub.clicked.connect(partial(self.opr, '-'))
        self.ui.btn_div.clicked.connect(partial(self.opr, '/'))
        self.ui.btn_mul.clicked.connect(partial(self.opr, '*'))
        self.ui.btn_sin.clicked.connect(partial(self.opr, 'sin'))
        self.ui.btn_cos.clicked.connect(partial(self.opr, 'cos'))
        self.ui.btn_tan.clicked.connect(partial(self.opr, 'tan'))
        self.ui.btn_cot.clicked.connect(partial(self.opr, 'cot'))
        self.ui.btn_log.clicked.connect(partial(self.opr, 'log'))
        self.ui.btn_sqrt.clicked.connect(partial(self.opr, 'sqrt'))
        self.ui.btn_c.clicked.connect(partial(self.opr, 'clc'))
        self.ui.btn_Per.clicked.connect(partial(self.opr, 'pers'))
        self.ui.btn_sign.clicked.connect(partial(self.opr, 'sign'))

        self.ui.btn_eaual.clicked.connect(partial(self.equal))

    def function_num(self, num):
        if num == '.':
            self.flag = 1

        if self.ui.textbox.text() == '' or self.ui.textbox.text() == '0':
            if num == 0:
                self.ui.textbox.setText(str(num))
            elif num == '.':
                self.ui.textbox.setText('0' + str(num))
            else:
                self.ui.textbox.setText(str(num))
        else:
            self.ui.textbox.setText(self.ui.textbox.text() + str(num))

    def opr(self, opr):

        if opr == '+' or opr == '-' or opr == '/' or opr == '*' or opr == 'sign' or opr == 'pers':

            if self.flag == 1:
                self.num1 = float(self.ui.textbox.text())
            else:
                self.num1 = int(self.ui.textbox.text())
            self.ui.textbox.setText('')

            if opr == '+':
                self.opr = 'sum'

            elif opr == '-':
                self.opr = 'sub'

            elif opr == '*':
                self.opr = 'mul'

            elif opr == '/':
                self.opr = 'div'

            elif opr == 'sign':
                self.ui.textbox.setText(str(-1 * self.num1))

            elif opr == 'pers':
                self.ui.textbox.setText(str(self.num1 / 100))

        else:
            self.ui.textbox.setText('')
            if opr == 'sin':
                self.opr = 'sin'

            elif opr == 'cos':
                self.opr = 'cos'

            elif opr == 'tan':
                self.opr = 'tan'

            elif opr == 'cot':
                self.opr = 'cot'

            elif opr == 'log':
                self.opr = 'log'

            elif opr == 'sqrt':
                self.opr = 'sqrt'

            elif opr == 'clc':
                self.opr = 'clear'
                self.ui.textbox.setText('')


    def equal(self):

        if self.opr == 'sum' or self.opr == 'sub' or self.opr == 'div' or self.opr == 'div' or self.opr == 'mul':
            if self.flag == 1:
                self.num2 = float(self.ui.textbox.text())
            else:
                self.num2 = int(self.ui.textbox.text())

            if self.opr == 'sum':
                self.ui.textbox.setText(str(self.num1 + self.num2))

            elif self.opr == 'sub':
                if self.num1 < self.num2:
                    self.ui.textbox.setText(str(1 * (self.num1 - self.num2)))
                else:
                    self.ui.textbox.setText(str(self.num1 - self.num2))

            elif self.opr == 'div':
                if self.num2 != 0:
                    self.ui.textbox.setText(str(self.num1 / self.num2))
                else:
                    self.ui.textbox.setText('undefined')

            elif self.opr == 'mul':
                self.ui.textbox.setText(str(self.num1 * self.num2))

        else:
            if self.flag == 1:
                self.num1 = float(self.ui.textbox.text())
            else:
                self.num1 = int(self.ui.textbox.text())
            self.ui.textbox.setText('')

            if self.opr == 'sin':
                self.ui.textbox.setText(str(math.sin(math.radians(self.num1))))

            elif self.opr == 'cos':
                self.ui.textbox.setText(str(math.cos(math.radians(self.num1))))

            elif self.opr == 'tan':
                self.ui.textbox.setText(str(math.tan(math.radians(self.num1))))

            elif self.opr == 'cot':
                sin = math.sin(math.radians(self.num1))
                cos = math.cos(math.radians(self.num1))
                self.ui.textbox.setText(str(cos / sin))

            elif self.opr == 'sqrt':
                if self.num1 < 0:
                    self.ui.textbox.setText('undefined')
                else:
                    self.ui.textbox.setText(str(math.sqrt(self.num1)))

            elif self.opr == 'log':
                if self.num1 < 0:
                    self.ui.textbox.setText('undefined')
                else:
                    self.ui.textbox.setText(str(math.log(self.num1, 10)))

app = QApplication([])
window = Main()

app.exec_()




