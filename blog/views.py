from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/liste_des_publications.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/details_de_la_publication.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/creer_une_publication.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/modifier_une_publication.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/supprimer_une_publication.html'
    success_url = reverse_lazy('post_list')
