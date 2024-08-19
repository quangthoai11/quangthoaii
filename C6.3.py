# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:33:57 2024

@author: Admin
"""

N=int(input("Nhập số nguyên dương N có 2 chữ số:"))
if N >= 10 and N <= 99:
 hang_don_vi = N%10
 hang_chuc = N//10
 Tong = hang_chuc+hang_don_vi
 print("Tổng các chữ số của N là:" , Tong)
 
