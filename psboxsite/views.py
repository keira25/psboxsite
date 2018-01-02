from django.views.generic import TemplateView

class home_view(TemplateView):
  template_name = 'home.html'

class signup_view(TemplateView):
  template_name = 'signup.html'

class login_view(TemplateView):
  template_name ='login.html'