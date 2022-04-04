from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('pirates/', views.pirate_list),
    path('pirates/<int:pk>', views.pirate_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)