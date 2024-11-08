from django.urls import path
from .views import index
from School_CRUD import views

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:detail_id>', views.detailPage)
]
