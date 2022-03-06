
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import CommentForm,BookCreateForm,ExampleForm
from .models import FeedModel,Comments,LikeBook
from users.models import CustomUser,FriendModel
from django.core.paginator import Paginator
from users.models import MessageFriendModel


# Create your views here.


class FeedBookView(LoginRequiredMixin,View):
    def get(self,request):
        #user follow message
        new=MessageFriendModel.objects.filter(friend_user=request.user).all().order_by("-id")
        suma=new.count()
        
        for i in new:
            print(i.my_user)
        #Book get
        friend=FriendModel.objects.filter(my_account=request.user).all()
        if friend:
            book=list()
            for i in friend:
                book+=list(FeedModel.objects.filter(author=i.friend_account).all())
            for i in range(0,len(book)):
                for j in range(i+1,len(book)):
                    if book[i].date <= book[j].date:
                        book[i],book[j]=book[j],book[i]

                    elif book[i].date == book[j].date:
                        if book[i].like.count() <= book[j].like.count():
                            book[i], book[j] = book[j], book[i]
                        else:
                            book[i]=book[i]
                            book[j]=book[j]
                    else:
                        book[i] = book[i]
                        book[j] = book[j]
        
        else:
            book=list(FeedModel.objects.all())
            for i in range(0,len(book)):
                for j in range(i+1,len(book)):
                    if book[i].like.count() <= book[j].like.count():
                        book[i],book[j]=book[j],book[i]
                    elif book[i].like.count() == book[j].like.count():
                        if book[i].date <= book[j].date:
                            book[i],book[j]=book[j],book[i]


                        else:
                            book[i]=book[i]
                            book[j]=book[j]
                    else:
                        book[i] = book[i]
                        book[j] = book[j]
        page=request.GET.get('page',1)
        pagination=Paginator(book,6)
        page_obg=pagination.get_page(page)

        #user top
        user=list(CustomUser.objects.all())
        n=0
        for i in range(len(user)):
            if  FriendModel.objects.filter(my_account=request.user,friend_account=user[i-n]).exists() or request.user==user[i-n]:
                user.pop(i-n)
                
                n+=1
     
        
       
        return render(request,'feed.html',{"page_obg":page_obg,"new":new,"n":suma,"userfollow":user})
class BookTop(LoginRequiredMixin,View):
    def get(self,request):
        book=list(FeedModel.objects.all())
        for i in range(0,len(book)):
            for j in range(i+1,len(book)):
                if book[i].like.count() <= book[j].like.count():
                    book[i],book[j]=book[j],book[i]
                elif book[i].like.count() == book[j].like.count():
                    if book[i].date <= book[j].date:
                        book[i],book[j]=book[j],book[i]


                    else:
                        book[i]=book[i]
                        book[j]=book[j]
                else:
                    book[i] = book[i]
                    book[j] = book[j]
        page=request.GET.get('page',1)
        pagination=Paginator(book,6)
        page_obg=pagination.get_page(page)
        return render(request,'best_Book.html',{"page_obg":page_obg,})
class DetailView(LoginRequiredMixin,View):
    def get(self,request,id):
        book=FeedModel.objects.get(id=id)
        sights=book.sight.all()
        user=request.user
        if user in sights:
            print(user.username)
        else:
            book.sight.add(user)
        forms=ExampleForm(request.POST or None)
        comments = Comments.objects.filter(book=book).order_by("-id")
        return render(request,'book_detile.html',{"book":book,"forms":forms,"commentss":comments})
    def post(self,request,id):
        forms=ExampleForm(request.POST or None)
        book=FeedModel.objects.get(id=id)
        if forms.is_valid():
            num1=request.POST.get('num1' or '')
            num2=request.POST.get('num2' or '')
            num3=request.POST.get('num3' or '')
            num4=request.POST.get('num4' or '')
            num5=request.POST.get('num5' or '')
            comments=request.POST.get('comments')
            num=[num1,num2,num3,num4,num5]
           
            print(num)
            
            
            s=5
            for i in range(0,len(num)):
                if num[i]=='' or num[i]==None :
                    s-=1
                else:
                    
                    break
            
            comment=Comments.objects.create(user=request.user,book=book,comments=comments,star=s)
            comment.save()
            return redirect('/feed/{}'.format(id))
        else:
            comment_from = CommentForm()
            book = FeedModel.objects.get(id=id)
            return render(request, 'detail.html', {"book": book, "form_comment": comment_from})

