from django.db import models

#通过ORM创建数据库
class Product(models.Model):
    productname = models.CharField('产品名称',max_length=64)  # 产品名称
    productdesc = models.CharField('产品描述',max_length=200)    # 产品描述
    producter = models.CharField('产品负责人',max_length=200,null=True)    # 产品负责人
    create_time = models.DateTimeField('创建时间',auto_now=True)  # 创建时间-自动获取当前时间    #当前时间
    #verbose_name指定在admin管理界面中显示中文；verbose_name表示单数形式的显示，verbose_name_plural表示复数形式的显示；中文的单数和复数一般不作区别。
    # 模型的复数形式

    class Meta:
        verbose_name = '产品管理'
        verbose_name_plural = '产品管理'

    def __str__(self):
        '''返回一个对象的描述信息'''
        return self.productname
