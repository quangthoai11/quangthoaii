# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:12:59 2024

@author: Admin
"""

from datetime import datetime
namsinh=int(input("Nhập năm sinh của bạn:"))
namhientai=datetime.now().year
tuoi=namhientai-namsinh
print(f"bạn sinh năm {namsinh} vậy bạn tuổi {tuoi}:")
