
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import CustomUser,FriendModel,MessageFriendModel,ChatModel
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterFrom,ChatFormm,UserUpdateFrom
from books.models import FeedModel



# Create your views here.



class RegisterUSer(View):
    def get(self,request):
        form = UserRegisterFrom()
        return render(request,'registers.html',{"form":form,})
    def post(self,request):
        form = UserRegisterFrom(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        else:
            return render(request, 'registers.html', {"form": form,})

class LogoutView(LoginRequiredMixin,View):
    def get(self,request):
        print('foydalanuvchi saytdan chiqdi')
        logout(request)

        return  redirect('users:login')




class LoginUser(View):
    def get(self,request):
        form=AuthenticationForm()

        return render(request,'index.html',{"form":form,})
    def post(self,request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('books:feed')
        else:
            return render(request, 'index.html', {"form": form})


class UpdateUser(LoginRequiredMixin,View):
    def get(self,request):
        
        form=UserUpdateFrom(instance=request.user)
        return render(request,'updateuser.html',{"form":form})
    def post(self,request):
        form=UserUpdateFrom(instance=request.user,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:userprofile')
        else:
            return render(request,'updateuser.html',{"form":form})
















class FriendChat(LoginRequiredMixin,View):
    def get(self,request):
        sh=request.user
        new1 = ChatModel.objects.filter(my_chat=sh).all()
        new2 = ChatModel.objects.filter(friend_chat=sh).all()
        cos = list(new1) + list(new2)
        for i in range(0,len(cos)):
            s = 0
            for j in range(i+1,len(cos)):
                if cos[i].friend_chat == cos[j-s].friend_chat and  cos[i].my_chat ==cos[j-s].my_chat:
                    cos.pop(j-s)
                    s+=1

        for i in range(0,len(cos)):
            s=0
            for j in range(i+1,len(cos)):
                if cos[i].my_chat == cos[j-s].friend_chat and  cos[i].friend_chat ==cos[j-s].my_chat :
                    cos.pop(j-s)
                    s+=1
        for i in cos:
            for j in cos:
                if i.date > j.date:
                    i.my_chat, j.my_chat = j.my_chat, i.my_chat
                    i.friend_chat, j.friend_chat = j.friend_chat, i.friend_chat
                    i.date, j.date = j.date, i.date
                    i.chat, j.chat = j.chat, i.chat

        return  render(request,'friendchat.html',{"users":cos})


class FriendProfile(LoginRequiredMixin,View):
    def get(self,request,id):
        user = CustomUser.objects.get(id=id)
        friend=FriendModel.objects.filter(my_account=request.user, friend_account=user).exists()
        books=FeedModel.objects.filter(author=user).all()
        sa=books.count()
        follow=FriendModel.objects.filter(my_account=user).count()
        followers=FriendModel.objects.filter(friend_account=user).count()
        return render(request,'friendprofile.html',{"userr":user,"friend":friend,"books":books,"follow":follow,"followers":followers,"sum":sa})

class MyProfile(LoginRequiredMixin,View):
    def get(self,request):

        sh=request.user
        follow = FriendModel.objects.filter(my_account=sh).count()
        folloing = FriendModel.objects.filter(friend_account=sh).count()
        book=FeedModel.objects.filter(author=sh).all()
        sa=book.count()
        return render(request,'userprofile.html',{'userr':sh,"books":book,'sum':sa,"following":folloing,"follow":follow})


class Followers(LoginRequiredMixin,View):
    def get(self,request,id):
        user = CustomUser.objects.get(id=id)
        follow = FriendModel.objects.filter(friend_account=user).all()
        sh = FriendModel.objects.filter(my_account=request.user).values('friend_account').all()
        s=[0]
        for i in sh:
            s.append(i['friend_account'])
        return render(request,'followers.html.',{"follows":follow,'item':s})


class Following(LoginRequiredMixin,View):
    def get(self,request,id):
        user = CustomUser.objects.get(id=id)
        follow = FriendModel.objects.filter(my_account=user).all()
        sh = FriendModel.objects.filter(my_account=request.user).values('friend_account').all()
        s = []
        for i in sh:
            s.append(i['friend_account'])
        return render(request,'following.html',{"follows":follow,'item':s})


class Follow(LoginRequiredMixin,View):
    def get(self,request,id):
        user=CustomUser.objects.get(id=id)
        friend=FriendModel.objects.filter(my_account=request.user, friend_account=user).exists()
        if friend:
            chat=FriendModel.objects.get(my_account=request.user,friend_account=user)
            chat.delete()
            return redirect(reverse("users:user_follow",kwargs={"id": id}))
        else:

            soz = FriendModel.objects.create(my_account=request.user, friend_account=user)
            soz.save()
            got=MessageFriendModel.objects.filter(my_user=request.user, friend_user=user).exists()
            sad = FriendModel.objects.filter(my_account=request.user, friend_account=user).exists()
            if not got and sad:
                chat = MessageFriendModel.objects.create(my_user=request.user, friend_user=user)
                chat.save()
            return redirect(reverse("users:user_follow",kwargs={"id": id}))

class ChatView(LoginRequiredMixin,View):
    def get(self,request,id):
        friend=CustomUser.objects.get(id=id)
        new1=ChatModel.objects.filter(my_chat=request.user,friend_chat=friend).all()
        new2=ChatModel.objects.filter(my_chat=friend,friend_chat=request.user)
        cos=list(new1)+list(new2)
        for i in cos:
            for j in cos:
                if i.date < j.date:
                    i.my_chat, j.my_chat = j.my_chat, i.my_chat
                    i.friend_chat, j.friend_chat = j.friend_chat, i.friend_chat
                    i.date, j.date = j.date, i.date
                    i.chat, j.chat = j.chat, i.chat

        form=ChatFormm()
        return render(request,'mychat.html',{"form":form,'cos':cos,"friend":friend})
    def post(self,request,id):
        form = ChatFormm(data=request.POST)
        frined=CustomUser.objects.get(id=id)
        if form.is_valid():
            chat=request.POST.get('chat')
            sh=ChatModel(my_chat=request.user,friend_chat=frined,chat=chat)
            sh.save()
            return redirect(reverse('users:chat',kwargs={"id":id}))

class FeedFollow(LoginRequiredMixin,View):
    def get(self,request,id):
        user=CustomUser.objects.get(id=id)
        friend=FriendModel.objects.filter(my_account=request.user, friend_account=user).exists()
        if friend:
            chat=FriendModel.objects.get(my_account=request.user,friend_account=user)
            chat.delete()
            return redirect(reverse("books:feed"))
        else:

            soz = FriendModel.objects.create(my_account=request.user, friend_account=user)
            soz.save()
            got=MessageFriendModel.objects.filter(my_user=request.user, friend_user=user).exists()
            sad = FriendModel.objects.filter(my_account=request.user, friend_account=user).exists()
            if not got and sad:
                chat = MessageFriendModel.objects.create(my_user=request.user, friend_user=user)
                chat.save()
            return redirect(reverse("books:feed"))