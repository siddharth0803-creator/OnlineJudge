from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:problem_id>/', views.Description, name='Description'),
    path('<int:problem_id>/Result/', views.Result, name='Result'),
    #path('runcode',views.runcode, name='runcode')
]
