from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Blog
from .utils import paginate_blogs


def blog_home(request):
    posts = Blog.objects.filter(is_published=True).select_related('cat')
    custom_range, posts = paginate_blogs(request, posts, 3)
    context = {
        'posts': posts,
        'custom_range': custom_range,
        'cat_selected': 0,
    }
    return render(request, 'blog/blog.html', context)


# class BlogHome(DataMixin, ListView):
#     template_name = 'blog/blog.html'
#     context_object_name = 'posts'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cat_selected'] = 0
#         context['title'] = 'Главная страница'
#         return context
#
#     def get_queryset(self):
#         return Blog.objects.filter(is_published=True).select_related('cat')


def show_post(request, post_slug):
    post = Blog.objects.get(slug=post_slug)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.post = post
        review.owner = request.user
        review.save()
        messages.success(request, 'Ваш отзыв добавлен')
        return redirect('post', post_slug=post.slug)

    context = {
        'post': post,
        'cat_selected': 1,
        'form': form,
    }
    return render(request, 'blog/post.html', context)


# class ShowPost(DetailView):
#     model = Blog
#     template_name = 'blog/post.html'
#     slug_url_kwarg = 'post_slug'
#     context_object_name = 'post'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = context['post']
#         return context


def blog_category(request, cat_slug):
    posts = Blog.objects.filter(cat__slug=cat_slug, is_published=True).select_related('cat')
    custom_range, posts = paginate_blogs(request, posts, 3)
    context = {
        'posts': posts,
        'title': 'Категория - ' + str(posts[0].cat),
        'cat_selected': posts[0].cat_id,
        'custom_range': custom_range,
    }
    return render(request, 'blog/blog.html', context)

# class BlogCategory(DataMixin, ListView):
#     model = Blog
#     template_name = 'blog/blog.html'
#     context_object_name = 'posts'
#
#     allow_empty = False
#
#     def get_queryset(self):
#         return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Категория - ' + str(context['posts'][0].cat)
#         context['cat_selected'] = context['posts'][0].cat_id
#         return context
