from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Form
from django.views.decorators.csrf import csrf_protect

# Create your views here.
class IndexPage(TemplateView):
    template_name = 'index.html'

@csrf_protect
def convert_form(request):
    if request.method == 'POST':
        first_name_ = request.POST.get('first_name')
        last_name_ = request.POST.get('last_name')
        email_ = request.POST.get('email')

        #save the fields inside database
        form_ = Form(first_name=first_name_, last_name=last_name_, email=email_)
        form_.save()

      
    return render(request, 'index.html')