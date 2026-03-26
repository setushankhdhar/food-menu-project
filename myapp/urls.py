from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.Detail.as_view(),name="detail"),
    path('create_item/',views.CreateItem.as_view(), name = 'create_item'),
    path('edit/<int:pk>',views.Edit.as_view(), name = 'edit'),
    path('delete/<int:pk>',views.Delete.as_view(), name = 'delete'),
]