from urlShort import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='home'),
    path('url/<decode>', views.redirect_to_original, name='go')
]
