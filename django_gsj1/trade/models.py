from django.db import models

# Create your models here.
class Trade(models.Model):
    id = models.BigIntegerField(primary_key=True,default=0,verbose_name=u"交易流水号")
    name = models.CharField(max_length=20,unique=True,verbose_name=u"用户真实姓名")
    account = models.CharField(max_length=20,verbose_name=u"银行储蓄账号")
    saving = models.DecimalField(max_digits=8,decimal_places=2,verbose_name=u"账户储蓄金额")
    expend = models.DecimalField(max_digits=8,decimal_places=2,verbose_name=u"账户支出金额")
    income = models.DecimalField(max_digits=8,decimal_places=2,verbose_name=u"账户收入总计")
    desc = models.CharField(max_length=20,unique=True,verbose_name=u"账户描述")
    class Meta:
        verbose_name= u"交易信息表"
        db_table = u"trade"