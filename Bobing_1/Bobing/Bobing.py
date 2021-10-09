import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
import random
import numpy as np
import pygame

class Bobing (QMainWindow):
    def __init__(self):
        super(Bobing, self).__init__()
        self.initUI()
        self.i=0    #设置计数器变量

    def initUI(self):
        self.setWindowTitle('中秋博饼')
        self.setFixedSize(1096,941)
        self.setWindowIcon(QIcon('图片/软件图标.png'))

        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        self.setMainWindow()  #首页

        self.setSingleWindow()

        self.setMultiWindow()

    #1.首页
    def setMainWindow(self):
        self.stack1 = QWidget()
        self.stack1.setGeometry(0,0,1096,941)
        self.stack1.setObjectName('MainWindow')
        style = '''
                    #MainWindow{
                        border-image:url('图片/主页背景.png');
                    }
                '''
        self.stack1.setStyleSheet(style)
        self.stack.addWidget(self.stack1)


        #1.1退出程序
        self.button1_1 = QPushButton(self.stack1)
        self.button1_1.move(990, 840)
        self.button1_1.setMaximumSize(80, 80)
        self.button1_1.setMinimumSize(80, 80)
        self.button1_1.setObjectName('button1_1')
        style = '''
                            #button1_1{
                                border-radius:4px;
                                background-image:url('图片//退出1.png');
                            }
                        '''
        self.button1_1.setStyleSheet(style)
        self.button1_1.clicked.connect(self.Quit)



        #1.2单人1.3多人按钮

        #单人游戏
        self.button1_2 = QPushButton(self.stack1)
        self.button1_2.move(360, 400)
        self.button1_2.setMaximumSize(396, 132)
        self.button1_2.setMinimumSize(396, 132)
        self.button1_2.setObjectName('button1_2')
        style = '''
                    #button1_2{
                        border-radius:4px;
                        background-image:url('图片//单人游戏.png');
                    }
                '''
        self.button1_2.setStyleSheet(style)
        #跳转
        self.button1_2.clicked.connect(self.displaySingelWindow)




        #多人模式图标
        self.button1_3 = QPushButton(self.stack1)
        self.button1_3.move(355, 600)
        self.button1_3.setMaximumSize(400, 132)
        self.button1_3.setMinimumSize(400,132)
        self.button1_3.setObjectName('button1_3')
        style = '''
                            #button1_3{
                                border-radius:4px;
                                background-image:url('图片//多人模式.png');
                            }
                        '''
        self.button1_3.setStyleSheet(style)

        #跳转多人游戏
        self.button1_3.clicked.connect(self.displayMultiWindow)

        #1.4.设置图标
        self.button1_4 = QPushButton(self.stack1)
        self.button1_4.move(10,0)
        self.button1_4.setMaximumSize(94,94)
        self.button1_4.setMinimumSize(94,94)
        self.button1_4.setObjectName('button1_4')
        style = '''
            #button1_4{
                border-radius:4px;
                background-image:url('图片//设置.png');
            }
        '''
        self.button1_4.setStyleSheet(style)
        self.button1_4.clicked.connect(self.Button1_4Clicked)

        # 1.7查看规则图标
        self.button1_5 = QPushButton(self.stack1)
        self.button1_5.move(900, 500)
        self.button1_5.setMaximumSize(120, 111)
        self.button1_5.setMinimumSize(120, 111)
        self.button1_5.setObjectName('button1_5')
        style = '''
                            #button1_5{
                                border-radius:4px;
                                background-image:url('图片//查看规则1.png');
                            }
                        '''
        self.button1_5.setStyleSheet(style)
        self.button1_5.clicked.connect(self.Button1_5Clicked)


        #1.5设置界面
        self.widget1_1 = QWidget(self.stack1)
        self.widget1_1.setGeometry(0,-5,1672,941)
        self.widget1_1.setObjectName('widget1_1')
        style = '''
                    #widget1_1{
                        border-image:url('图片//设置页面1.png');
                    }
                '''
        self.widget1_1.setStyleSheet(style)
        #默认隐藏设置页面
        self.widget1_1.hide()



        #1.6返回按钮
        self.button1_12 = QPushButton(self.widget1_1)
        self.button1_12.setGeometry(0,0,94,94)
        self.button1_12.setObjectName('button1_12')
        style = '''
                                                    #button1_12{
                                                        border-radius:4px;
                                                        background-image:url('图片//返回.png');
                                                    }
                                                '''
        self.button1_12.setStyleSheet(style)
        self.button1_12.clicked.connect(self.Button1_12Clicked)






        # 1.8规则界面
        self.widget1_2 = QWidget(self.stack1)
        self.widget1_2.setGeometry(0, -5, 1096, 941)
        self.widget1_2.setObjectName('widget1_2')
        style = '''
                        #widget1_2{
                            border-image:url('图片//规则.png');
                        }
                    '''
        self.widget1_2.setStyleSheet(style)
        # 默认隐藏设置页面
        self.widget1_2.hide()

        # 1.9规则返回按钮
        self.button1_13 = QPushButton(self.widget1_2)
        self.button1_13.setGeometry(0, 0, 94, 94)
        self.button1_13.move(950,10)
        self.button1_13.setObjectName('button1_13')
        style = '''
                                                        #button1_13{
                                                            border-radius:4px;
                                                            background-image:url('图片//返回.png');
                                                        }
                                                    '''
        self.button1_13.setStyleSheet(style)
        self.button1_13.clicked.connect(self.Button1_13Clicked)

    #2.单人游戏界面
    def setSingleWindow(self):

        #规则

        #self.resultDic = {'六':{},'五':{},'四':{},'三':{},'二':{},'一':{}}



        self.stack2 = QWidget()
        self.stack2.setGeometry(0,0,1672,941)
        self.stack2.setObjectName('SearchWindow')
        style = '''
                        #SearchWindow{
                            border-image:url('图片//单人游戏界面.png');
                        }
                    '''
        self.stack2.setStyleSheet(style)
        self.stack.addWidget(self.stack2)


        #返回按钮
        self.button2_1 = QPushButton(self.stack2)
        self.button2_1.move(0,0)
        self.button2_1.setMaximumSize(94,94)
        self.button2_1.setMinimumSize(94,94)
        self.button2_1.setObjectName('button2_1')
        style = '''
            #button2_1{
                border-radius:4px;
                background-image:url('图片//返回.png');
            }
        '''
        self.button2_1.setStyleSheet(style)
        self.button2_1.clicked.connect(self.returnMain)


        #开始摇骰子按钮
        self.button2_2 = QPushButton(self.stack2)
        self.button2_2.move(70,250)
        self.button2_2.setMaximumSize(295, 212)
        self.button2_2.setMinimumSize(295, 212)
        self.button2_2.setObjectName('button2_2')
        style = '''
            #button2_2{
                border-radius:4px;
                background-image:url('图片//开始按钮1.png');
            }
        '''
        self.button2_2.setStyleSheet(style)

        self.button2_2.clicked.connect(self.show_function)

        # nummm =self.show_function()
        # print(nummm)

        #结果+文字
        self.label2_3 = QLabel(self.stack2)
        self.label2_3.resize(311,158)
        self.label2_3.move(550,250)
        self.label2_3.setPixmap(QPixmap('图片/玩家.png'))
        self.label2_3.setScaledContents(True)

        self.lineedit2_3 = QLineEdit(self.stack2)
        self.lineedit2_3.setReadOnly(True)
        self.lineedit2_3.move(830,300)
        self.lineedit2_3.setFont(QFont('华光琥珀_CNKI', 36))
        self.lineedit2_3.setFixedWidth(250)

    # 3.设置多人游戏界面
    def setMultiWindow(self):
        self.stack3 = QWidget()
        self.stack3.setGeometry(0, 0, 1672, 941)
        self.stack3.setObjectName('MultiWindow')
        style = '''
                                  #MultiWindow{
                                      border-image:url('图片//多人界面.png');
                                  }
                              '''
        self.stack3.setStyleSheet(style)
        self.stack.addWidget(self.stack3)


        #输入人数
        self.lineedit3_0 = QLineEdit(self.stack3)
        self.lineedit3_0.move(290,195)
        self.lineedit3_0.setFont(QFont('华光琥珀_CNKI', 36))
        self.lineedit3_0.setFixedWidth(50)

        #确认按钮
        self.button3_3 = QPushButton(self.stack3)
        self.button3_3.move(350,205)
        self.button3_3.setMaximumSize(45, 45)
        self.button3_3.setMinimumSize(45, 45)
        self.button3_3.setObjectName('button3_3')
        style = '''
            #button3_3{
                border-radius:4px;
                background-image:url('图片//确认按钮1.png');
            }
        '''
        self.button3_3.setStyleSheet(style)
        self.button3_3.clicked.connect(self.jumpWindow)


        #隐藏玩家1-4标识
        #玩家1
        self.lineedit3_1_0 = QLineEdit(self.stack3)
        self.lineedit3_1_0.setText('玩家1')
        self.lineedit3_1_0.setVisible(True)
        self.lineedit3_1_0.setReadOnly(True)
        self.lineedit3_1_0.move(650,280)
        self.lineedit3_1_0.setFont(QFont('华光琥珀_CNKI', 36))
        self.lineedit3_1_0.setVisible(False)
        self.lineedit3_1_0.setFixedWidth(150)

        self.lineedit3_1 = QLineEdit(self.stack3)
        self.lineedit3_1.setVisible(True)
        self.lineedit3_1.move(800,280)
        self.lineedit3_1.setFont(QFont('华光琥珀_CNKI', 36))
        self.lineedit3_1.setFixedWidth(200)
        self.lineedit3_1.setVisible(False)

        #玩家2
        self.lineedit3_2_0 = QLineEdit(self.stack3)
        self.lineedit3_2_0.setText('玩家2')
        self.lineedit3_2_0.setVisible(True)
        self.lineedit3_2_0.setReadOnly(True)
        self.lineedit3_2_0.move(650,380)
        self.lineedit3_2_0.setFont(QFont('华光琥珀_CNKI', 36))
        self.lineedit3_2_0.setVisible(False)
        self.lineedit3_2_0.setFixedWidth(150)

        self.lineedit3_2 = QLineEdit(self.stack3)
        self.lineedit3_2.setVisible(True)
        self.lineedit3_2.move(800,380)
        self.lineedit3_2.setFont(QFont('华光琥珀_CNKI', 36))
        self.lineedit3_2.setFixedWidth(200)
        self.lineedit3_2.setVisible(False)

        #玩家3
        self.lineedit3_3_0 = QLineEdit(self.stack3)
        self.lineedit3_3_0.setText('玩家3')
        self.lineedit3_3_0.setVisible(True)
        self.lineedit3_3_0.setReadOnly(True)
        self.lineedit3_3_0.move(650,480)
        self.lineedit3_3_0.setFont(QFont('华光琥珀_CNKI', 36))
        self.lineedit3_3_0.setVisible(False)
        self.lineedit3_3_0.setFixedWidth(150)

        self.lineedit3_3 = QLineEdit(self.stack3)
        self.lineedit3_3.setVisible(True)
        self.lineedit3_3.move(800,480)
        self.lineedit3_3.setFont(QFont('华光琥珀_CNKI', 36))
        self.lineedit3_3.setFixedWidth(200)
        self.lineedit3_3.setVisible(False)

        #玩家4
        self.lineedit3_4_0 = QLineEdit(self.stack3)
        self.lineedit3_4_0.setText('玩家4')
        self.lineedit3_4_0.setVisible(True)
        self.lineedit3_4_0.setReadOnly(True)
        self.lineedit3_4_0.move(650,580)
        self.lineedit3_4_0.setFont(QFont('华光琥珀_CNKI', 36))
        self.lineedit3_4_0.setVisible(False)
        self.lineedit3_4_0.setFixedWidth(150)

        self.lineedit3_4 = QLineEdit(self.stack3)
        self.lineedit3_4.setVisible(True)
        self.lineedit3_4.move(800,580)
        self.lineedit3_4.setFont(QFont('华光琥珀_CNKI', 36))
        self.lineedit3_4.setFixedWidth(200)
        self.lineedit3_4.setVisible(False)

        # 返回按钮
        self.button3_1 = QPushButton(self.stack3)
        self.button3_1.move(0, 0)
        self.button3_1.setMaximumSize(94, 94)
        self.button3_1.setMinimumSize(94, 94)
        self.button3_1.setObjectName('button3_1')
        style = '''
                      #button3_1{
                          border-radius:4px;
                          background-image:url('图片//返回.png');
                      }
                  '''
        self.button3_1.setStyleSheet(style)
        self.button3_1.clicked.connect(self.returnMain)



        #开始摇骰子按钮
        self.button3_2 = QPushButton(self.stack3)
        self.button3_2.move(70,280)
        self.button3_2.setMaximumSize(295, 212)
        self.button3_2.setMinimumSize(295, 212)
        self.button3_2.setObjectName('button3_2')
        style = '''
            #button3_2{
                border-radius:4px;
                background-image:url('图片//开始按钮1.png');
            }
        '''
        self.button3_2.setStyleSheet(style)

        # self.button3_2.clicked.connect(lambda:self.show_function_multi(1))
        # self.button3_2.clicked.connect(lambda:self.show_function_multi(2))
        # self.button3_2.clicked.connect(lambda:self.show_function_multi(3))
        # self.button3_2.clicked.connect(lambda:self.show_function_multi(4))
        self.button3_2.clicked.connect(self.show_function_multi)





    #骰子+结果
    def show_function_multi(self):

        self.i+=1    #变量自增
        #print(self.i)
        num = self.lineedit3_0.text()
        #print(num)

        result = []

        for i in range (1,7): #0-6六个骰子
            # 前4个骰子

            if i<4 :
                num = random.randrange(1,7,1)
                if num == 1:

                    pic = "图片/1.png"
                    self.label3_3 = QLabel(self.stack3)
                    self.label3_3.resize(250,250)
                    self.label3_3.move(-30+i*120,530)
                    self.label3_3.setPixmap(QPixmap('图片//1.png'))
                    self.label3_3.setScaledContents(True) #让图片自适应标签大小
                    self.label3_3.show()

                elif num == 2:

                    pic = "图片/2.png"
                    self.label3_3 = QLabel(self.stack3)
                    self.label3_3.resize(250, 250)
                    self.label3_3.move(-30+i*120,530)
                    self.label3_3.setPixmap(QPixmap('图片//2.png'))
                    self.label3_3.setScaledContents(True)
                    self.label3_3.show()

                elif num == 3:

                    pic = "图片/3.png"
                    self.label3_3 = QLabel(self.stack3)
                    self.label3_3.resize(250, 250)
                    self.label3_3.move(-30+i*120,530)
                    self.label3_3.setPixmap(QPixmap('图片//3.png'))
                    self.label3_3.setScaledContents(True)
                    self.label3_3.show()

                elif num == 4:

                    pic = "图片/4.png"
                    self.label3_3 = QLabel(self.stack3)
                    self.label3_3.resize(250, 250)
                    self.label3_3.move(-30+i*120,530)
                    self.label3_3.setPixmap(QPixmap('图片//4.png'))
                    self.label3_3.setScaledContents(True)
                    self.label3_3.show()

                elif num == 5:

                    pic = "图片/5.png"
                    self.label3_3 = QLabel(self.stack3)
                    self.label3_3.resize(250, 250)
                    self.label3_3.move(-30+i*120,530)
                    self.label3_3.setPixmap(QPixmap('图片//5.png'))
                    self.label3_3.setScaledContents(True)
                    self.label3_3.show()

                else:

                    pic = "图片/6.png"
                    self.label3_3 = QLabel(self.stack3)
                    self.label3_3.resize(250, 250)
                    self.label3_3.move(-30+i*120,530)
                    self.label3_3.setPixmap(QPixmap('图片//6.png'))
                    self.label3_3.setScaledContents(True)
                    self.label3_3.show()

            #显示第4-第6个骰子

            else:

                num = random.randrange(1, 7, 1)

                if num == 1:

                    pic = "图片/1.png"
                    self.label3_3 = QLabel(self.stack3)
                    self.label3_3.resize(250, 250)
                    self.label3_3.move(-30+ (i-3) *120, 630)
                    self.label3_3.setPixmap(
                        QPixmap('图片//1.png'))
                    self.label3_3.setScaledContents(True)
                    self.label3_3.show()

                elif num == 2:

                    pic = "图片/2.png"
                    self.label3_3 = QLabel(self.stack3)
                    self.label3_3.resize(250, 250)
                    self.label3_3.move(-30+ (i-3) *120, 630)
                    self.label3_3.setPixmap(
                        QPixmap('图片//2.png'))
                    self.label3_3.setScaledContents(True)
                    self.label3_3.show()

                elif num == 3:

                    self.label3_3 = QLabel(self.stack3)
                    self.label3_3.resize(250, 250)
                    self.label3_3.move(-30+ (i-3) *120, 630)
                    self.label3_3.setPixmap(
                        QPixmap('图片//3.png'))
                    self.label3_3.setScaledContents(True)
                    self.label3_3.show()

                elif num == 4:

                    self.label3_3 = QLabel(self.stack3)
                    self.label3_3.resize(250, 250)
                    self.label3_3.move(-30+ (i-3) *120, 630)
                    self.label3_3.setPixmap(
                        QPixmap('图片//4.png'))
                    self.label3_3.setScaledContents(True)
                    self.label3_3.show()

                elif num == 5:

                    self.label3_3 = QLabel(self.stack3)
                    self.label3_3.resize(250, 250)
                    self.label3_3.move(-30+ (i-3) *120, 630)
                    self.label3_3.setPixmap(
                        QPixmap('图片//5.png'))
                    self.label3_3.setScaledContents(True)
                    self.label3_3.show()

                else:

                    self.label3_3 = QLabel(self.stack3)
                    self.label3_3.resize(250, 250)
                    self.label3_3.move(-30+ (i-3) *120, 630)
                    self.label3_3.setPixmap(
                        QPixmap('图片//6.png'))
                    self.label3_3.setScaledContents(True)
                    self.label3_3.show()

            result.append(num)

        #计数
        num_1 = str(result).count("1")
        num_2 = str(result).count("2")
        num_3 = str(result).count("3")
        num_4 = str(result).count("4")
        num_5 = str(result).count("5")
        num_6 = str(result).count("6")
        count_result = [num_1,num_2,num_3,num_4,num_5,num_6]
        print(count_result)





        #根据规则判断结果

        jie_guo = ["六杯黑", "六杯红", "状元", "状元插金花", "对堂", "状元",
                   "四进", "状元", "三红", "二举", "一秀", "再接再厉"]

        if count_result == self.liuBeiHei:
            res = 0

        elif count_result == self.liuBeiHong:
            res = 1

        elif count_result == self.zhuangYuan:
            res = 2

        elif count_result == self.jinHua:
            res = 3

        elif count_result == self.duiTang:
            res = 4

        elif count_result[2] == 5:
            res = 5

        elif count_result[2] == 4:
            res = 6

        elif count_result[3] == 4:
            res = 7

        elif count_result[3] == 3:
            res = 8

        elif count_result[3] == 2:
            res = 9

        elif count_result[3] == 1:
            res = 10

        else:
            res = 11



        if self.i == 1:
            self.lineedit3_1.setText(jie_guo[res])

        elif self.i == 2:
            self.lineedit3_2.setText(jie_guo[res])
        elif self.i == 3:
            self.lineedit3_3.setText(jie_guo[res])
        else:
            self.i == 4
            self.lineedit3_4.setText(jie_guo[res])
            self.button3_2.hide()

    #弹窗
    def jumpWindow(self):
        content = self.lineedit3_0.text()   #人数
        #print(content)
        if content == '2' or content == '3' or content == '4':
            QMessageBox.information(self, "提示", "设置成功", QMessageBox.Cancel)
            self.lineedit3_1.setVisible(True)
            self.lineedit3_1_0.setVisible(True)
            num = self.lineedit3_0.text()
            if num == '2':
                self.lineedit3_2.setVisible(True)
                self.lineedit3_2_0.setVisible(True)
            elif num == '3':
                self.lineedit3_2.setVisible(True)
                self.lineedit3_2_0.setVisible(True)
                self.lineedit3_3.setVisible(True)
                self.lineedit3_3_0.setVisible(True)
            else:
                self.lineedit3_2.setVisible(True)
                self.lineedit3_2_0.setVisible(True)
                self.lineedit3_3.setVisible(True)
                self.lineedit3_3_0.setVisible(True)
                self.lineedit3_4.setVisible(True)
                self.lineedit3_4_0.setVisible(True)
        else:
            QMessageBox.warning(self, "警告", "请输入2-4之间的整数", QMessageBox.Cancel)

    #随机数
    def randomNum(self):
        self.label2_2.show()

    #设置
    def Button1_4Clicked(self):
        self.widget1_1.show()
    def Button1_12Clicked(self):
        self.widget1_1.hide()

    #规则
    def Button1_5Clicked(self):
        self.widget1_2.show()
    def Button1_13Clicked(self):
        self.widget1_2.hide()


    #博饼结果

    liuBeiHei = [0, 0, 0, 0, 0, 6]
    liuBeiHong = [0, 0, 0, 6, 0, 0]
    zhuangYuan = [0, 0, 6, 0, 0, 0]
    jinHua = [2, 0, 0, 4, 0, 0]
    duiTang = [1, 1, 1, 1, 1, 1]

    #显示骰子,并返回存放结果的数组
    def show_function(self):

        #计算各点数的总数（计数器）
        counter_1 = 0
        counter_2 = 0
        counter_3 = 0
        counter_4 = 0
        counter_5 = 0
        counter_6 = 0

        #用来存放各点数个数的列表

        result_list = []


        for i in range(1,7):

            # 前4个骰子

            if i<4 :
                num = random.randrange(1,7,1)
                if num == 1:

                    counter_1 += 1

                    pic = "图片/1.png"
                    self.label2_2 = QLabel(self.stack2)
                    self.label2_2.resize(300,300)
                    self.label2_2.move(150+i*120,400)
                    self.label2_2.setPixmap(QPixmap('图片//1.png'))
                    self.label2_2.setScaledContents(True) #让图片自适应标签大小
                    self.label2_2.show()

                elif num == 2:

                    counter_2 += 1

                    pic = "图片/2.png"
                    self.label2_2 = QLabel(self.stack2)
                    self.label2_2.resize(300, 300)
                    self.label2_2.move(150+i*120,400)
                    self.label2_2.setPixmap(QPixmap('图片//2.png'))
                    self.label2_2.setScaledContents(True)
                    self.label2_2.show()

                elif num == 3:

                    counter_3 += 1

                    pic = "图片/3.png"
                    self.label2_2 = QLabel(self.stack2)
                    self.label2_2.resize(300, 300)
                    self.label2_2.move(150+i*120,400)
                    self.label2_2.setPixmap(QPixmap('图片//3.png'))
                    self.label2_2.setScaledContents(True)
                    self.label2_2.show()

                elif num == 4:

                    counter_4 += 1

                    pic = "图片/4.png"
                    self.label2_2 = QLabel(self.stack2)
                    self.label2_2.resize(300, 300)
                    self.label2_2.move(150+i*120,400)
                    self.label2_2.setPixmap(QPixmap('图片//4.png'))
                    self.label2_2.setScaledContents(True)
                    self.label2_2.show()

                elif num == 5:

                    counter_5 += 1

                    pic = "图片/5.png"
                    self.label2_2 = QLabel(self.stack2)
                    self.label2_2.resize(300, 300)
                    self.label2_2.move(150+i*120,400)
                    self.label2_2.setPixmap(QPixmap('图片//5.png'))
                    self.label2_2.setScaledContents(True)
                    self.label2_2.show()

                else:

                    counter_6 += 1

                    pic = "图片/6.png"
                    self.label2_2 = QLabel(self.stack2)
                    self.label2_2.resize(300, 300)
                    self.label2_2.move(150+i*120,400)
                    self.label2_2.setPixmap(QPixmap('图片//6.png'))
                    self.label2_2.setScaledContents(True)
                    self.label2_2.show()

            #显示第4-第6个骰子

            else:

                num = random.randrange(1, 7, 1)

                if num == 1:

                    counter_1 += 1


                    pic = "图片/1.png"
                    self.label2_2 = QLabel(self.stack2)
                    self.label2_2.resize(300, 300)
                    self.label2_2.move(150 + (i-3) * 120, 500)
                    self.label2_2.setPixmap(
                        QPixmap('图片//1.png'))
                    self.label2_2.setScaledContents(True)
                    self.label2_2.show()

                elif num == 2:

                    counter_2 += 1

                    pic = "图片/2.png"
                    self.label2_2 = QLabel(self.stack2)
                    self.label2_2.resize(300, 300)
                    self.label2_2.move(150 + (i-3) * 120, 500)
                    self.label2_2.setPixmap(
                        QPixmap('图片//2.png'))
                    self.label2_2.setScaledContents(True)
                    self.label2_2.show()

                elif num == 3:

                    counter_3 += 1

                    pic = "图片/3.png"
                    self.label2_2 = QLabel(self.stack2)
                    self.label2_2.resize(300, 300)
                    self.label2_2.move(150 + (i-3) * 120, 500)
                    self.label2_2.setPixmap(
                        QPixmap('图片//3.png'))
                    self.label2_2.setScaledContents(True)
                    self.label2_2.show()

                elif num == 4:

                    counter_4 += 1


                    pic = "图片/4.png"
                    self.label2_2 = QLabel(self.stack2)
                    self.label2_2.resize(300, 300)
                    self.label2_2.move(150 + (i-3) * 120, 500)
                    self.label2_2.setPixmap(
                        QPixmap('图片//4.png'))
                    self.label2_2.setScaledContents(True)
                    self.label2_2.show()

                elif num == 5:

                    counter_5 += 1

                    pic = "图片/5.png"
                    self.label2_2 = QLabel(self.stack2)
                    self.label2_2.resize(300, 300)
                    self.label2_2.move(150 + (i-3) * 120, 500)
                    self.label2_2.setPixmap(
                        QPixmap('图片//5.png'))
                    self.label2_2.setScaledContents(True)
                    self.label2_2.show()

                else:

                    counter_6 += 1

                    pic = "图片/6.png"
                    self.label2_2 = QLabel(self.stack2)
                    self.label2_2.resize(300, 300)
                    self.label2_2.move(150 + (i-3) * 120, 500)
                    self.label2_2.setPixmap(
                        QPixmap('图片//6.png'))
                    self.label2_2.setScaledContents(True)
                    self.label2_2.show()


        result_list = [counter_1, counter_2, counter_3, counter_4, counter_5, counter_6]

        print(result_list)


        #根据规则判断结果

        if result_list == self.liuBeiHei:
            print("六杯黑")
            self.lineedit2_3.setText("六杯黑")

        elif result_list == self.liuBeiHong:
            print("六杯红")
            self.lineedit2_3.setText("六杯红")

        elif result_list == self.zhuangYuan:
            print("状元")
            self.lineedit2_3.setText("状元")

        elif result_list == self.jinHua:
            print("状元插金花")
            self.lineedit2_3.setText("状元插金花")

        elif result_list == self.duiTang:
            print("对堂")
            self.lineedit2_3.setText("对堂")

        elif result_list[2] == 5:
            print("状元")
            self.lineedit2_3.setText("状元")

        elif result_list[2] == 4:
            print("四进")
            self.lineedit2_3.setText("四进")

        elif result_list[3] == 4:
            print("状元")
            self.lineedit2_3.setText("状元")

        elif result_list[3] == 3:
            print("三红")
            self.lineedit2_3.setText("三红")

        elif result_list[3] == 2:
            print("二举")
            self.lineedit2_3.setText("二举")

        elif result_list[3] == 1:
            print("一秀")
            self.lineedit2_3.setText("一秀")

        else:
            print("再接再厉")
            self.lineedit2_3.setText("再接再厉")

    #退出程序
    def Quit(self):
        app = QApplication.instance()
        app.quit()

    #返回首页
    def returnMain(self):
        self.stack.setCurrentIndex(0)

    #打开单人游戏界面
    def displaySingelWindow(self):
        self.stack.setCurrentIndex(1)#切换页面

    #打开多人游戏界面
    def displayMultiWindow(self):
        self.stack.setCurrentIndex(2)#切换页面




if __name__ == '__main__':
    app = 0
    app = QApplication(sys.argv)
    main = Bobing()
    main.show()
    sys.exit(app.exec_())