# articles/views.py
from django.contrib.auth.mixins import LoginRequiredMixin #restrict views
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy

from .models import Article

'tell the program where they will use the db, on what UI? what db?'
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list.html')

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title','body',)
    login_url = 'login' #show when 404 not logged in

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)