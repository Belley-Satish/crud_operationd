from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login_user'),
    path('registration/',views.registration,name='registration'),
    path('logout',views.logout_user,name='logout_user'),
    path('search',views.search,name='search'),
    path('create',views.create,name='create'),
    path('update/<int:id>',views.update,name='update'),
    path('update1',views.update1,name='update1'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('completed',views.completed,name='completed'),
    path('InComplete',views.InComplete,name='InComplete'),
    path('InProgress',views.InProgress,name='InProgress'),
]
