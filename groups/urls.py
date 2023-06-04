from django.urls import path

from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name="all"),
    path('new/', views.CreateGroup.as_view(), name="create"),
    path('groups/<slug:slug>/', views.SingleGroup.as_view(),name="single"),
    path('groups/<slug:slug>/join/', views.JoinGroup.as_view(),name="join"),
    path('groups/<slug:slug>/leave/', views.LeaveGroup.as_view(),name="leave"),
]
