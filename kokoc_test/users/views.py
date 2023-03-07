from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


from .forms import CreationForm


User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('test:index')
    template_name = 'users/signup.html'


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'users/profile.html', context)


def list_of_users(request):
    users = User.objects.all()
    context = {'users': users }
    return render(request, 'users/list_users.html', context)
