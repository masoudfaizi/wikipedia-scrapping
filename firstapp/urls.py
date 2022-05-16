from django.urls import path
from firstapp.views import DataListView, DataDetailView

urlpatterns = [
    path('', DataListView.as_view()),
    path('<int:pk>', DataDetailView.as_view(), name='data-detail'),
]
