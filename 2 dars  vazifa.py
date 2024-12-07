# 1 masala
# from datetime import datetime
# hozirgi_sana = datetime.now()
# print("Hozirgi sana:", hozirgi_sana)
#--------------
# 2 masala
# from datetime import datetime
# hozirgi_vaqt = datetime.now().time()
# print("Hozirgi vaqt:", hozirgi_vaqt.strftime("%H:%M:%S"))
#---------------
# 3 masala
# from datetime import datetime
# hozirgi_sana = datetime.now()
# formatlangan_sana = hozirgi_sana.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatlangan sana:", formatlangan_sana)
#---------------
# 4 masala
# from datetime import datetime
# kiritilgan_sana = input("Sanani YYYY-MM-DD formatida kiriting: ")
# kiritilgan_sana_obj = datetime.strptime(kiritilgan_sana, "%Y-%m-%d")
# hafta_kuni = kiritilgan_sana_obj.strftime("%A")
# print("Bu sana haftaning", hafta_kuni, "kuniga to'g'ri keladi.")
# --------------
#5 masala
# import time
# sekund = int(input("Taymer uchun soniyalarni kiriting: "))
# print("Taymer boshlandi...")
# time.sleep(sekund)
# print("Vaqt tugadi!")
# ----------
# 6 masala
# from datetime import datetime
# tugilgan_kun = input("Tug'ilgan kuningizni YYYY-MM-DD formatida kiriting: ")
# tugilgan_kun_obj = datetime.strptime(tugilgan_kun, "%Y-%m-%d")
# bugungi_kun = datetime.now()
# farq = bugungi_kun - tugilgan_kun_obj
# print(f"Sizning tug'ilganingizdan {farq.days} kun o'tdi.")
#----------------
# 7 masala
# from datetime import datetime
# bugungi_kun = datetime.now()
# faqat_sana = bugungi_kun.strftime("%Y-%m-%d")
# print("Bugungi sana:", faqat_sana)
#-----
# 8 masala
# from datetime import datetime
# bugungi_kun = datetime.now()
# hafta_kuni = bugungi_kun.weekday()
# if hafta_kuni in [5, 6]:
#     print("Bugun hafta oxiri.")
# else:
#     print("Bugun ish kuni.")
#--------------
# 9 masal
# from datetime import datetime
# sana1 = input("Birinchi sanani YYYY-MM-DD formatida kiriting: ")
# sana2 = input("Ikkinchi sanani YYYY-MM-DD formatida kiriting: ")
# sana1_obj = datetime.strptime(sana1, "%Y-%m-%d")
# sana2_obj = datetime.strptime(sana2, "%Y-%m-%d")
# farq = abs((sana2_obj - sana1_obj).days)
# print(f"Ikki sana orasida {farq} kun bor.")
#------------
# 10 masala
# from datetime import datetime
# hozirgi_sana = datetime.now()
# datetime_str = hozirgi_sana.strftime("%Y-%m-%d %H:%M:%S")
# print("Satrdagi sana va vaqt:", datetime_str)
# qayta_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
# print("Qayta obyekt:", qayta_datetime)
# --------------------
# 11 masala
# oy = int(input("Sanadagi oy raqamini kiriting (1-12): "))
# if oy in [12, 1, 2]:
#     print("Qish fasli.")
# elif oy in [3, 4, 5]:
#     print("Bahor fasli.")
# elif oy in [6, 7, 8]:
#     print("Yoz fasli.")
# elif oy in [9, 10, 11]:
#     print("Kuz fasli.")
# else:
#     print("Noto'g'ri oy raqami.")
#----------------
# 12 masala
# from datetime import datetime
# bugungi_kun = datetime.now()
# yangi_yil = datetime(year=bugungi_kun.year + 1, month=1, day=1)
# qolgan_vaqt = yangi_yil - bugungi_kun
# print(f"Yangi yilgacha {qolgan_vaqt.days} kun qoldi.")
#----------------
# 13 masala
# import time
# kutish_vaqti = int(input("Necha soniya kutishni xohlaysiz? "))
# print("Kutilmoqda...")
# time.sleep(kutish_vaqti)
# print("Davom etamiz!")
############-----------
# 14 masala
# import time
# intervalli = int(input("Qayta bajarish oraliq vaqtini (soniyada) kiriting: "))
# for i in range(5):
#     print(f"{i+1}-marta: Davom etmoqda...")
#     time.sleep(intervalli)
# print("Davriy amal tugadi.")
#
# THANK YOU FOR ,,E'TIBOR"





