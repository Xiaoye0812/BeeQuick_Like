from django.db import models

from users.models import UserModel


class OrderModel(models.Model):
    # 订单
    user = models.ForeignKey(UserModel)  # 用户
    o_num = models.CharField(max_length=64)  #
    o_status = models.IntegerField(default=0)  # 状态 0-下单未付款 1-已付款未发货 2-已付款已发货...
    o_create = models.DateTimeField(auto_now_add=True)  # 创建时间

    class Meta:
        db_table = 'tb_orders'



