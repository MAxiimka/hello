from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='primary'),
    path('stix/', views.stix, name='stix'),
    path('overview', views.overview, name='overview'),
    path('overview/<int:article_id>/', views.Detail, name='Detail'),
    path('overview/<int:article_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
]
