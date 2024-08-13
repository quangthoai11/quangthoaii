# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:34:08 2024

@author: Thoai
"""

import math

a = float(input("Nhập giá trị của a:"))
b = float(input("Nhập giá trị của b:"))
c = float(input("Nhập giá trị của c:"))
print("{0}x^2+{1}x+{2}=0".format(a,b,c))
delta = b**2 - 4*a*c
if (a!=0):
    if (delta<0):
        print("Phuong trinh VN")
    elif (delta==0):
        x=-b/2*a
        print("Pt có nghiệm kép x1=x2=",x)
    else:
      x1 = (-b+math.sqrt(delta))/(2*a)
      x2 = (-b-math.sqrt(delta))/(2*a)
      print("Pt có nghiệm x1={0} va x2={1}".format(x1, x2))
      