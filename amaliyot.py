
from decimal import Decimal, InvalidOperation
from datetime import datetime, timedelta
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
    def narx(self, qiymat):
        try:
            qiymat = Decimal(qiymat)
            if qiymat <= 0:
                raise ValueError("Narx manfiy yoki 0 bo‘lishi mumkin emas.")
            self._narx = qiymat
        except (InvalidOperation, TypeError):
            raise ValueError("Narx to‘g‘ri formatda kiritilishi kerak (raqam).")

    @staticmethod
    def tasodifiy_sana():
        bugun = datetime.now()
        tasodifiy_kun = bugun - timedelta(days=random.randint(0, 10))
        return tasodifiy_kun.strftime('%Y-%m-%d')

    def yangi_narx(self):
        chegirma = self.narx * Decimal(self.chegirma_foiz) / 100
        yangi_narx = self.narx - chegirma
        if yangi_narx < 0:
            raise ValueError("Chegirma noto‘g‘ri hisoblandi, natija manfiy bo‘ldi.")
        return yangi_narx

    def natija(self):
        yangi_narx = self.yangi_narx()
        return f"Yangi narx: {yangi_narx} UZS (Sana: {self.sana})"

# Foydalanish misoli
try:
    mahsulot = Mahsulot("100000")  # Mahsulot narxi: 100000 UZS
    print(f"Mahsulot narxi: {mahsulot.narx} UZS, chegirma: {mahsulot.chegirma_foiz}%")
    print(mahsulot.natija())
except ValueError as xato:
    print(f"Xato: {xato}")


