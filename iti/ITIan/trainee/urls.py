from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.Newstrainee, name='Newstrainee'),
    path('delete/<tr_id>', views.deletestudent, name='deletestudent'),
    path('edit/<tr_id>', views.edittrainee, name='edittrainee'),
]