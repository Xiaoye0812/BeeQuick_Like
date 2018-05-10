from django.db import models


class UserModel(models.Model):

    user_name = models.CharField(max_length=32, unique=True)  # 用户名
    password = models.CharField(max_length=255)  # 密码
    email = models.CharField(max_length=64, unique=True)  # 邮箱
    sex = models.BooleanField(default=False)  # 性别 False代表女
    icon = models.ImageField(upload_to='icons')  # 头像
    is_delete = models.BooleanField(default=False)  # 是否删除

    class Meta:
        db_table = 'tb_users'


class TicketModel(models.Model):

    user = models.ForeignKey(UserModel)
    ticket = models.CharField(max_length=32)
    create_time = models.IntegerField()

    class Meta:
        db_table = 'tb_user_ticket'
