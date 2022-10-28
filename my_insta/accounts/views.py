from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import LoginForm
from django.core.paginator import Paginator

from accounts.forms import CustomUserCreationForm

from accounts.forms import UserChangeForm

from posts.models import Post
from accounts.models import Account


# from accounts.forms import ProfileChangeForm


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        next = request.GET.get('next')
        form_data = {} if not next else {'next': next}
        form = self.form(form_data)
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        next = form.cleaned_data.get('next')
        user = authenticate(request, email=email, password=password)
        print(user)
        if not user:
            return redirect('login')
        login(request, user)
        if next:
            return redirect(next)
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    # success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():

            account = form.save()
            login(request, account)

            print(account)
            return redirect('profile', pk=account.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)





# class ProfileView(LoginRequiredMixin, DetailView):
#     model = get_user_model()
#     template_name = 'user_detail.html'
#     context_object_name = 'account'
#
#
#     def get_context_data(self, **kwargs):
#         posts = self.object.posts.order_by('-created_at')
#         account = Account.objects.get(id=25)
#         posts_count = Post.objects.filter(author=account).count()
#         print(posts_count)
#         kwargs['posts_count'] = posts_count
#         kwargs['posts'] = posts
#         return super().get_context_data(**kwargs)

class ProfileView(DetailView):
    template_name = 'user_detail.html'
    model = Account

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = self.object
        posts = account.posts.order_by('-created_at').exclude(is_deleted=True)
        context['posts'] = posts
        return context

class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'


    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})

