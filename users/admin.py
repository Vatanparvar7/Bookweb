from django.contrib import admin
from .models import CustomUser,MessageFriendModel,FriendModel,ChatModel
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model=CustomUser
    list_display = ['id','username','last_name','first_name','email','image']
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(FriendModel)
admin.site.register(MessageFriendModel)
admin.site.register(ChatModel)
