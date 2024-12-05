from urlShort import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('<decode>', views.redirect_to_original, name='go')
]