from django.db import models

from quick_buy.models import GoodType
from order.models import OrderModel


class GoodModel(models.Model):
    id = models.IntegerField(primary_key=True)

    is_xf = models.IntegerField(default=1)
    pm_desc = models.CharField(max_length=100)
    dealer_id = models.CharField(max_length=16)

    specifics = models.CharField(max_length=100)  # 规格

    category = models.ForeignKey(GoodType)  # 类别id
    child_cid = models.CharField(max_length=16)  # 子类别id
    child_cid_name = models.CharField(max_length=100)  # 子类别名称

    store_num = models.IntegerField(default=1)  # 排序编号
    product_num = models.IntegerField(default=1)  # 销量排序

    product_id = models.CharField(max_length=16)  # 产品id
    product_img = models.CharField(max_length=200)  # 产品图片
    product_name = models.CharField(max_length=100)  # 产品名称
    product_long_name = models.CharField(max_length=200)  # 产品完整名称

    prefer_price = models.FloatField(default=0)  # 优惠价格
    market_price = models.FloatField(default=1)  # 市场价格(原始价格)

    class Meta:
        db_table = 'tb_main_goods'


class OrderGoodsModel(models.Model):
    # 订单商品
    goods = models.ForeignKey(GoodModel)  # 商品
    order = models.ForeignKey(OrderModel)  # 订单
    good_num= models.IntegerField(default=1)  # 商品个数

    class Meta:
        db_table = 'tb_order_goods'
