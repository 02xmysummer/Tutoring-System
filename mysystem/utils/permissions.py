from rest_framework.permissions import BasePermission, IsAuthenticated
from mysystem.models import AbstractUser
# from teacher.models import Teacher
class IsAdminOrSelf(BasePermission):
    def has_permission(self, request, view):
        return IsAuthenticated().has_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        current_user = request.user
        try:
            # 注意：这里我们假设在 POST 请求中，我们总是通过 user_id 来获取目标用户对象
            # 但在实际情况下，对于更新操作，你可能需要从数据库中获取当前登录的用户对象并检查其权限
            # 而不是从请求数据中获取 user_id（除非这是你的业务逻辑的一部分）。
            # 但由于我们在这里实现的是一个通用的权限检查类，我们将继续从请求数据中获取 user_id。
            user_id = int(request.data.get('user_id'))
            target_user = AbstractUser.objects.get(id=user_id)
        except (ValueError, AbstractUser.DoesNotExist):
            return False

        # 检查当前用户是否是管理员（role == 0）或尝试修改自己的信息（current_user.id == target_user.id）
        return current_user.role == 0 or current_user.id == target_user.id