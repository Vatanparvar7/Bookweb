
from django.test import TestCase
from .models import CustomUser,FriendModel,ChatModel
from django.urls import reverse
from django.contrib.auth import get_user

class RegistrationTestcase(TestCase):
    def test_register_account(self):
        self.client.post(
            reverse('users:register'),
            data={
            "username":"Shexroz12",
            "first_name":"Shexroz",
            "last_name":"Toshpolatov",
            "email":"sheed20x@gmail.com",
            "password":"123",
        })

        user=CustomUser.objects.get(first_name="Shexroz")
        

        self.assertEqual(user.first_name,"Shexroz")
        self.assertEqual(user.last_name,"Toshpolatov")
        self.assertEqual(user.email,"sheed20x@gmail.com")
        self.assertTrue(user.check_password,"123")
    def test_required_user(self):
        self.client.post(
            reverse('users:register'),
            data={
            "first_name":"Shexroz",
            "last_name":"Toshpolatov",
            "email":"sheed20x@gmail.com",
           
        })

        user=CustomUser.objects.all()

        self.assertEqual(user.count(),0)
    def test_required_form(self):
        response=self.client.post(
            reverse('users:register'),
            data={
            
            "first_name":"Shexroz",
            "last_name":"Toshpolatov",
            "email":"sheed20x@gmail.com",
            
        })
        user=CustomUser.objects.all()
        self.assertEqual(user.count(),0)
        self.assertFormError(response,"form",'password','This field is required.')
        self.assertFormError(response,"form",'username','This field is required.')


    def test_gmail_check(self):
        
        response=self.client.post(
            reverse('users:register'),
            data={
            "username":"Shexroz12",
            "first_name":"Shexroz",
            "last_name":"Toshpolatov",
            "email":"sheed20x",
            "password":"123",
        })
        user=CustomUser.objects.all()
        self.assertEqual(user.count(),0)

        self.assertFormError(response,"form","email",'Enter a valid email address.')
    def test_user_unique(self):
        respone=self.client.post(
            reverse('users:register'),
            data={
            "username":"Shexroz12",
            "first_name":"Shexroz",
            "last_name":"Toshpolatov",
            "email":"sheed20x@gmail.com",
            "password":"123",
        })

        respone2=self.client.post(
            reverse('users:register'),
            data={
            "username":"Shexroz12",
            "first_name":"Shexroz",
            "last_name":"Toshpolatov",
            "email":"sheed20x@gmail.com",
            "password":"123",
        })
        user=CustomUser.objects.count()
        self.assertEqual(user,1)
        self.assertFormError(respone2,"form",'username','A user with that username already exists.')


class LoginRequiredForm(TestCase):

    def test_user_successful(self):

        user = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user.set_password('123')
        user.save()
        self.client.post(
            reverse('users:login'),
            data={
                "username":"Shexrozbek",
                "password":'123',
            }
        )
        user=get_user(self.client)

        self.assertTrue(user.is_authenticated)
    def test_login_error(self):
        user = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user.set_password('123')
        user.save()
        self.client.post(
            reverse('users:login'),
            data={
                "username":"Shexrozbekk",
                "password":'123',
            }
        )

        user=get_user(self.client)
        self.assertFalse(user.is_authenticated)
        
class UserProfileTest(TestCase):
    def test_users_profile(self):
        response=self.client.get(
            reverse('users:userprofile'),
        )
        
        self.assertNotEqual(response.url,'?next=/profile/updateuserprofile/')

    def test_user_detail(self):
        user = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user.set_password('123')
        user.save()
        self.client.login(username="Shexrozbek",password='123')

        response=self.client.get(reverse('users:userprofile'))

        self.assertContains(response,user.username)
        self.assertContains(response,user.first_name)
        self.assertContains(response,user.last_name)
    def test_profile_update(self):
        db_user = CustomUser.objects.create(
            username="Shexrozbek",
            first_name="Shexroz",
            last_name="Toshev",
            email="shecx3@gmail.com"

        )
        db_user.set_password("123")
        db_user.save()
        self.client.login(username="Shexrozbek",password="123")
        responses=self.client.post(
            reverse("users:updateuser"),
            data={
                "username" : "Shexrozbeks",
                "first_name" : "Jasur",
                "email" : "shecd3x@gmail.com",
                "last_name" : "Ernazarov",
            }
        )
        db_user.refresh_from_db()
        self.assertEqual(responses.url,reverse("users:userprofile"))
        self.assertEqual(db_user.username,"Shexrozbeks")
        self.assertEqual(db_user.first_name, "Jasur")
        self.assertEqual(db_user.last_name, "Ernazarov")
        self.assertEqual(db_user.email, "shecd3x@gmail.com")
       
        


