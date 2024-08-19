# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:54:49 2024

@author: Admin
"""
gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
sg=3600
tong_giay = gio * 3600 + phut * 60 + giay
print("Tổng số giây là:" , tong_giay)



