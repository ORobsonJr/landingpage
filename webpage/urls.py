from django.urls import path, include
from .views import IndexPage, convert_form

urlpatterns = [
    path('', IndexPage.as_view()),
    path('form_submission/', convert_form, name='form_submission')
]