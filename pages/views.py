from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, render

# Create your views here.
# Function based Views vs. Class Based Views


class HomePageView(TemplateView): #Heritage - OOP (Object Oriented Programming)
  template_name = "pages/home.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["name"] = "Courtney"
    return context
  

class AboutPageView(TemplateView):
  template_name = "pages/about.html"


# Function Based Views
def contact_page(request):
  # return HttpResponse("Hello World from FBV")

  contact_info = {
    "name": "Courtney",
    "address": "We are conveniently located at 1084 South Long Street, Tokyo, JP, 901-0112",
    "email": "Allinline@gmail.com",
  }

  return render(request, "pages/contact.html", contact_info)