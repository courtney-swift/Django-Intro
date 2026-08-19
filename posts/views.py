from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView,
)
from.models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView): # GET Request -> List
  # model attribute let django know from which model (table) we want to retrieve the data
  model = Post
  # context_object_name attribute allow us to change the name of how we call it inside of the template
  context_object_name = "posts"
  template_name = "posts/list.html"

  # SELECT * FROM posts

class PostDetailView(DetailView): # GET Request -> Single Object
  template_name = "posts/detail.html"
  model = Post
  context_object_name = "single_post"

class PostCreateView(CreateView):
  template_name = "posts/new.html"
  model = Post
  fields = ["title", "subtitle", "body"]

  def form_valid(self, form):
    # This function help us to run some validations before we create the abject
    form.instance.author = User.objects.last()
    return super().form_valid(form)

class PostUpdateView(UpdateView):
  template_name = "posts/edit.html"
  model = Post
  fields = ["title", "subtitle", "body"]

class PostDeleteView(DeleteView): # POST Request -> A form to handle the delete functionality 
  template_name = "posts/delete.html"
  model = Post
  # success_url attribute allow us to redirect the uster to another view if the request is successful
  success_url = reverse_lazy("post_list")