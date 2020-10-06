from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context={
        'posts':  Post.objects.all()
        
    }
    return render(request, 'intern_blog/home.html',context)


class PostListView(ListView):
   
    model = Post

    template_name = 'intern_blog/home.html'
 
    
    context_object_name='posts'
    ordering=['-date']


def categoryview(request,category):
    print(category)
    if (category,category) not in Post.CATEGORIES:
        print ("yes")
        category="other"
    context = {
        'posts':  Post.objects.filter(category=category).order_by('-date')

    }
    return render(request, 'intern_blog/home.html', context)

# class CategoryListView(ListView,category):

#     model = Post

#     template_name = 'intern_blog/category.html'

#     context_object_name = 'posts'
#     ordering = ['-date']


class PostDetailView(DetailView):
    model = Post
    

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['title', 'content','category']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url ='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
   


def about(request):
    return render(request, 'intern_blog/about.html')
