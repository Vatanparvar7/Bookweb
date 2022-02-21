# from django.test import TestCase
# a=[[1,6],[5,4],[1,7],[7,9],[7,5],[9,7],[9,8],[2,3],[5,6],[5,8]]
#
# for i in range(0,len(a)):
#     for j in range(0,len(a)):
#         if a[i][0]>a[j][0]:
#             a[i],a[j]=a[j],a[i]
#         elif a[i][0]==a[j][0]:
#             if a[i][1]<a[j][1]:
#                 a[i], a[j] = a[j], a[i]
#             else:
#                 a[i] = a[i]
#                 a[j] = a[j]
#         else:
#             a[i]=a[i]
#             a[j]=a[j]
# print(a)
# if book[i].like.count() <= book[j].like.count():
#     book[i].id, book[j].id = book[j].id, book[i].id
#     book[i].author, book[j].author = book[j].author, book[i].author
#     book[i].name, book[j].name = book[j].name, book[i].name
#     book[i].title, book[j].title = book[j].title, book[i].title
#     book[i].image, book[j].image = book[j].image, book[i].image
#     book[i].date, book[j].date = book[j].date, book[i].date
#     book[i].like, book[j].like = book[j].like, book[i].like
#     book[i].file, book[j].file = book[j].file, book[i].file
# elif book[i].like.count() == book[j].like.count():
#     if book[i].date <= book[j].date:
#         book[i].id, book[j].id = book[j].id, book[i].id
#         book[i].author, book[j].author = book[j].author, book[i].author
#         book[i].name, book[j].name = book[j].name, book[i].name
#         book[i].title, book[j].title = book[j].title, book[i].title
#         book[i].image, book[j].image = book[j].image, book[i].image
#         book[i].date, book[j].date = book[j].date, book[i].date
#         book[i].like, book[j].like = book[j].like, book[i].like
#         book[i].file, book[j].file = book[j].file, book[i].file
#
#
#     else:
#         book[i].author = book[i].author
#         book[i].id = book[i].id
#         book[i].name = book[i].name
#         book[i].title = book[i].title
#         book[i].image = book[i].image
#         book[i].date = book[i].date
#         book[i].like = book[i].like
#         book[i].file = book[i].file
#
#         book[j].author = book[j].author
#         book[j].id = book[j].id
#         book[j].name = book[j].name
#         book[j].title = book[j].title
#         book[j].image = book[j].image
#         book[j].date = book[j].date
#         book[j].like = book[j].like
#         book[j].file = book[j].file
# else:
#     book[i].id = book[i].id
#     book[j].id = book[j].id