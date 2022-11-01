from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Q
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import LoginForm
from django.core.paginator import Paginator

from accounts.forms import CustomUserCreationForm

from accounts.forms import UserChangeForm

from posts.models import Post
from accounts.models import Account

from accounts.forms import PasswordChangeForm

from accounts.forms import SearchForm


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
        account = authenticate(request, email=email, password=password)
        if not account:
            return redirect('login')
        login(request, account)
        if next:
            return redirect(next)
        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('login')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    # success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            account = form.save()
            login(request, account)
            return redirect('profile', pk=account.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class ProfileView(DetailView):
    template_name = 'user_detail.html'
    model = Account
    answer = 'accounts'

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        print(self.request.GET)
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.search_value:
            queryset = Account.objects.filter(Q(username__icontains=self.search_value) |
                                              Q(email__icontains=self.search_value) |
                                              Q(first_name__icontains=self.search_value))
            if len(queryset) == 0:
                self.answer = 'no'
            else:
                self.answer = 'yes'
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = self.object
        subscriptions = account.subscriptions.count()
        subscribers = account.subscribers.count()
        # posts = account.posts.order_by('-created_at').exclude(is_deleted=True)
        posts = Post.objects.filter(author=account).order_by('-created_at').exclude(is_deleted=True)
        if self.search_value:
            context['accounts'] = self.get_queryset()
            print(self.get_queryset())
            print(self.answer)
        context['answer'] = self.answer
        context['posts'] = posts
        context['form'] = self.form
        context['subscriptions'] = subscriptions
        context['subscribers'] = subscribers
        return context


class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'


    def get_context_data(self, **kwargs):
        if 'profile_form' not in kwargs:
            kwargs['profile_form'] = self.get_profile_form()
        return super().get_context_data()

    def get_profile_form(self):
        form_kwargs = {'instance': self.object}
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
        return UserChangeForm(**form_kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        profile_form = self.get_profile_form()
        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        response = super(UserChangeView, self).form_valid(form)
        profile_form.save()
        return response

    def form_invalid(self, form, profile_form):
        context = self.get_context_data(form=form, profile_form=profile_form)
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(UpdateView):
    model = get_user_model()
    template_name = 'user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('login')


class ProfileFollowView(TemplateView):
    template_name = 'profile.html'

    def post(self, request, *args, **kwargs):
        from_user = request.user
        to_user = Account.objects.get(id=kwargs['pk'])
        to_user.subscribers.add(from_user)
        return redirect('profile', pk=to_user.pk)


