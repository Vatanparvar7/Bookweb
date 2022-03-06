from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from users.models import CustomUser
# Create your models here.

class FeedModel(models.Model):
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=False,blank=False)
    title=models.CharField(max_length=200,default="......")
    image=models.ImageField(upload_to='bookimage/',default="bookimage/bookimage.jpg")
    date=models.DateTimeField(auto_now_add=True)
    like=models.ManyToManyField(CustomUser,related_name="like",blank=True,)
    file=models.FileField(upload_to='bookfile/',null=False,blank=False,default='bookfile/sh.pdf')
    sight=models.ManyToManyField(CustomUser,related_name="sight",blank=True,)

    def __str__(self):
        return self.name
class Comments(models.Model):
    book=models.ForeignKey(FeedModel,on_delete=models.CASCADE,related_name='book')
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    comments=models.CharField(max_length=300)
    time=models.DateTimeField(auto_now_add=True)
    star=models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.book.name


class LikeBook(models.Model):
    booklike=models.ForeignKey(FeedModel,related_name='booklike',on_delete=models.CASCADE)
    userlike=models.ForeignKey(CustomUser,related_name='userlike',on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.book.nmae




