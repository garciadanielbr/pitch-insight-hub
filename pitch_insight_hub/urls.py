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
from analytics.views import LeagueView, SeasonView, TeamView, FixtureView, TeamFormGuideView

router = DefaultRouter()
router.register(r'leagues', LeagueView)
router.register(r'seasons', SeasonView)
router.register(r'teams', TeamView)
router.register(r'fixtures', FixtureView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/teams/<int:team_id>/form-guide/', TeamFormGuideView.as_view(), name='team-form-guide'),
]

