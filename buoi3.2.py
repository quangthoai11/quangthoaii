# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:10:29 2024

@author: Thoai
"""

GPA = float(input("Nhập điểm trung bình(GPA):"))
if GPA < 3.5:
    print("Học lực kém")
elif GPA <= 3.5 and GPA <5.0:
    print("Học lực yếu")
elif GPA <= 5.0 and GPA <7.0:
    print("Học lực trung bình")
elif GPA <= 7.0 and GPA <8.0:
    print("Học lực khá")
elif GPA <= 8.0 and GPA <9.0:
    print("Học lực giỏi")
else:
    print("Học lực xuất sắc")
