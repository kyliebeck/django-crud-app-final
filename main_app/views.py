from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Craft, Hobby

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def craft_index(request):
    crafts = Craft.objects.all()
    return render(request, 'crafts/index.html', {'crafts': crafts})

def craft_detail(request, craft_id):
    craft = Craft.objects.get(id=craft_id)
    hobby = Hobby.objects.all()
    return render(request, 'crafts/detail.html', {'craft': craft})

class CraftCreate(CreateView):
    model = Craft
    fields = '__all__'

class CraftUpdate(UpdateView):
    model = Craft
    fields = '__all__'

class CraftDelete(DeleteView):
    model = Craft
    success_url = '/crafts/'

class HobbyCreate(CreateView):
    model = Hobby
    fields = '__all__'

class HobbyList(ListView):
    model = Hobby

class HobbyDetail(DetailView):
    model = Hobby

class HobbyUpdate(UpdateView):
    model = Hobby
    fields = '__all__'

class HobbyDelete(DeleteView):
    model = Hobby
    success_url = '/hobbies/'
