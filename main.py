import sys
from UI import Ui_MainWindow
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt


class Guess_the_number(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)   # 继承主窗口类
        self.setupUi(self)

        self.initUi_txt()       # 初始化文本
        self.initUi_button()       # 初始化按键

    def initUi_txt(self):
        self.left = 0  # 提示范围的左界默认值
        self.right = 1000  # 提示范围的右界默认值
        self.guess_num = random.randint(1, 999)     # 生成随机数
        self.label_1.setText('数值的范围是：{}-{}'.format(self.left, self.right))  # 提示数值范围
        self.label_2.setText('请输入')

    def initUi_button(self):
        self.pushButton.clicked.connect(self.abnormal)     # 确认
        self.pushButton_2.clicked.connect(app.quit)     # 退出游戏
        self.pushButton_3.clicked.connect(self.initUi_txt)   # 重新开始

    def abnormal(self):     # 捕获输入异常
        QApplication.processEvents()    # 将正在处理的事件的控制权还给Qt 个人理解为把它丢到子进程，以防主进程堵塞
        text = self.lineEdit.text()  # 接受文本框中的文本
        try:
            text = int(text)
            self.guess(text)
        except:
            self.label_2.setText('     输入不合法')
            self.label_1.setText('数值的范围:{}-{}'.format(self.left, self.right))
            self.lineEdit.clear()

    def guess(self, text):  # 判断
        if self.guess_num == text:
            QMessageBox.about(self, "胜利", "恭喜你猜中了")     # 弹出对话框
            self.initUi_txt()

        elif self.guess_num > text:
            if text > self.left:
                self.left = text
            self.label_1.setText('数值的范围:{}-{}'.format(self.left, self.right))
            self.label_2.setText('      猜小了')

        elif self.guess_num < text:
            if text < self.right:
                self.right = text
            self.label_1.setText('数值的范围:{}-{}'.format(self.left, self.right))
            self.label_2.setText('       猜大了')

        self.lineEdit.clear()   # 清除输入框

    def keyPressEvent(self, e):     # 设置快捷键
        if e.key() == Qt.Key_Return:
            self.abnormal()
        elif e.key() == Qt.Key_Escape:
            app.quit()
        elif e.key() == Qt.Key_R:
            self.reset()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    MainWindow = Guess_the_number()

    MainWindow.show()
    sys.exit(app.exec_())
