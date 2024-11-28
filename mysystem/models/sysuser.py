from django.db import models

from .absuser import AbstractUser

class SysUser(models.Model):
    id = models.AutoField('学生ID', primary_key=True)
    absuser = models.OneToOneField(AbstractUser, on_delete=models.CASCADE, related_name='sysuser')

    class Meta:
        db_table = 'sysuser'

