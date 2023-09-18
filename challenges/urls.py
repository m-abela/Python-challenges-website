from django.urls import path
from . import views

urlpatterns = [
    path('', views.challenge_view, name='challenge_list'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('challenge/<int:challenge_id>/', views.challenge_detail, name='challenge_detail'),
    path('submit_solution/<int:challenge_id>/', views.submit_solution, name='submit_solution'),
    path('challenge_success/', views.challenge_success, name='challenge_success'),
    path('challenge_fail/', views.challenge_fail, name='challenge_fail'),

    path('writing/', views.writing, name='writing'),

]