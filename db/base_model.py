from django.db import models

class BaseModel(models.Model):
    """
    自定义模型类的抽象类
    """
    craete_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now_add=True,verbose_name="更新时间")
    is_delete = models.BooleanField(default=False,verbose_name="删除标记")

    class Meta:
        # 说明当前模型是一个抽象模型类，
        # 抽象模型类在生成迁移文件并执行迁移文件后不会在数据库中生成对应的表
        abstract = True
