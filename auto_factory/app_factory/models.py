from django.db import models


class Detail(models.Model):
    """Auto detail model"""

    types = (
        ('ФАРА', 'фара'),
        ('РЕШЁТКА', 'решётка'),
        ('РУЧКА', 'ручка'),
        ('КАПОТ', 'капот'),
        ('РУЛЬ', 'руль'),
        ('КРЕСЛО', 'кресло'),
    )

    detail_type = models.CharField("Деталь", max_length=255, choices=types, null=False, blank=False)
    price = models.DecimalField('Цена', default=0, decimal_places=2, max_digits=11, blank=False)

    class META:
        verbose_name = 'Detail'
        verbose_name_plural = 'Detail'

    def __str__(self):
        return self.detail_type


class CurrentAutoDetail(models.Model):
    """Model to Expand Detail for current car"""
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantity', default=1)
    parameter = models.TextField('Parameters', max_length=250, blank=True)

    class META:
        verbose_name = 'CurrentAutoDetail'
        verbose_name_plural = 'CurrentAutoDetail'

    def __str__(self):
        return f'{self.detail.detail_type} - {self.quantity} - {self.detail.price}'

    def get_total_price(self):
        return self.quantity * self.detail.price


class Auto(models.Model):
    """Car model"""
    name = models.CharField('Название', max_length=100, null=False, blank=False)
    markup = models.FloatField('Наценка %', default=0, null=False, blank=False)
    parts = models.ManyToManyField(CurrentAutoDetail)

    class META:
        verbose_name = 'Auto'
        verbose_name_plural = 'Auto'

    def __str__(self):
        return self.name

    def get_total_price(self):
        sql = Auto.objects.filter(pk=self.pk).only('parts__detail__detail_type', 'parts__quantity').values(
            'parts__detail__detail_type', 'parts__quantity', 'parts__detail__price')
        return sum(list(map(lambda item: item['parts__quantity'] * int(item['parts__detail__price']), sql))) * (
                self.markup / 100 + 1)


class AutoPrice(models.Model):
    """Модель расчета стоимости и сохранения информациии в бд"""
    created_at = models.DateTimeField("Crated at", auto_now_add=True)
    auto_name = models.ForeignKey(Auto, on_delete=models.CASCADE)
    price = models.DecimalField('Цена', default=0, decimal_places=2, max_digits=12, blank=False)

    def save(self, *args, **kwargs):
        self.price = self.auto_name.get_total_price()
        super().save(*args, **kwargs)

    class META:
        verbose_name = 'AutoPrice'
        verbose_name_plural = 'AutoPrice'

    def __str__(self):
        return self.auto_name.name
