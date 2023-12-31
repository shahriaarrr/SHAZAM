from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('update_user/', views.update_user, name='update_user'),
    path('thunder_like/<int:pk>', views.thunder_likes, name="thunder_like"),
    path('thunder_show/<int:pk>', views.thunder_show, name="thunder_show"),
    path('hunt/<int:pk>', views.hunt, name="hunt"),
    path('unhunt/<int:pk>', views.unhunt, name="unhunt"),
    path('profile/hunters/<int:pk>', views.hunters, name='hunters'),
    path('profile/hunts/<int:pk>', views.hunts, name='hunts'),
    path('delete_thunder/<int:pk>', views.delete_thunder, name='delete_thunder'),
]