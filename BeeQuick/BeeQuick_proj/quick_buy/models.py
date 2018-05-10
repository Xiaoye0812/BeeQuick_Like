from django.db import models

from order.models import OrderModel


class GoodType(models.Model):
    # 商品类别
    type_id = models.IntegerField(primary_key=True)  # 分类id
    type_name = models.CharField(max_length=100)  # 分类名称
    child_type_names = models.CharField(max_length=200)  # 子商品名称
    type_sort = models.IntegerField(default=1)  # 排序编号

    class Meta:
        db_table = 'tb_good_types'
