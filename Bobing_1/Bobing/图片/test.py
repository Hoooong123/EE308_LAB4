import sys
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

    def initUI(self):
        self.setWindowTitle('中秋博饼')
        self.setFixedSize(1672,941)
        self.setWindowIcon(QIcon('图片/软件图标.png'))

        self.stack = QStackedWidget(self)
        self.setCentralWidget(self.stack)

        self.setMainWindow()  #首页

        self.setSingleWindow()

    #1.首页
    def setMainWindow(self):
        self.stack1 = QWidget()
        self.stack1.setGeometry(0,0,1672,941)
        self.stack1.setObjectName('MainWindow')
        style = '''
                    #MainWindow{
                        border-image:url('图片/主页面.png');
                    }
                '''
        self.stack1.setStyleSheet(style)
        self.stack.addWidget(self.stack1)

        #1.1退出程序
        self.button1_1 = QPushButton(self.stack1)
        self.button1_1.move(1030, 660)
        self.button1_1.setMaximumSize(450, 300)
        self.button1_1.setMinimumSize(450, 300)
        self.button1_1.setObjectName('button1_1')
        style = '''
                            #button1_1{
                                border-radius:4px;
                                background-image:url('图片/退出程序.png');
                            }
                        '''
        self.button1_1.setStyleSheet(style)
        self.button1_1.clicked.connect(self.Quit)



        #1.2单人1.3多人按钮

        #单人游戏
        self.button1_2 = QPushButton(self.stack1)
        self.button1_2.move(985, 505)
        self.button1_2.setMaximumSize(400, 300)
        self.button1_2.setMinimumSize(400, 300)
        self.button1_2.setObjectName('button1_2')
        style = '''
                    #button1_2{
                        border-radius:4px;
                        background-image:url('图片/干员寻访.png');
                    }
                '''
        self.button1_2.setStyleSheet(style)
        #跳转
        self.button1_2.clicked.connect(self.displaySingelWindow)




        #公开招募
        self.button1_3 = QPushButton(self.stack1)
        self.button1_3.move(1285, 520)
        self.button1_3.setMaximumSize(400, 300)
        self.button1_3.setMinimumSize(400, 300)
        self.button1_3.setObjectName('button1_3')
        style = '''
                            #button1_3{
                                border-radius:4px;
                                background-image:url('图片/公开招募.png');
                            }
                        '''
        self.button1_3.setStyleSheet(style)
        #跳转
        #self.button1_3.clicked.connect(self.showPublicOffer)

        #1.4.设置图标
        self.button1_4 = QPushButton(self.stack1)
        self.button1_4.move(10,-2)
        self.button1_4.setMaximumSize(100,100)
        self.button1_4.setMinimumSize(100,100)
        self.button1_4.setObjectName('button1_4')
        style = '''
            #button1_4{
                border-radius:4px;
                background-image:url('图片/设置.png');
            }
        '''
        self.button1_4.setStyleSheet(style)
        self.button1_4.clicked.connect(self.Button1_4Clicked)

        #1.5设置界面
        #设置界面
        self.widget1_1 = QWidget(self.stack1)
        self.widget1_1.setGeometry(0,-5,1672,941)
        self.widget1_1.setObjectName('widget1_1')
        style = '''
                    #widget1_1{
                        border-image:url('图片/设置页面.png');
                    }
                '''
        self.widget1_1.setStyleSheet(style)
        #默认隐藏设置页面
        self.widget1_1.hide()

        #1.6返回按钮
        self.button1_12 = QPushButton(self.widget1_1)
        self.button1_12.setGeometry(0,0,200,100)
        self.button1_12.setObjectName('button1_12')
        style = '''
                                                    #button1_12{
                                                        border-radius:4px;
                                                        background-image:url('图片/返回按钮.png');
                                                    }
                                                '''
        self.button1_12.setStyleSheet(style)
        self.button1_12.clicked.connect(self.Button1_12Clicked)





    #2.单人游戏界面
    def setSingleWindow(self):

        #规则

        #self.resultDic = {'六':{},'五':{},'四':{},'三':{},'二':{},'一':{}}



        self.stack2 = QWidget()
        self.stack2.setGeometry(0,0,1672,941)
        self.stack2.setObjectName('SearchWindow')
        style = '''
                        #SearchWindow{
                            border-image:url('图片/游戏界面.jpg');
                        }
                    '''
        self.stack2.setStyleSheet(style)
        self.stack.addWidget(self.stack2)

        #单人模式图标
        self.label2_1 = QLabel(self.stack2)
        self.label2_1.move(600,200)
        self.label2_1.setPixmap(QPixmap('图片/单人模式.png'))


        #返回按钮
        self.button2_1 = QPushButton(self.stack2)
        self.button2_1.move(0,0)
        self.button2_1.setMaximumSize(200,100)
        self.button2_1.setMinimumSize(200,100)
        self.button2_1.setObjectName('button2_1')
        style = '''
            #button2_1{
                border-radius:4px;
                background-image:url('图片/返回按钮.png');
            }
        '''
        self.button2_1.setStyleSheet(style)
        self.button2_1.clicked.connect(self.returnMain)


        #开始摇骰子按钮
        self.button2_2 = QPushButton(self.stack2)
        self.button2_2.move(100,100)
        self.button2_2.setMaximumSize(400, 300)
        self.button2_2.setMinimumSize(400, 300)
        self.button2_2.setObjectName('button2_2')
        style = '''
            #button2_2{
                border-radius:4px;
                background-image:url('图片/干员寻访.png');
            }
        '''
        self.button2_2.setStyleSheet(style)



        pic=self.button2_2.clicked.connect(self.fault_show_function)






        #重置按钮
        self.button2_3 = QPushButton(self.stack2)
        self.button2_3.move(240,280)
        self.button2_3.setMaximumSize(200,100)
        self.button2_3.setMinimumSize(200,100)
        self.button2_3.setObjectName('button2_3')
        style = '''
            #button2_3{
                border-radius:4px;
                background-image:url('图片/抽卡重置.png');
            }
        '''
        self.button2_3.setStyleSheet(style)
        self.button2_3.clicked.connect(self.reset)






    def reset(self):
        num = num = random.randrange(1,7,1)
        self.label2_2.hide()


    #随机数
    def randomNum(self):
        self.label2_2.show()

    #设置
    def Button1_4Clicked(self):
        self.widget1_1.show()
    def Button1_12Clicked(self):
        self.widget1_1.hide()

    #跳出窗口
    def fault_show_function(self):
        num = random.randrange(1,7,1)
        if num == 1:
            pic = "图片/1.png"
            self.label2_2 = QLabel(self.stack2)
            self.label2_2.move(400,100)
            self.label2_2.setPixmap(QPixmap('图片/1.png'))
            self.label2_2.show()
        elif num == 2:
            pic = "图片/2.png"
            self.label2_2 = QLabel(self.stack2)
            self.label2_2.move(400,100)
            self.label2_2.setPixmap(QPixmap('图片/2.png'))
            self.label2_2.show()
        elif num == 3:
            pic = "图片/3.png"
            self.label2_2 = QLabel(self.stack2)
            self.label2_2.move(400,100)
            self.label2_2.setPixmap(QPixmap('图片/3.png'))
            self.label2_2.show()
        elif num == 4:
            pic = "图片/4.png"
            self.label2_2 = QLabel(self.stack2)
            self.label2_2.move(400,100)
            self.label2_2.setPixmap(QPixmap('图片/4.png'))
            self.label2_2.show()
        elif num == 5:
            pic = "图片/5.png"
            self.label2_2 = QLabel(self.stack2)
            self.label2_2.move(400,100)
            self.label2_2.setPixmap(QPixmap('图片/5.png'))
            self.label2_2.show()
        else:
            pic = "图片/6.png"
            self.label2_2 = QLabel(self.stack2)
            self.label2_2.move(400,100)
            self.label2_2.setPixmap(QPixmap('图片/6.png'))
            self.label2_2.show()


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




if __name__ == '__main__':
    app = 0
    app = QApplication(sys.argv)
    main = Bobing()
    main.show()
    sys.exit(app.exec_())
