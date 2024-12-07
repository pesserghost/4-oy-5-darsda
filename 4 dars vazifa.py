# class LowerCaseDescriptor:
#     def __get__(self, instance, owner):
#         return self.value
#     def __set__(self, instance, value):
#         self.value = value.lower()
#     def __delete__(self, instance):
#         del self.value
# class User:
#     name = LowerCaseDescriptor()
#     def __init__(self, name):
#         self.name = name
# class Product:
#     title = LowerCaseDescriptor()
#     def __init__(self, title):
#         self.title = title
# user = User("Ali")
# print(user.name)
# product = Product("Laptop")
# print(product.title)
# user.name = "Zuhra"
# print(user.name)
# product.title = "Smartphone"
# print(product.title)
#2
# class MusbatQiymat:
#     def __init__(self):
#         self._qiymat = 0
#     def __get__(self, instance, owner):
#         return self._qiymat
#     def __set__(self, instance, qiymat):
#         if qiymat < 0:
#             raise ValueError("Qiymat musbat bo'lishi kerak!")
#         self._qiymat = qiymat
#     def __delete__(self, instance):
#         del self._qiymat
# class MeningKlassim:
#     musbat_qiymat = MusbatQiymat()
# obyekt = MeningKlassim()
# obyekt.musbat_qiymat = 10
# print(obyekt.musbat_qiymat)
# try:
#     obyekt.musbat_qiymat = -5  # Xato
# except ValueError as xato:
#     print(xato)
#3  DATATIME MODULI
#1
# from datetime import datetime, timedelta
# bugungi_sana = datetime.now().date()
# print(f"Bugungi sana: {bugungi_sana}")
# yetti_kun_oldin = bugungi_sana - timedelta(days=7)
# print(f"7 kun oldin: {yetti_kun_oldin}")
# yetti_kun_keyin = bugungi_sana + timedelta(days=7)
# print(f"7 kun keyin: {yetti_kun_keyin}")

#2
# from datetime import datetime
# tugilgan_yil = int(input("Tug‘ilgan yilingizni kiriting: "))
# tugilgan_oy = int(input("Tug‘ilgan oyingizni kiriting (1-12): "))
# tugilgan_kun = int(input("Tug‘ilgan kuningizni kiriting (1-31): "))
# bugungi_sana = datetime.now()
# tugilgan_sana = datetime(year=tugilgan_yil, month=tugilgan_oy, day=tugilgan_kun)
# yosh = bugungi_sana.year - tugilgan_yil
# if (bugungi_sana.month, bugungi_sana.day) < (tugilgan_sana.month, tugilgan_sana.day):
#     yosh -= 1
# if (bugungi_sana.month, bugungi_sana.day) == (tugilgan_sana.month, tugilgan_sana.day):
#     print("Tug‘ilgan kuningiz bilan!")
# else:
#     print(f"Sizning yoshingiz: {yosh}")
#
#3
# from datetime import datetime
# vaqt_format = "%H:%M:%S"  # Soat:daqiqa:soniya
# vaqt1 = input("Birinchi vaqtni kiriting (HH:MM:SS formatda): ")
# vaqt2 = input("Ikkinchi vaqtni kiriting (HH:MM:SS formatda): ")
# vaqt1_obj = datetime.strptime(vaqt1, vaqt_format)
# vaqt2_obj = datetime.strptime(vaqt2, vaqt_format)
# vaqt_farqi = abs((vaqt2_obj - vaqt1_obj).total_seconds())
# print(f"Vaqt oralig'idagi jami soniyalar: {int(vaqt_farqi)}")

#math moduli
#1
# import math
# diametr = float(input("Aylananing diametrini kiriting: "))
# radius = diametr / 2
# yuza = math.pi * (radius ** 2)
# print(f"Aylananing yuzasi: {yuza:.2f}")
#2
# import math
# son = float(input("Biror sonni kiriting: "))
# if son < 0:
#     raise ValueError("Son manfiy bo'lishi mumkin emas!")
# kvadrat_ildiz = math.sqrt(son)
# kub_ildiz = son ** (1/3)
# print(f"Sonning kvadrat ildizi: {kvadrat_ildiz:.2f}")
# print(f"Sonning kub ildizi: {kub_ildiz:.2f}")
# random moduli
#1
# import random
# butun_sonlar = [random.randint(1, 100) for _ in range(5)]
# haqiqiy_sonlar = [random.uniform(0, 1) for _ in range(3)]
# butun_sonlar_ortacha = sum(butun_sonlar) / len(butun_sonlar)
# haqiqiy_sonlar_ortacha = sum(haqiqiy_sonlar) / len(haqiqiy_sonlar)
# print(f"Butun sonlar: {butun_sonlar}")
# print(f"Haqiqiy sonlar: {haqiqiy_sonlar}")
# print(f"Butun sonlarning o'rtacha qiymati: {butun_sonlar_ortacha:.2f}")
# print(f"Haqiqiy sonlarning o'rtacha qiymati: {haqiqiy_sonlar_ortacha:.2f}")
