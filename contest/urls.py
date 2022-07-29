from msilib.schema import ListView
from django.urls import path
from .views import AllContestView, ContestDetailView, ContestResultView
urlpatterns = [
    path('', AllContestView.as_view(), name = 'all-contest'),
    path('<int:pk>/',ContestDetailView.as_view(), name = 'contest-detail'),
    path('<int:pk>/result',ContestResultView.as_view(), name = 'contest-result')
]