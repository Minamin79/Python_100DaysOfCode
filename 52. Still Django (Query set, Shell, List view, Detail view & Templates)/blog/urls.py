from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='Post_list'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/', views.post_details),
    path('contact-us/', views.contact_us)
]