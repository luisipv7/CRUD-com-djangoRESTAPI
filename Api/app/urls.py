from django.conf.urls import url
from app import views

app_name = 'api'
urlpatterns = [
    url(r'^contatos$', views.contato_list),
    url(r'^contatos/(?P<pk>[0-9]+)$', views.contato_detail),
    url(r'^contatos/published$', views.contato_list_published)
]
