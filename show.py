import sys
import os
import time 
import math

import numpy as np 
import cv2 as cv

from PIL import Image
from matplotlib import pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class myapp(QWidget):

    def __init__(self):
        super(myapp,self).__init__()
        self.InitUI()

    def InitUI(self):
        #禁止最大化按钮
        self.setFixedSize(1900, 700)
        self.setWindowTitle("Image Fusion")

        self.ori_area1 = QLabel(self)
        self.ori_area1.setStyleSheet("QLabel{background:white;}")
        self.ori_area1.setGeometry(250,50,512,512)

        self.ori_area2 = QLabel(self)
        self.ori_area2.setStyleSheet("QLabel{background:white;}")
        self.ori_area2.setGeometry(800,50,512,512)

        self.ori_area3 = QLabel(self)
        self.ori_area3.setStyleSheet("QLabel{background:white;}")
        self.ori_area3.setGeometry(1350,50,512,512)




        select_btn = QPushButton(self)
        select_btn.setText("Wavelet")
        select_btn.setGeometry(50,50,150,50)
        select_btn.clicked.connect(self.selectimg1)

        select_btn = QPushButton(self)
        select_btn.setText("Laplace")
        select_btn.setGeometry(50, 150, 150, 50)
        select_btn.clicked.connect(self.selectimg2)

        select_btn = QPushButton(self)
        select_btn.setText("DenseFuse")
        select_btn.setGeometry(50,250,150,50)
        select_btn.clicked.connect(self.selectimg3)

        select_btn = QPushButton(self)
        select_btn.setText("DeepFuse")
        select_btn.setGeometry(50, 350, 150, 50)
        select_btn.clicked.connect(self.selectimg4)

        select_btn = QPushButton(self)
        select_btn.setText("PCA")
        select_btn.setGeometry(50, 450, 150, 50)
        select_btn.clicked.connect(self.selectimg5)

        #add images
        select_btn = QPushButton(self)
        select_btn.setText("Select")
        select_btn.setGeometry(660, 562, 100, 50)
        select_btn.clicked.connect(self.selectimg6)

        select_btn = QPushButton(self)
        select_btn.setText("Select")
        select_btn.setGeometry(1212, 562, 100, 50)
        select_btn.clicked.connect(self.selectimg7)

        select_btn = QPushButton(self)
        select_btn.setText("Fuse")
        select_btn.setGeometry(1760, 562, 100, 50)
        select_btn.clicked.connect(self.selectimg8)
        #select_btn = QPushButton(self)
        #select_btn.setText("Select")
        #select_btn.setGeometry(1450, 450, 100, 50)
        #select_btn.clicked.connect(self.selectimg8)
    #def openimage(self):
    #    imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
    #    jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
    #    self.label.setPixmap(jpg)
    def selectimg1(self):
        os.system("python wavelet.py")
        print("Done!")

    def selectimg2(self):
        #os.system("cd data/ImageFusion-master")
        os.system("python laplace.py")
        print("Done!")
#        os.system("python xiaobo1.py")
#        os.system("python xiaobo1.py")

    def selectimg3(self):
        #os.system("cd ~")
        #os.system("ls")
        ##os.system("cd data")
        #os.system("cd data/imagefusion_densefuse-master")
        #os.system("ls")
        os.system("python data/imagefusion_densefuse-master/main.py")
        #os.system("python xiaobo1.py")
        print("Done!")
        #os.system("python xiaobo1.py")

    def selectimg4(self):
        os.system("python data/Imagefusion_deepfuse-master/main.py")
        print("Done!")

    def selectimg5(self):
        os.system("python pca.py")
        print("Done!")

    def selectimg6(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.png;;*.jpg;;*.tif;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.ori_area1.width(), self.ori_area1.height())
        jpg.save('/home/bingyang/wby/1/1.tif')
        jpg.save('/home/bingyang/wby/1/1.png')
        #jpg.save('/home/bingyang/wby/1/2.tif')
        #jpg.save('/home/bingyang/wby/1/1.tif')
        self.ori_area1.setPixmap(jpg)

    def selectimg7(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.png;;*.jpg;;*.tif;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.ori_area2.width(), self.ori_area2.height())
        jpg.save('/home/bingyang/wby/1/2.tif')
        jpg.save('/home/bingyang/wby/1/2.png')

        self.ori_area2.setPixmap(jpg)

    def selectimg8(self):
        #p=QtGui.QPixmap()
        #p.load(('/home/wby/1/3.jpg'))
        jpg=QtGui.QPixmap('/home/bingyang/wby/1/3.png').scaled(self.ori_area3.width(), self.ori_area3.height())
        self.ori_area3.setPixmap(jpg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #myapp.direc = 4
    ex = myapp()
    ex.show()
    sys.exit(app.exec_())
