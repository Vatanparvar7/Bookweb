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
                        exrorr
)


app_name='books'
urlpatterns=[
    path('',FeedBookView.as_view(),name='feed'),
    path('bookserach/',BookSearch.as_view(),name='booksearch'),
    path('usersearch/',UserSearch.as_view(),name="usersearch"),
    path('friendreviw/',FriendReview.as_view(),name="friendreview"),
    path('<int:id>/',DetailView.as_view(),name='detail'),
    path('like/<int:id>/',LikeView.as_view(),name="like"),
    path('bookcreate/',BookCreateView.as_view(),name="bookcreate"),
    path('bookcreate/<int:id>/edit/',BookEditView.as_view(),name="bookedit"),
    path('bookdelete/<int:id>/messge/',BookDeleteMessage.as_view(),name="deletemessage"),
    path('bookcreate/<int:id>/delete/',BookDeleteView.as_view(),name="bookdelete"),
    path('<int:book_id>/comments/<int:comment_id>/edit/',BookReviewEdit.as_view(),name='commentedit'),
    path('<int:book_id>/view/<int:comment_id>',CommentDelete.as_view(),name='commentdelete'),
    path('<int:book_id>/delete/<int:comment_id>deletes/',CommentDeletes.as_view(),name='commentdeletes'),
    path('404/',exrorr,)
]