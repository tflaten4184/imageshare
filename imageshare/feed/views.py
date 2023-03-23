from django.shortcuts import render
from django.views.generic import TemplateView, FormView, DetailView

from .models import Post
from .forms import PostForm



class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context

class PostView(FormView):
    template_name = "post.html"
    form_class = PostForm
    success_url = "/" # home, feed

    def form_valid(self, form):
        # form.save() # Why not this?
        Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image']
        )
        return super().form_valid(form)



class DetailPostView(DetailView):
    template_name="detail.html"
    model = Post

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['queryset'] = self
    #     return context