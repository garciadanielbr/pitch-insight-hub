"""pitch_insight_hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from analytics.views import PlayerViewSet, MatchViewSet, PlayerPerformanceViewSet, TopScorersView, TeamPerformanceView

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'performances', PlayerPerformanceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/top-scorers/', TopScorersView.as_view(), name='top-scorers'),
    path('api/team-performance/', TeamPerformanceView.as_view(), name='team-performance'),
]