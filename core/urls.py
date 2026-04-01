from django.urls import path
from .views import competitions_view, competitions_users_page_view, results_view, home_view, login_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('results/', results_view, name='results'),
    path('competitions/', competitions_view, name='competitions'),
    path('competitions-users-page/', competitions_users_page_view, name='competitions-users-page')
]


