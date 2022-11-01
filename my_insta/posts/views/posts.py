from django.views.generic import CreateView, View, FormView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,  PermissionRequiredMixin


from posts.forms import PostForm
from posts.models import Post
from posts.models import Comment
from accounts.forms import CommentForm


class PostCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'create_post.html'
    form_class = PostForm
    model = Post
    permission_required = 'posts.add_post'

    def has_permission(self):
        return super().has_permission() or self.get_object().email == self.request.user

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author_id = self.kwargs['pk']
            post = form.save()
            return redirect('profile', pk=self.kwargs['pk'])
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


class PostView(DetailView):
    template_name = 'post_detail.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self,  **kwargs):
        comments = Comment.objects.all()
        context = super(PostView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = comments
        return context


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'post_update.html'
    form_class = PostForm
    model = Post
    context_object_name = 'post'
    permission_required = 'posts.change_post'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user


    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostLikeView(LoginRequiredMixin, View):
    model = Post

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        post.user_likes.add(request.user)
        count = post.like_count
        Post.objects.filter(id=post.id).update(like_count=(count + 1))
        return redirect('index')


class CommentCreateView(LoginRequiredMixin, FormView):
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')
            user = request.user
            comment = Comment.objects.create(author=user, post=post, text=comment)
            user.commented_posts.add(post)
            count = post.comment_count
            Post.objects.filter(id=post.id).update(comment_count=(count + 1))
        return redirect('index')


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'post_confirm_delete.html'
    model = Post
    success_url = '/'
    permission_required = 'posts.change_post'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

