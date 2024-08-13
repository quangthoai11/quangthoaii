# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:19:43 2024

@author: Thoai
"""

a=float(input("Nhập giá trị của a:"))
b=float(input("Nhập giá trị của b:"))
if a==0:
   if b==0:
    print("Phương trình có vô số nghiệm")
   else:
     print("Phương trình vô nghiệm") 
else:
    x=-b/a

    print("Phương trình có 1 nghiệm x=" , x)
    