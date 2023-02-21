from django.db import models

# Create your models here.

class Stock(models.Model):
    stock_name = models.CharField(max_length=16, verbose_name='STOCK_NAME')
    stock_code = models.CharField(max_length=16, verbose_name='STOCK_CODE')
    stock_open_price = models.IntegerField(verbose_name='STOCK_OPEN_PRICE')
    stock_high_price = models.IntegerField(verbose_name='STOCK_HIGH_PRICE')
    stock_low_price = models.IntegerField(verbose_name='STOCK_LOW_PRICE')
    stock_close_price = models.IntegerField(verbose_name='STOCK_CLOSE_PRICE')
    stock_volume = models.IntegerField(verbose_name='STOCK_VOLUME')
    stock_amount = models.IntegerField(verbose_name='STOCK_AMOUNT')
    stock_change_rate = models.IntegerField(verbose_name='STOCK_CHANGE_RATE')

    class Meta:
        db_table='shinhan_stock'
        verbose_name = '주식정보'
        verbose_name_plural = '주식정보'


class Cart(models.Model):
    user = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name='사용자')
    stock = models.ForeignKey('stock.Stock', on_delete=models.CASCADE, verbose_name='주식')
    cart = models.IntegerField(verbose_name='카트')
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시') # tstamp을 이용한 일정기간 후 카트 삭제

    class Meta:
        db_table = 'shinhan_stock_cart'
        verbose_name = '알파 카트'
        verbose_name_plural = '알파 카트'