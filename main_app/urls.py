
from django.urls import path
from . import views


urlpatterns = [
     path('accounts/signup/', views.signup, name='signup'),
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('crafts/', views.craft_index, name='craft-index'),
    path('crafts/<int:craft_id>/', views.craft_detail, name='craft-detail'),
    path('crafts/create/', views.CraftCreate.as_view(), name='craft-create'),
    path('crafts/<int:pk>/update/', views.CraftUpdate.as_view(), name='craft-update'),
    path('crafts/<int:pk>/delete/', views.CraftDelete.as_view(), name='craft-delete'),
    path('hobbies/create/', views.HobbyCreate.as_view(), name='hobby-create'),
    path('hobbies/<int:pk>/', views.HobbyDetail.as_view(), name='hobby-detail'),
    path('hobbies/', views.HobbyList.as_view(), name='hobby-index'),
    path('hobbies/<int:pk>/update/', views.HobbyUpdate.as_view(), name='hobby-update'),
    path('hobbies/<int:pk>/delete/', views.HobbyDelete.as_view(), name='hobby-delete'),
    path('crafts/<int:craft_id>/associate-hobby/<int:hobby_id>/', views.associate_hobby, 
    name='associate-hobby'),
   

]

