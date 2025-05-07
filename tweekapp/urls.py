from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name="homepage"),
    path('tweeks/',views.tweek_list,name='tweek_list'),
    path('tweek_create/',views.tweek_create,name='tweek_create'),
    path('<int:tweek_id>/edit/',views.tweek_edit, name='tweek_edit'),
    path('<int:tweek_id>/delete/',views.tweek_delete,name='tweek_delete'),
    path('register/',views.register_user,name='register'),
    path('login/', views.custom_login, name='login'),
    path('accounts/logout/', views.custom_logout, name='logout'),
]
