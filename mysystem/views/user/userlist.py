from rest_framework.views import APIView
from rest_framework.response import Response
from mysystem.models import AbstractUser,SysUser
from datetime import timezone
import dateutil.parser
GENDERS  = ['男','女']
ROLES = ['管理员','普通用户','老师']

class UserList(APIView):

    def get(self,request):
        index = int(request.GET.get('index', 1))
        sysusers = SysUser.objects.all()[10 * (index-1):10 * index]
        # total = SysUser.objects.count()
        res = []
        for sysuser in sysusers:
            iso_time_str = str(sysuser.absuser.create_time)
            dateObject = dateutil.parser.isoparse(iso_time_str)
            localdt = dateObject.replace(tzinfo = timezone.utc).astimezone(tz=None)

            res.append({
                'id':sysuser.absuser.id,
                'username':sysuser.absuser.username,
                'nickname':sysuser.absuser.nickname,
                'role':ROLES[sysuser.absuser.role],
                'gender':GENDERS[sysuser.absuser.gender],
                'status': '正常' if sysuser.absuser.is_active else '封禁',
                'email':sysuser.absuser.email,
                'phonenumber':sysuser.absuser.phonenumber,
                'create_time':localdt.strftime('%Y-%m-%d %H:%M:%S'),
                # 'count':total
            })
        return Response(res)
    
    # def delete(self, request):
    #     try:
    #         users_id = request.data.getlist('users_id',[])  # 使用getlist来处理列表数据
    #         if(len(users_id) == 0):
    #             return Response({'result': 'users_id不存在'})
            
    #         # 使用QuerySet的filter和delete方法来批量删除用户
    #         SysUser.objects.filter(id__in=users_id).delete()
            
    #         return Response({'result': '用户批量删除成功'})
    #     except SysUser.DoesNotExist:
    #         # 注意：在批量删除时，通常不会抛出DoesNotExist异常，
    #         # 因为filter()方法返回的是一个QuerySet，即使没有找到任何对象，
    #         # 调用其delete()方法也不会引发异常。
    #         # 这里保留异常处理主要是为了捕获其他可能的数据库错误。
    #         return Response({'result': '发生错误: 尝试删除的用户中可能不存在某些用户，但已尝试删除所有提供的ID'})
    #     except Exception as e:
    #         return Response({'result': '发生错误: {}'.format(str(e))})
