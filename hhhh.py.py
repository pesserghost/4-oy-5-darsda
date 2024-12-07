from decimal import Decimal
from datetime import datetime
import random

class Mahsulot:
    def __init__(self, narx):
        self._narx = None
        self.narx = narx
        self.chegirma_foiz = random.randint(1, 50)
        self.sana = self.tasodifiy_sana()
    @property
    def narx(self):
        return self._narx
    @narx.setter
    def narx(self, qiymat:str):
        if qiymat.isdigit():
            try:
                qiymat = Decimal(qiymat)
                if qiymat <= 0:
                    raise ValueError("Narx manfiy yoki 0 bo‘lishi mumkin emas.")
                self._narx = qiymat
            except Exception:
                raise ValueError("Narx noto‘g‘ri formatda kiritilgan.")
        else:
            raise ValueError("Narx faqat raqam yoki matn ko‘rinishida bo‘lishi kerak.")

    @staticmethod
    def tasodifiy_sana():
        hozir = datetime.now()
        tasodifiy_kun = random.randint(0, 10)
        tasodifiy_soniya = tasodifiy_kun * 86400
        tasodifiy_vaqt = hozir.timestamp() - tasodifiy_soniya
        tasodifiy_sana = datetime.fromtimestamp(tasodifiy_vaqt)
        return tasodifiy_sana.strftime('%Y-%m-%d')
    def yangi_narx(self):
        chegirma = self.narx * Decimal(self.chegirma_foiz) / 100
        yangi_narx = self.narx - chegirma
        if yangi_narx < 0:
            raise ValueError("Chegirma noto‘g‘ri hisoblandi, natija manfiy bo‘lib qoldi.")
        return f"Yangi narx: {yangi_narx} UZS (Sana: {self.sana}) Foyizi {self.chegirma_foiz} foizd {self.chegirma_foiz * yangi_narx /100}"


mahsulot = Mahsulot("100000")
print(mahsulot.yangi_narx())

# 1
from decimal import Decimal
from datetime import datetime
import random

class Mahsulot:
    def __init__(self, narx):
        self._narx = None
        self.narx = narx  # Setter orqali narxni o‘rnatish
        self.sana = self.tasodifiy_sana()

    @property
    def narx(self):
        return self._narx

    @narx.setter
    def narx(self, qiymat):
        # Agar qiymat matn bo‘lsa, uni raqamga aylantirishga urinadi
        if isinstance(qiymat, str) and qiymat.isdigit():
            qiymat = Decimal(qiymat)

        # Agar qiymat Decimal bo‘lmasa, xato chiqaradi
        elif not isinstance(qiymat, Decimal):
            raise ValueError("Narx faqat musbat raqam ko‘rinishida bo‘lishi kerak.")

        # Narx musbat ekanligini tekshirish
        if qiymat <= 0:
            raise ValueError("Narx manfiy yoki 0 bo‘lishi mumkin emas.")

        # To‘g‘ri qiymat bo‘lsa, saqlash
        self._narx = qiymat

    @staticmethod
    def tasodifiy_sana():
        hozir = datetime.now()
        tasodifiy_kun = random.randint(0, 10)  # 0 dan 10 kungacha tasodifiy kun
        tasodifiy_soniya = tasodifiy_kun * 86400  # Kunlarni soniyaga aylantirish
        tasodifiy_vaqt = hozir.timestamp() - tasodifiy_soniya
        tasodifiy_sana = datetime.fromtimestamp(tasodifiy_vaqt)
        return tasodifiy_sana.strftime('%Y-%m-%d')

    def yangi_narx(self):

        yangi_narx = self.narx * 12000

        if self.narx < 0:
            raise ValueError("Chegirma noto‘g‘ri hisoblandi, natija manfiy bo‘lib qoldi.")

        return f"Yangi narx: {yangi_narx} UZS (Sana: {self.sana})"


usd = input("Usd ni kiritng : ")
mahsulot = Mahsulot(usd)
print(mahsulot.yangi_narx())  # 20% chegirma bilan yangi narxni hisoblash
