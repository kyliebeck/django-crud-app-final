from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Craft, Hobby
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('craft-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)



class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def craft_index(request):
    crafts = Craft.objects.filter(user=request.user)
    return render(request, 'crafts/index.html', {'crafts': crafts})

@login_required
def craft_detail(request, craft_id):
    craft = Craft.objects.get(id=craft_id)
    hobbies = Hobby.objects.all()
    hobbies_craft_doesnt_have = Hobby.objects.exclude(id__in = craft.hobbies.all().values_list('id'))
    return render(request, 'crafts/detail.html', {
        'craft': craft,
        'hobbies': hobbies,
        'hobbies': hobbies_craft_doesnt_have
        })

def associate_hobby(request, craft_id, hobby_id):
    Craft.objects.get(id=craft_id).hobbies.add(hobby_id)
    return redirect('craft-detail', craft_id=craft_id)



class CraftCreate(LoginRequiredMixin, CreateView):
    model = Craft
    fields = ['title', 'duration', 'level', 'supplies', 'instructions']
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class CraftUpdate(LoginRequiredMixin, UpdateView):
    model = Craft
    fields = ['title', 'duration', 'level', 'supplies', 'instructions']

class CraftDelete(LoginRequiredMixin, DeleteView):
    model = Craft
    success_url = '/crafts/'

class HobbyCreate(LoginRequiredMixin, CreateView):
    model = Hobby
    fields = ['name', 'description']

class HobbyList(LoginRequiredMixin, ListView):
    model = Hobby

class HobbyDetail(LoginRequiredMixin, DetailView):
    model = Hobby

class HobbyUpdate(LoginRequiredMixin, UpdateView):
    model = Hobby
    fields = '__all__'

class HobbyDelete(LoginRequiredMixin, DeleteView):
    model = Hobby
    success_url = '/hobbies/'
