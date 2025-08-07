from django.urls import path
from . import views
app_name = "leads"

urlpatterns =[
    path('landing',views.landing, name="landing"),
    path('', views.home_page, name="index"),
    path('<int:pk>', views.lead_details, name="details"),
    #path("details", views.lead_details, det),
    path("create/", views.lead_create, name="create"),
    path('update/<int:pk>', views.update, name = "update"),
    path('delete/<int:pk>', views.delete, name="delete")
]