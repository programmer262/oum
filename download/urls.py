from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('Cours',views.cour,name='cour'),
    path('exercice/',views.exercice,name='exercice'),
    path('correction/',views.correction,name='correction'),
  	path('register/', views.registerPage, name="register"),
	path('', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('classe/', views.classe, name="classe"),
	path('endlive/', views.live, name="live"),

	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
