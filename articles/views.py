# articles/views.py
from django.contrib.auth.mixins import LoginRequiredMixin #restrict views
from django.core.exceptions import PermissionDenied #denying the change if the editor is not the author
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy

from .models import Article

'tell the program where they will use the db, on what UI? what db?'
class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
                raise PermissionDenied
        return super().dispatch(request, *args,**kwargs)

class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list.html')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
                raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title','body',)
    login_url = 'login' #show when 404 not logged in

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)