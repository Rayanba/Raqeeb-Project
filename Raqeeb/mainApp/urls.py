from django.urls import path
from . import views


urlpatterns = [
    path('main/',views.main, name= 'main'),
    path('dashboard/',views.dashboard, name= 'dashboard'),
    path('form/',views.upload, name= 'upload'),
    # path('report/',views.report, name= 'report')
]