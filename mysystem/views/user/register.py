from rest_framework.views import APIView
from rest_framework.response import Response
from mysystem.models import SysUser,AbstractUser
from django.contrib.auth.hashers import make_password, check_password


class Register(APIView):

    def post(self, request):
        data = request.POST
        username = data.get("username", "").strip()
        password = data.get("password", "").strip()
        password_confirm = data.get("password_confirm", "").strip()
        if not username or not password:
            return Response({
                'result': "用户名和密码不能为空"
            })
        if password != password_confirm:
            return Response({
                'result': "两个密码不一致",
            })
        if AbstractUser.objects.filter(username=username).exists():
            return Response({
                'result': "用户名已存在"
            })
        passwd = make_password(password=password)
        absuser = AbstractUser.objects.create(username=username,password=passwd,role=1)
        SysUser.objects.create(absuser=absuser)
        return Response({
            'result': "success",
        })

