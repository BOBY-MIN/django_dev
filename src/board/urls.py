'''
Created on 2021. 5. 3.

@author: 이상민
'''

from django.urls import path
from board import views

app_name = 'board'

urlpatterns = [
        path('', views.index),
        path('post', views.post),
        path('detail/<int:id>', views.detail),
        path('delete/<int:id>', views.delete),
        path('modify/<int:id>', views.modify),
        path('update', views.update),
    ]