
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    image = models.ImageField(blank=True,null=True,upload_to='userimage/',default='userimage/userimage.jpg',)
    


class MessageFriendModel(models.Model):
    my_user=models.ForeignKey(CustomUser,related_name='my_user',on_delete=models.CASCADE)
    friend_user=models.ForeignKey(CustomUser,related_name='friend_user',on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.my_user.username


class FriendModel(models.Model):
    my_account=models.ForeignKey(CustomUser,related_name='Shexroz',on_delete=models.CASCADE)
    friend_account=models.ForeignKey(CustomUser,related_name='Jasur',on_delete=models.CASCADE)
    vaqt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.my_account.username

class ChatModel(models.Model):
    my_chat=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='my_chat')
    friend_chat = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friend_chat')
    chat=models.CharField(max_length=350)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.my_chat.username