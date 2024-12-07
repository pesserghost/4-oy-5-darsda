import re
from datetime import datetime

class XatoQiymat(Exception):
    pass

class NotogriTelefonRaqamiXatolik(Exception):
    pass

class KuchsizParolXatolik(Exception):
    pass

class NotogriEmailXatolik(Exception):
    pass

class YoshKichikXatolik(Exception):
    pass

class ManfiyNarxXatolik(Exception):
    pass

class NotogriBosqichXatolik(Exception):
    pass

class NotogriSanaXatolik(Exception):
    pass

class Yosh:
    def __get__(self, obyekt, egasi):
        return obyekt.__dict__.get("yosh")

    def __set__(self, obyekt, qiymat):
        if not isinstance(qiymat, int) or qiymat <= 0:
            raise XatoQiymat("Yosh musbat butun son bo'lishi kerak.")
        obyekt.__dict__["yosh"] = qiymat

class TelefonRaqami:
    def __get__(self, obyekt, egasi):
        return obyekt.__dict__.get("telefon_raqami")

    def __set__(self, obyekt, qiymat):
        if not (qiymat.isdigit() and len(qiymat) in [9, 12]):
            raise NotogriTelefonRaqamiXatolik("Telefon raqami faqat raqamlardan iborat bo'lishi va uzunligi 9 yoki 12 bo'lishi kerak.")
        obyekt.__dict__["telefon_raqami"] = qiymat

class Parol:
    def __get__(self, obyekt, egasi):
        return obyekt.__dict__.get("parol")

    def __set__(self, obyekt, qiymat):
        if len(qiymat) < 8 or not any(c.isupper() for c in qiymat) or not any(c in "!@#$%^&*()-_=+[]{};:'\",.<>?/" for c in qiymat):
            raise KuchsizParolXatolik("Parol kamida 8 belgidan iborat bo'lishi, katta harf va maxsus belgi o'z ichiga olishi kerak.")
        obyekt.__dict__["parol"] = qiymat

class Email:
    def __get__(self, obyekt, egasi):
        return obyekt.__dict__.get("email")

    def __set__(self, obyekt, qiymat):
        if "@" not in qiymat or "." not in qiymat:
            raise NotogriEmailXatolik("Email manzili @ va . belgilarini o'z ichiga olishi kerak.")
        obyekt.__dict__["email"] = qiymat

class FaoliyatYillari:
    def __get__(self, obyekt, egasi):
        return obyekt.__dict__.get("faoliyat_yillari")

    def __set__(self, obyekt, tugilgan_yil):
        hozirgi_yil = datetime.now().year
        yosh = hozirgi_yil - tugilgan_yil
        if yosh < 16:
            raise YoshKichikXatolik("Foydalanuvchi yoshi 16 dan katta bo'lishi kerak.")
        obyekt.__dict__["faoliyat_yillari"] = yosh

class Narx:
    def __get__(self, obyekt, egasi):
        return obyekt.__dict__.get("narx")

    def __set__(self, obyekt, qiymat):
        if qiymat < 0:
            raise ManfiyNarxXatolik("Narx manfiy bo'lmasligi kerak.")
        obyekt.__dict__["narx"] = qiymat

class Bosqich:
    def __get__(self, obyekt, egasi):
        return obyekt.__dict__.get("bosqich")

    def __set__(self, obyekt, qiymat):
        if not (1 <= qiymat <= 12):
            raise NotogriBosqichXatolik("Bosqich 1 dan 12 gacha bo'lishi kerak.")
        obyekt.__dict__["bosqich"] = qiymat

class Sana:
    def __get__(self, obyekt, egasi):
        return obyekt.__dict__.get("sana")

    def __set__(self, obyekt, qiymat):
        try:
            datetime.strptime(qiymat, "%Y-%m-%d")
        except ValueError:
            raise NotogriSanaXatolik("Sana faqat YYYY-MM-DD formatida bo'lishi kerak.")
        obyekt.__dict__["sana"] = qiymat
class Foydalanuvchi:
    yosh = Yosh()
    telefon_raqami = TelefonRaqami()
    parol = Parol()
    email = Email()
    faoliyat_yillari = FaoliyatYillari()
    narx = Narx()
    bosqich = Bosqich()
    sana = Sana()

foydalanuvchi = Foydalanuvchi()
foydalanuvchi.yosh = 25
foydalanuvchi.telefon_raqami = "998901234567"
foydalanuvchi.parol = "Kuchli@123"
foydalanuvchi.email = "misol@gmail.com"
foydalanuvchi.faoliyat_yillari = 1995
foydalanuvchi.narx = 1000
foydalanuvchi.bosqich = 10
foydalanuvchi.sana = "2024-11-28"
print(foydalanuvchi.sana)

