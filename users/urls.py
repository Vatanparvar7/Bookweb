from django.urls import path
from .views import ( RegisterUSer,
                     LoginUser,
                     LogoutView,
                     FriendChat,
                     FriendProfile,
                     Follow,
                     Account,
                     ChatView,
                     MyProfile,
                     Followers,
                     Following,
                     UpdateUser
                     )



app_name='users'
urlpatterns=[
    path('register/',RegisterUSer.as_view(),name='register'),
    path('profile/',MyProfile.as_view(),name='userprofile'),
    path('profile/<int:id>/updateuserprofile/',UpdateUser.as_view(),name='updateuser'),
    path('',LoginUser.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('friendchat/',FriendChat.as_view(),name="friendchat",),
    path('users/<int:id>/',FriendProfile.as_view(),name="user_follow",),
    path('users/<int:id>/follow/',Follow.as_view(),name="follow",),
    path('accounts/',Account.as_view(),name='account'),
    path('friendchat/<int:id>/chat/',ChatView.as_view(),name="chat",),
    path('users/<int:id>/followers/',Followers.as_view(),name="followers",),
    path('users/<int:id>/following/',Following.as_view(),name="following",),

]