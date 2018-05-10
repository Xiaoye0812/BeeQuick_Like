from django.db import models

from goods.models import GoodModel
from users.models import UserModel


class CartModel(models.Model):
    # 购物车
    user = models.ForeignKey(UserModel)  # 用户
    goods = models.ForeignKey(GoodModel)  # 商品
    c_num = models.IntegerField(default=1)  # 商品个数
    is_select = models.BooleanField(default=True)  # 是否选择商品

    class Meta:
        db_table = 'tb_carts'
