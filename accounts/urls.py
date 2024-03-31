from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.ContactView.as_view(), name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('post/', views.post, name='post'),
]
