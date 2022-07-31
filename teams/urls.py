from django.urls import path
from .views import TeamsListView , TeamsDetailView , TeamsCreateView , TeamsUpdateView , TeamsDeleteView

urlpatterns = [
  path('',TeamsListView.as_view(),name='teams_list'),
  path('<int:pk>/',TeamsDetailView.as_view(), name='teams_detail'),
  path('create/',TeamsCreateView.as_view(), name='teams_create'),
  path('<int:pk>/update/',TeamsUpdateView.as_view(),name='teams_update'),
  path('<int:pk>/delete/',TeamsDeleteView.as_view(),name='teams_delete')
]
