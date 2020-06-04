import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

A = cv.imread('/home/bingyang/wby/1/1.png')
B = cv.imread('/home/bingyang/wby/1/2.png')

G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)

G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)


lpA = [gpA[5]]
for i in range(5, 0, -1):
    GE = cv.pyrUp(gpA[i])

    L = cv.subtract(gpA[i-1], GE)
    lpA.append(L)


lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i-1], GE)
    lpB.append(L)


LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:,0:cols//2,:], lb[:, cols//2:,:]))
    LS.append(ls)

ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])


real = np.hstack((A[:,:cols//2], B[:, cols//2:]))
cv.imwrite('/home/bingyang/wby/1/3.png',real)
cv.imshow('apple', A)
cv.imshow('orange', B)
cv.imshow('direct', real)
cv.imshow('pyramid', ls_)
