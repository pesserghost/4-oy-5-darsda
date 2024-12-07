from decimal import Decimal
"""quyidagi masalalarni hammasi uchun bitta import ishlatilgan """
#
# son1 = Decimal(input("1-sonni kiriting: "))
# son2 = Decimal(input("2-sonni kiriting: "))
# yigindi = son1 + son2
# print("Yig‘indi:", yigindi)'
# 2
# narx = Decimal(input("Mahsulot narxini kiriting: "))
# chegirma_foizi = Decimal(input("Chegirma foizini kiriting: "))
# chegirma_miqdori = narx * chegirma_foizi / 100
# print("Chegirma miqdori:", chegirma_miqdori)
#3]
# son = Decimal(input("Sonni kiriting: "))
# yaxlitlangan_son = round(son, 2)
# print("Yaxlitlangan son:", yaxlitlangan_son)
#4]
# son1 = Decimal(input("1-sonni kiriting: "))
# son2 = Decimal(input("2-sonni kiriting: "))
# kattasi = max(son1, son2)
# print("Katta qiymat:", kattasi)
#5
# son1 = Decimal(input("1-sonni kiriting: "))
# son2 = Decimal(input("2-sonni kiriting: "))
# son3 = Decimal(input("3-sonni kiriting: "))
# yigindi = son1 + son2 + son3
# ayirma = son1 - son2 - son3
# bolinma = son1 / (son2 + son3)
# print("Yig‘indi:", yigindi)
# print("Ayirma:", ayirma)
# print("Bo‘linma:", bolinma)
#6
# son = Decimal(input("Sonni kiriting: "))
# valyuta_format = f"${son:,.2f}"
# print("Valyuta format:", valyuta_format)
#7
# narx = Decimal(input("Narxni kiriting: "))
# ikki_barobar = narx * 2
# print("Ikki barobar narx:", ikki_barobar)
#8
# son = Decimal(input("Sonni kiriting: "))
# kasr_qism = son - son.to_integral_value()
# print("Kasr qismi:", kasr_qism)
#
#9
# son = 7
# kub = pow(son, 3)
# print("Sonning kubi:", kub)
#10
# son = Decimal(input("Sonni kiriting: "))
# foiz_qism = son * 0.15
# print("15% qismi:", foiz_qism)
# RANDOM
#1
# import random
# raqam = random.randint(1, 1000)
# print("Tasodifiy raqam:", raqam)
#2
import random
# import string
# parol = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%", k=12))
# print("Tasodifiy parol:", parol)
#3
# import random
# tanga = random.choice(["Oq", "Gerb"])
# print("Tanga natijasi:", tanga)
#4
# lotereya = random.sample(range(1, 50), 6)
# print("Lotereya sonlari:", lotereya)
#5
# tasodifiy_sonlar = [random.randint(1, 1000) for _ in range(1000)]
# ortacha = sum(tasodifiy_sonlar) / len(tasodifiy_sonlar)
# print("O'rtacha qiymat:", ortacha)
# 6
# rang = tuple(random.randint(0, 255) for _ in range(3))
# print("Tasodifiy rang (RGB):", rang)
#7
# royxat = ['Olma', 'Banan', 'Olcha', 'Uzum', 'Anor']
# tanlangan = random.choice(royxat)
# print("Tanlangan element:", tanlangan)
#8
# royxat = ['Olma', 'Banan', 'Olcha', 'Uzum', 'Anor']
# random.shuffle(royxat)
# print("Aralashtirilgan ro'yxat:", royxat)

# math bilan ishlash
#1
import math
# son = 16
# ildiz = math.sqrt(son)
# print("Kvadrat ildiz:", ildiz)
#2
# burchak = math.radians(30)
# sin_qiymat = math.sin(burchak)
# cos_qiymat = math.cos(burchak)
# print("Sinusi:", sin_qiymat, "Kosinusi:", cos_qiymat)
#3
# asos = 10
# qiymat = 100
# logarifm = math.log(qiymat, asos)
# print("Logarifm:", logarifm)
#4
# son = 5
# faktorial = math.factorial(son)
# print("Faktorial:", faktorial)
# MASALALAR UCHUN IMPORT BIR MARTA ISHLATILDI












