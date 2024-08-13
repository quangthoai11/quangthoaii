# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:40:54 2024

@author: Thoai
"""

a = float(input("Nhập giá trị của a:"))
b = float(input("Nhập giá trị của b:"))
c = float(input("Nhập giá trị của c:"))
if a+b>c or a+c>b or b+c>a:
    print("Đây là ba cạnh của một tam giác")
    if a == b == c:
      print("Đây là tam giác đều")
    elif a==b and b==c and a==c :
      print ("Đây là tam giác cân")
    elif a**2==b**2+c**2 or c**2==a**2+b**2 or b**2==a**2+c**2:
      print ("Đây là một tam giác vuông")
    else:
      print ("Đây là tam giác thường")
else:
    print ("a,b,c không phải là ba cạnh một tam giác")
      