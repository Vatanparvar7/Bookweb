from django.urls import path
from .views import  (   
                        FeedBookView,
                        DetailView,
                        LikeView,
                        BookCreateView,
                        BookEditView,
                        BookDeleteView,
                        BookSearch,
                        UserSearch,
                        BookReviewEdit,
                        CommentDelete,
                        CommentDeletes,
                        BookDeleteMessage,
                        FriendReview,
                        BookTop,
                        favouritebook,
                        deletefavouritebook,
                        FavouriteBook
        
)


app_name='books'
urlpatterns=[
    path('',FeedBookView.as_view(),name='feed'),# wrote test
    path('bookserach/',BookSearch.as_view(),name='booksearch'),# wrote test
    path('usersearch/',UserSearch.as_view(),name="usersearch"),# wrote test
    path('bookTop/',BookTop.as_view(),name="Booktop"),
    path('mybookfavourite/',FavouriteBook.as_view(),name="bookfavourite"),
    path('friendreviw/',FriendReview.as_view(),name="friendreview"),
    path('<int:id>/',DetailView.as_view(),name='detail'),# wrote test
    path('like/<int:id>/',LikeView.as_view(),name="like"),# wrote test
    path('bookcreate/',BookCreateView.as_view(),name="bookcreate"),
    path('bookcreate/<int:id>/edit/',BookEditView.as_view(),name="bookedit"),
    path('bookdelete/<int:id>/messge/',BookDeleteMessage.as_view(),name="deletemessage"),# wrote test
    path('bookcreate/<int:id>/delete/',BookDeleteView.as_view(),name="bookdelete"),# wrote test
    path('<int:book_id>/comments/<int:comment_id>/edit/',BookReviewEdit.as_view(),name='commentedit'), # wrote test
    path('<int:book_id>/view/<int:comment_id>',CommentDelete.as_view(),name='commentdelete'),# wrote test
    path('<int:book_id>/delete/<int:comment_id>deletes/',CommentDeletes.as_view(),name='commentdeletes'),# wrote test
    path('favouritebook/<int:id>/',favouritebook.as_view(),name='favourite'),
    path('favouritebook/<int:id>/delete',deletefavouritebook.as_view(),name='deletelikebook'),

]