# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:07:33 2024

@author: Admin
"""

a=int(input("Nhập số nguyên a:"))
b=int(input("Nhập số nguyên b:"))
# Tính tổng , hiệu , tích
tong = a + b
hieu = a - b
tich = a * b
if b != 0:
    thuong_2cs = round(a / b, 2)
    thuong_3cs = round(a / b, 3)
    chia_lay_du = a % b
    chia_lay_nguyen = a // b
    print(f"Tổng: {tong}")
    print(f"Hiệu: {hieu}") 
    print(f"Tích: {tich}")
    print(f"Thương ( làm tròn 2 chữ số ): {thuong_2cs}")
    print(f"Thương ( làm tròn 3 chữ số ): {thuong_3cs}")
    print(f"Chia lấy dư: {chia_lay_du}")
    print(f"Chia lấy nguyên: {chia_lay_nguyen}")
else :
    print("Không thể chia cho 0")
    
    