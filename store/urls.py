from django.conf.urls import url

from store.views import index, login

urlpatterns = [
    url(r'^$', index.index_view, name='index'),
    url(r'^login/$', login.login_view, name='login')
]
