
import pickle
from django.urls import reverse
from django.test import TestCase,Client
from users.models import CustomUser
from .models import FeedModel,Comments

class BookListTestCase(TestCase):
    def test_book_list(self):
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
        response=self.client.get(
            reverse("books:feed")
        )

        self.assertContains(response,"No Book")
    

    def test_book_list_contain(self):
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

        book1=FeedModel.objects.create(author_id=1,title="Fizika",name="Matemtaika")
        book2=FeedModel.objects.create(author_id=1,title="Fizika2",name="Matemtaika2")
        book3=FeedModel.objects.create(author_id=1,title="Fizika3",name="Matemtaika3")
        book4=FeedModel.objects.create(author_id=1,title="Fizika4",name="Matemtaika4")

        books=FeedModel.objects.count()
        self.assertEqual(books,4)
        
        books=FeedModel.objects.all()
        response=self.client.get(
            reverse("books:feed")
        )

        for book in books:
            self.assertContains(response,book.title)
            self.assertContains(response,book.author)
            self.assertContains(response,book.name)


    def test_detail_book(self):
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
        book1=FeedModel.objects.create(author_id=1,title="Fizika",name="Matemtaika")
        
        response=self.client.get(
            reverse('books:detail',kwargs={"id":book1.id})
        )

        self.assertContains(response,book1.title)
        self.assertContains(response,book1.name)
    def test_book_search(self):
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
        book1=FeedModel.objects.create(author_id=1,title="Fizika",name="Matemtaika")
        book2=FeedModel.objects.create(author_id=1,title="Fizika2",name="Matemtaika2")
        book3=FeedModel.objects.create(author_id=1,title="Fizika3",name="Matemtaika3")
        book4=FeedModel.objects.create(author_id=1,title="Fizika4",name="Matemtaika4")

        response=self.client.get(reverse('books:booksearch')+'?q=Matemtaika')
        self.assertContains(response,book1.name)
        response=self.client.get(reverse('books:booksearch')+'?q=Matemtaika2')
        self.assertContains(response,book2.name)
        response=self.client.get(reverse('books:booksearch')+'?q=Matemtaika3')
        self.assertContains(response,book3.name)
        response=self.client.get(reverse('books:booksearch')+'?q=Matemtaika4')
        self.assertContains(response,book4.name)
    def test_user_search(self):
        
        user = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user.set_password('123')
        user.save()
        user1 = CustomUser.objects.create(username="Jasur",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user1.set_password('1234')
        user1.save()
        user3 = CustomUser.objects.create(username="Shaxruz",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user3.set_password('1235')
        user3.save()

        self.client.login(username="Shexrozbek",password='123')
        
        response1=self.client.get(reverse('books:usersearch')+'?q=Jasur')
        self.assertContains(response1,user1.username)
        response2=self.client.get(reverse('books:usersearch')+'?q=Shexrozbek')
        self.assertContains(response2,user.username)
        response3=self.client.get(reverse('books:usersearch')+'?q=Shaxruz')
        self.assertContains(response3,user3.username)

    def test_user_nosearch_urltest(self):
        user = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user.set_password('123')
        user.save()
        user1 = CustomUser.objects.create(username="Jasur",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user1.set_password('1234')
        user1.save()
        book1=FeedModel.objects.create(author_id=2,title="Fizika",name="Matemtaika")
        book2=FeedModel.objects.create(author_id=1,title="Fizika2",name="Matemtaika2")
        book3=FeedModel.objects.create(author_id=2,title="Fizika3",name="Matemtaika3")
        book4=FeedModel.objects.create(author_id=1,title="Fizika4",name="Matemtaika4")
        self.client.login(username="Shexrozbek",password='123')
        response=self.client.get(reverse('books:usersearch'))
        self.assertEqual(response.status_code,200)

class BookCreateDelteTest(TestCase):
    def test_book_delete(self):
        user = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user.set_password('123')
        user.save()
        book1=FeedModel.objects.create(author_id=2,title="Fizika",name="Matemtaika")
        book_count=FeedModel.objects.count()
        self.assertEqual(book_count,1)
        self.client.login(username="Shexrozbek",password='123')
        response=self.client.get(reverse('books:bookdelete',kwargs={"id":book1.id}))
        book_count=FeedModel.objects.count()
        self.assertEqual(book_count,0)
    

    def test_book_delete_message(self):
        user = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user.set_password('123')
        user.save()
        book1=FeedModel.objects.create(author_id=1,title="Fizika",name="Matemtaika")
        self.client.login(username="Shexrozbek",password='123')
        response=self.client.get(reverse('books:deletemessage',kwargs={"id":book1.id}))
        self.assertContains(response,"Are you going to delete this book?")
        self.assertContains(response,book1.name)
    

      

class CommentTestCase(TestCase):
    def test_comment_create(self):
        user = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user.set_password('123')
        user.save()
        
        book1=FeedModel.objects.create(author_id=1,title="Fizika",name="Matemtaika")
        self.client.login(username="Shexrozbek",password='123')
        response=self.client.post(
            reverse('books:detail',kwargs={"id":book1.id}),
            data={
                
                "num1":'',
                "num2":1,
                "num3":1,
                "num4":'',
                "num5":'',
                "comments":"Bu kitob juda zor ekan",
            }

            )
        count=Comments.objects.count()
        self.assertEqual(count,1)
        comment=Comments.objects.get(book=book1)
        self.assertEqual(comment.comments,"Bu kitob juda zor ekan")
        self.assertEqual(comment.user,user)
        self.assertEqual(comment.book,book1)
        self.assertEqual(comment.star,4)
    

    def test_book_comment_update(self):
        user = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user.set_password('123')
        user.save()
        
        book1=FeedModel.objects.create(author_id=1,title="Fizika",name="Matemtaika")
        self.client.login(username="Shexrozbek",password='123')
        
        comment=Comments.objects.create(
            user=user,
            book=book1,
            comments="Bu kitob zor ekan",
            star=3, 
        )
        
        comment=Comments.objects.get(user=user)
        self.assertEqual(comment.user,user)
        self.assertEqual(comment.comments,"Bu kitob zor ekan")
        self.assertEqual(comment.book,book1)
        self.assertEqual(comment.star,3)
        

        response=self.client.post(
            reverse('books:commentedit',kwargs={"book_id":book1.id,"comment_id":comment.id}),
            data={
                "comments":"Bu kitob juda zor ekan45s",
                "num1":1,
                "num2":'',
                "num3":1,
                "num4":1,
                "num5":'',
            }

        )
        comment.refresh_from_db()
        commenta=Comments.objects.get(user=user)
        self.assertEqual(commenta.comments,"Bu kitob juda zor ekan45s")
        self.assertEqual(commenta.star,5)
    

    def test_comment_delete(self):
        user = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user.set_password('123')
        user.save()
        
        book1=FeedModel.objects.create(author_id=1,title="Fizika",name="Matemtaika")
        self.client.login(username="Shexrozbek",password='123')
        
        comment=Comments.objects.create(
            user=user,
            book=book1,
            comments="Bu kitob zor ekan",
            star=3, 
        )
        comment2=Comments.objects.create(
            user=user,
            book=book1,
            comments="Bu kitob zor ekanssad",
            star=3, 
        )
        
        response=self.client.get(reverse('books:commentdeletes',kwargs={"book_id":book1.id,"comment_id":comment.id})),
       
        comments_count=Comments.objects.count()
        self.assertEqual(comments_count,1)
    

    def test_viewcomment(self):
        user = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user.set_password('123')
        user.save()
        
        book1=FeedModel.objects.create(author_id=1,title="Fizika",name="Matemtaika")
        self.client.login(username="Shexrozbek",password='123')
        comment=Comments.objects.create(
            user=user,
            book=book1,
            comments="Bu kitob zor ekan",
            star=3, 
        )
        respone=self.client.get(
            reverse('books:commentdelete',kwargs={"book_id":book1.id,"comment_id":comment.id}),
        )

        self.assertContains(respone,"Are you going to delete this review?")
        self.assertContains(respone,comment.comments)
        
class Bookliektest(TestCase):
    
    def test_book_like(self):
        user = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user.set_password('123')
        user.save()
        
        book1=FeedModel.objects.create(author=user,title="Fizika",name="Matemtaika")
        self.client.login(username="Shexrozbek",password='123')
        respone=self.client.get(
            reverse('books:like',kwargs={"id":book1.id}),
        )
        
        book=FeedModel.objects.get(id=book1.id)

        like_count=book.like.count()

        self.assertEqual(like_count,1)

    
    def test_book_dislike(self):
        user = CustomUser.objects.create(username="Shexrozbek",first_name="Shexroz",last_name="Toshpolatov",email="shexroz@gmail.com")
        user.set_password('123')
        user.save()
        
        book1=FeedModel.objects.create(author=user,title="Fizika",name="Matemtaika")
        self.client.login(username="Shexrozbek",password='123')
        respone=self.client.get(
            reverse('books:like',kwargs={"id":book1.id}),
        )
        
       
        self.client.login(username="Shexrozbek",password='123')
        respone=self.client.get(
            reverse('books:like',kwargs={"id":book1.id}),
        )
        book=FeedModel.objects.get(id=book1.id)

        like_count=book.like.count()

        self.assertEqual(like_count,0)
    






