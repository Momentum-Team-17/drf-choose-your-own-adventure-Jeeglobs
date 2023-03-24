from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('core/books/', views.BookListCreate.as_view()),
    # path('core/<int:pk>', views.BookDetail.as_view()),
    path('core/books/<int:pk>', views.BookEditDelete.as_view()),
    path('core/trackers/', views.TrackerListCreate.as_view()),
    path('core/trackers/<int:pk>',
         views.TrackerEditDelete.as_view()),
    path('core/users', views.UserListCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
