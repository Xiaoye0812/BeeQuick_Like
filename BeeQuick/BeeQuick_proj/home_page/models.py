from django.db import models


class HomeGoodModel(models.Model):
    id = models.AutoField(primary_key=True)

    is_xf = models.IntegerField(default=1)
    pm_desc = models.CharField(max_length=100)
    dealer_id = models.CharField(max_length=16)

    specifics = models.CharField(max_length=100)  # 规格

    category_id = models.CharField(max_length=16)  # 类别id
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
        db_table = 'tb_home_goods'


class HomePage(models.Model):

    # 图片
    img = models.CharField(max_length=200)
    # 名称
    name = models.CharField(max_length=200)
    # 通用id
    track_id = models.CharField(max_length=10)

    class Meta:
        # 抽象
        abstract = True


class HomeBanner(HomePage):
    # 轮播

    class Meta:
        db_table = 'tb_home_banner'


class HomeNav(HomePage):
    # 导航

    class Meta:
        db_table = 'tb_home_nav'


class HomeShop(HomePage):
    # 商店

    class Meta:
        db_table = 'tb_home_shop'


class HomeMustBuy(HomePage):
    # 必购

    class Meta:
        db_table = 'tb_home_mustbuy'


class HomeShow(HomePage):

    brand_name = models.CharField(max_length=100)  # 品牌
    category_id = models.CharField(max_length=16)  # 类别id

    good1 = models.ForeignKey(HomeGoodModel, related_name='good1')
    good2 = models.ForeignKey(HomeGoodModel, related_name='good2')
    good3 = models.ForeignKey(HomeGoodModel, related_name='good3')

    class Meta:
        db_table = 'tb_home_show'
