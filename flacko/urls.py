from django.urls import path
from .views import (JordyListView, JordyDetailView, JordyCreateView, JordyUpdateView, JordyDeleteView,
                    LordListView, LordDetailView, LordCreateView, LordUpdateView, LordDeleteView)

urlpatterns = [
    path('jordy/list/', JordyListView.as_view(), name="jordy_list"),
    path('jordy/<int:pk>/', JordyDetailView.as_view(), name="jordy_detail"),
    path('jordy/<int:pk>/edit/', JordyUpdateView.as_view(), name="jordy_edit"),
    path('jordy/new/', JordyCreateView.as_view(), name="jordy_create"),
    path('jordy/<int:pk>/delete/', JordyDeleteView.as_view(), name="jordy_delete"),
    path('lord/list/', LordListView.as_view(), name="lord_list"),
    path('lord/<int:pk>/', LordDetailView.as_view(), name="lord_detail"),
    path('lord/<int:pk>/edit/', LordUpdateView.as_view(), name="lord_edit"),
    path('lord/new/', LordCreateView.as_view(), name="lord_create"),
    path('lord/<int:pk>/delete/', LordDeleteView.as_view(), name="lord_delete"),
]