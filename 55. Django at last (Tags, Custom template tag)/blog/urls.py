from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/', views.post_details, name='post_details'),
    path('contact-us/', views.contact_us, name='contact_us')
]