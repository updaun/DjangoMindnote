from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    # path('info/', views.info),
    path('diary/', views.page_list),
    # path('write/', views.page_create),
    path('diary/<int:page_id>/', views.page_detail, name="page-detail"),
    # path('page/<int:page_id>/edit', views.page_update),
    # path('page/<int:page_id>/delete', views.page_delete),
]
