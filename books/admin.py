from django.contrib import admin
from .models import FeedModel,Comments,LikeBook
# Register your models here.

admin.site.register(FeedModel)
admin.site.register(Comments)
admin.site.register(LikeBook)