from django.db import models
from django.utils.timezone import now
class AbstractUser(models.Model):
    id = models.AutoField('学生ID', primary_key=True)
    username = models.CharField('用户名', max_length=16, unique=True)
    nickname = models.CharField('昵称', max_length=16, default='qwe')
    password = models.CharField('密码', max_length=128)  # 密码字段，应在保存前使用make_password哈希
    gender = models.IntegerField('性别', default=0) # 0 1
    age = models.IntegerField('年龄',null=True)
    email = models.EmailField('邮箱', null=True, unique=False)  # 注意：unique=False，因为blank=True
    phonenumber = models.CharField('手机号码', max_length=15, blank=True, null=True)
    role = models.IntegerField('角色',  default=1)  # 0 1 2
    is_active = models.BooleanField('帐号状态（0正常 1封禁）', default=True)
    create_time = models.DateTimeField('创建时间', default=now)  # Django会期望一个可调用的对象

    def is_authenticated(self):
        return True
    
    class Meta:
        db_table = "abstract_user"