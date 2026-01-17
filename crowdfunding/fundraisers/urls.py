from django.urls import path
from . import views #The . here means "in this folder"

urlpatterns = [
    path('fundraisers/', views.FundraiserList.as_view()),
]