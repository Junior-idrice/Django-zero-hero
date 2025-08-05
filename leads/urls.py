from django.urls import path
from . import views
app_name = "leads"

urlpatterns =[
    path('', views.home_page, name="home"),
    path('<int:pk>', views.lead_details, name="details"),
    path("details", views.lead_details),
    path("create/", views.lead_create),
    path('update/<int:pk>', views.update)
]