class LikeView(LoginRequiredMixin,View):
    def get(self,request,id):
        book=FeedModel.objects.get(id=id)
        likes=book.like.all()
        user=request.user
        if user in likes:
            book.like.remove(user)
        else:
            book.like.add(user)
        return redirect('books:feed')

class BookCreateView(LoginRequiredMixin,View):
    def get(self,request):
        form=BookCreateForm()
        return render(request,'bookcreates.html',{"form":form})
    def post(self,request):
        form = BookCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            user=request.user
            name=request.POST.get('name')
            title=request.POST.get('title')
            image=request.FILES.get('image')
            file=request.FILES.get('file')
            sa=FeedModel.objects.create(author=user,title=title,image=image,file=file,name=name,)
            sa.save()
            return redirect('users:userprofile')
        else:
            return render(request, 'bookcreates.html', {"form": form})

class BookEditView(LoginRequiredMixin,View):
    def get(self,request,id):
        book=FeedModel.objects.get(id=id)
        form=BookCreateForm(instance=book)
        return render(request,'bookedits.html',{"form":form})
    def post(self,request,id):
        book = FeedModel.objects.get(id=id)
        form=BookCreateForm(instance=book,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:userprofile')
        else:
            return render(request,'bookedits.html',{"form":form})

class BookDeleteMessage(View):
    def get(self,request,id):
        sh=request.user
        book=FeedModel.objects.get(id=id)
        return render(request,'bookdelete.html',{"book":book,'user':sh})
class BookDeleteView(LoginRequiredMixin,View):
    def get(self,request,id):
        book=FeedModel.objects.get(id=id)
        book.delete()
        return redirect('users:userprofile')

class BookSearch(View):
    def get(self,request):
        name=request.GET.get('q','')
        if name!= '':
            # Foydalanuvchiga izlatgan kitobi boyicha eng like kop va vaqtliroq chiqqan kitoblar ko'rastiladi.
            books=FeedModel.objects.filter(name__icontains=name).all()
            book=list(books)
            for i in range(0,len(book)):
                for j in range(i+1,len(book)):
                    if book[i].date <= book[j].date:
                        book[i],book[j]=book[j],book[i]

                    elif book[i].date == book[j].date:
                        if book[i].like.count() <= book[j].like.count():
                            book[i], book[j] = book[j], book[i]
                        else:
                            book[i]=book[i]
                            book[j]=book[j]
                    else:
                        book[i] = book[i]
                        book[j] = book[j]
        else:
            # Agar foydalanuvchi kitob izlatgan bolsa unga eng kop like bor va vaqtliroq chiqqan kitoblar korsatiladi
            #  kitoblarni korsatiladi.
            books=FeedModel.objects.all()[:5]
            book=list(books)
            for i in range(0,len(book)):
                for j in range(i+1,len(book)):
                    if  book[i].like.count() <= book[j].like.count():
                        book[i],book[j]=book[j],book[i]

                    elif book[i].like.count() == book[j].like.count():
                        if book[i].date <= book[j].date:
                            book[i], book[j] = book[j], book[i]
                        else:
                            book[i]=book[i]
                            book[j]=book[j]
                    else:
                        book[i] = book[i]
                        book[j] = book[j]
        return render(request,'booksearch.html',{'books':book})


class UserSearch(LoginRequiredMixin,View):
    def get(self,request):
        uss=request.GET.get('q' or None)
        print(uss)
        if uss !='' and uss != None:
            users=CustomUser.objects.filter(username__icontains=uss).all()
        else:
            books=FeedModel.objects.all()
            book=list(books)
            for i in range(0,len(book)):
                for j in range(i+1,len(book)):
                    if  book[i].like.count() <= book[j].like.count():
                        book[i],book[j]=book[j],book[i]

                    elif book[i].like.count() == book[j].like.count():
                        if book[i].date <= book[j].date:
                            book[i], book[j] = book[j], book[i]
                        else:
                            book[i]=book[i]
                            book[j]=book[j]
                    else:
                        book[i] = book[i]
                        book[j] = book[j]
            for i in range(0,len(book)):
                s=0
                for j in range(i+1,len(book)):
                    if book[i].author == book[j-s].author:
                        book.pop(j-s)
                        s+=1
            users=book[:10]
        return render(request,'usersearch.html',{'users':users,'q':uss})


class BookReviewEdit(LoginRequiredMixin,View):
    def get(self,request,book_id,comment_id):
        book=FeedModel.objects.get(id=book_id)
        review=Comments.objects.get(id=comment_id)
        # reviews=review.filter(id=comment_id)
        forms=ExampleForm(request.POST or None)
        return render(request,'commentedit.html',{'forms':forms,'comment':review,'book':book})
    def post(self,request,book_id,comment_id):
        book=FeedModel.objects.get(id=book_id)
        review=Comments.objects.get(id=comment_id)
        forms=ExampleForm(request.POST or None)
        if forms.is_valid():
            num1=request.POST.get('num1')
            num2=request.POST.get('num2')
            num3=request.POST.get('num3')
            num4=request.POST.get('num4')
            num5=request.POST.get('num5')
            comments=request.POST.get('comments')
            num=[num1,num2,num3,num4,num5]
           
            print(num)
            
            
            s=5
            for i in range(0,len(num)):
                if num[i]=='' or num[i]==None :
                    s-=1
                else:
                    
                    break
            
            # comment=Comments.objects.create(user=request.user,book=book,comments=comments,star=s+1)
            # comment.save()
            review.user=request.user
            review.book=book
            review.comments=comments
            review.star=s
            review.save()
            return redirect('/feed/{}'.format(book_id))
        else:
            return render(request,'commentedit.html',{'forms':forms})
class CommentDelete(LoginRequiredMixin,View):
    def get(self,request,book_id,comment_id):
        comment=Comments.objects.get(id=comment_id)
        book=FeedModel.objects.get(id=book_id)
        return render(request,'commentdelete.html',{'book':book,'comment':comment})
class CommentDeletes(LoginRequiredMixin,View):
    def get(self,request,book_id,comment_id):
        review=Comments.objects.get(id=comment_id)
        review.delete()
        return redirect('/feed/{}'.format(book_id))
class FriendReview(View):
    def get(self,request):
        friend=FriendModel.objects.filter(my_account=request.user).all()
        if friend:
            book=list()
            for i in friend:
                book+=list(Comments.objects.filter(user=i.friend_account).all())
            for i in range(0,len(book)):
                for j in range(i+1,len(book)):
                    if book[i].time <= book[j].time:
                        book[i],book[j]=book[j],book[i]
                    else:
                        book[i] = book[i]
                        book[j] = book[j]
            

        else:
            book=list(Comments.objects.all().order_by('id'))
            for i in range(0,len(book)):
                for j in range(i+1,len(book)):
                    if book[i].time <= book[j].time:
                        book[i],book[j]=book[j],book[i]
                    else:
                        book[i] = book[i]
                        book[j] = book[j]
        page=request.GET.get('page',1)
        pagination=Paginator(book,6)
        page_obg=pagination.get_page(page)
        return render(request,'friendcommentview.html',{"page_obg":page_obg})

class favouritebook(View):
    def get(self,request,id):
        book=FeedModel.objects.get(id=id)
        

        if not LikeBook.objects.filter(userlike=request.user,booklike=book).exists():
            like=LikeBook.objects.create(
                userlike=request.user,
                booklike=book,
            )
            like.save()
        return redirect("books:feed")
class deletefavouritebook(View):
    def get(self,request,id):
        book=FeedModel.objects.get(id=id)
        

        if LikeBook.objects.filter(userlike=request.user,booklike=book).exists():
            like=LikeBook.objects.get(userlike=request.user,booklike=book)
            like.delete()
        return redirect("books:bookfavourite")
class FavouriteBook(View):
    def get(self,request):
        favouriteBook=LikeBook.objects.filter(userlike=request.user).all()
        return render(request,'myfavouritebook.html',{"books":favouriteBook})









