from django.urls import path
from . import views_example

app_name = 'store'

urlpatterns = [
    path('', views_example.index, name='home'),
    path('test/', views_example.test_view, name="test_vies"),
    path('browse/', views_example.browse, name='browse'),
    path('simple/', views_example.SimpleClassBasedView.as_view(), name='simple'),
]