class LogoutTest(TestCase):
    def test_user_logout(self):
        user = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user.set_password('123')
        user.save()
        self.client.login(username="Shexrozbek",password='123')
        self.client.get(reverse('users:logout'))
        user=get_user(self.client)
        self.assertFalse(user.is_authenticated)


class FollowTest(TestCase):

    def test_following(self):
        user1 = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user1.set_password('123')
        user1.save()

        user2 = CustomUser.objects.create(username="Shexroz",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user2.set_password('1234')
        user2.save()
        self.client.login(username="Shexrozbek",password='123')
        self.client.get(reverse('users:follow',kwargs={"id":user2.id}))
        
        follow_count=FriendModel.objects.count()
        follow_user=FriendModel.objects.get(my_account=user1)
        self.assertEqual(follow_count,1)
        self.assertEqual(follow_user.friend_account,user2)
    

    def test_unfollow(self):
        user1 = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user1.set_password('123')
        user1.save()

        user2 = CustomUser.objects.create(username="Shexroz",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user2.set_password('1234')
        user2.save()
        self.client.login(username="Shexrozbek",password='123')
        self.client.get(reverse('users:follow',kwargs={"id":user2.id}))
        follow_count=FriendModel.objects.count()
        follow_user=FriendModel.objects.get(my_account=user1)
        self.assertEqual(follow_count,1)
        self.assertEqual(follow_user.friend_account,user2)

        self.client.get(reverse('users:follow',kwargs={"id":user2.id}))
        follow_count=FriendModel.objects.count()
        self.assertEqual(follow_count,0)
    
    def test_user_following(self):
        user1 = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user1.set_password('123')
        user1.save()

        user2 = CustomUser.objects.create(username="Shexroz",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user2.set_password('1234')
        user2.save()
        self.client.login(username="Shexrozbek",password='123')
        self.client.get(reverse('users:follow',kwargs={"id":user2.id}))#followers
        response1=self.client.get(reverse('users:followers',kwargs={"id":user2.id}))

        self.assertContains(response1,user1.username)
        response2=self.client.get(reverse('users:following',kwargs={"id":user1.id}))

        self.assertContains(response2,user2.username)

class Chatmessagetest(TestCase):
    
    def test_message_write(self):
        user1 = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user1.set_password('123')
        user1.save()

        user2 = CustomUser.objects.create(username="Shexroz",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user2.set_password('1234')
        user2.save()
        self.client.login(username="Shexrozbek",password='123')

        self.client.post(
            reverse("users:chat",kwargs={"id":user2.id}),
            data={
                "chat":"Hello.I am Shexroz",
            }
        )
        chat_count=ChatModel.objects.count()
        chatt=ChatModel.objects.get(my_chat=user1)

        self.assertEqual(chat_count,1)
        self.assertEqual(chatt.chat,"Hello.I am Shexroz")
        self.assertEqual(chatt.friend_chat,user2)
    
    def test_FriendChat(self):
        user1 = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user1.set_password('123')
        user1.save()

        user2 = CustomUser.objects.create(username="Shexroz",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user2.set_password('1234')
        user2.save()
        self.client.login(username="Shexrozbek",password='123')

        self.client.post(
            reverse("users:chat",kwargs={"id":user2.id}),
            data={
                "chat":"Hello.I am Shexroz",
            }
        )
        
        response1=self.client.get(
            reverse("users:friendchat"),
        )

        self.assertContains(response1,user2.username)

    def test_friend_profile(self):
        user1 = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user1.set_password('123')
        user1.save()

        user2 = CustomUser.objects.create(username="Shexroz",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user2.set_password('1234')
        user2.save()
        self.client.login(username="Shexrozbek",password='123')

        response=self.client.get(
            reverse("users:user_follow",kwargs={"id":user2.id})
        )

        self.assertContains(response,user2.username)
        self.assertContains(response,user2.first_name)
        self.assertContains(response,user2.last_name)














        



    