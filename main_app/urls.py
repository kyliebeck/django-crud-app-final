
from django.urls import path
from . import views
from django.views.generic.edit import CreateView, UpdateView, DeleteView # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crafts/', views.craft_index, name='craft-index'),
    path('crafts/<int:craft_id>/', views.craft_detail, name='craft-detail'),
    path('crafts/create/', views.CraftCreate.as_view(), name='craft-create'),
    path('crafts/<int:pk>/update/', views.CraftUpdate.as_view(), name='craft-update'),
    path('crafts/<int:pk>/delete/', views.CraftDelete.as_view(), name='craft-delete'),
    path('hobbies/create/', views.HobbyCreate.as_view(), name='hobby-create',),
    path('hobbies/<int:pk>/', views.HobbyDetail.as_view(), name='hobby-detail'),
    path('hobbies/', views.HobbyList.as_view(), name='hobby-index'),
]
