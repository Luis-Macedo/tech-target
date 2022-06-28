from django import views
from django.urls import path
from dashboards import views

urlpatterns = [
    path('perQuestion/<int:question_id>', views.dash_per_question, name="dashPerForm")
]