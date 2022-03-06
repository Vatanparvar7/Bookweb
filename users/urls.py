from django.urls import path
from .views import ( RegisterUSer,
                     LoginUser,
                     LogoutView,
                     FriendChat,
                     FriendProfile,
                     Follow,
                     ChatView,
                     MyProfile,
                     Followers,
                     Following,
                     UpdateUser,
                     FeedFollow
                     )



app_name='users'
urlpatterns=[
    path('register/',RegisterUSer.as_view(),name='register'),#The test was written
    path('profile/',MyProfile.as_view(),name='userprofile'),#The test was written
    path('profile/updateuserprofile/',UpdateUser.as_view(),name='updateuser'),#The test was written
    path('',LoginUser.as_view(),name='login'),#The test was written
    path('logout/',LogoutView.as_view(),name='logout'),#The test was written
    path('friendchat/',FriendChat.as_view(),name="friendchat",),#The test was written
    path('users/<int:id>/',FriendProfile.as_view(),name="user_follow",),
    path('users/<int:id>/follow/',Follow.as_view(),name="follow",),#The test was written
    path('friendchat/<int:id>/chat/',ChatView.as_view(),name="chat",),#The test was written
    path('users/<int:id>/followers/',Followers.as_view(),name="followers",),#The test was written
    path('users/<int:id>/following/',Following.as_view(),name="following",),#The test was written
    path('feedfollow/<int:id>/follow/',FeedFollow.as_view(),name="FeedFollow")#The test was written

]