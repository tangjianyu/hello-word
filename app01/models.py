from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType

class Policy(models.Model):
    """价格策略"""
    price = models.IntegerField()
    content_type = models.ForeignKey(ContentType,verbose_name='关联的表名称')
    object_id = models.IntegerField(verbose_name='关联的表中的数据行的ID')

    content_object = GenericForeignKey('content_type','object_id')

class Course(models.Model):
    """普通课程"""
    title = models.CharField(max_length=32)
    policy_list = GenericRelation(Policy)
    class Meta:
        verbose_name_plural = '123'

class VIPCourse(models.Model):
    """VIP课程"""
    title = models.CharField(max_length=32)
    policy_list = GenericRelation(Policy)

