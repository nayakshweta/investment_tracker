from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.total_investment, name='total_investment'),
]