from django.db import models

class Goods(models.Model):
    goodsname = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.goodsname