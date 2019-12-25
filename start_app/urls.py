from django.urls import path
from django.conf.urls import url
from start_app import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", views.start, name='start'),
    path("searchResult", views.searchResult, name='searchResult'),
    path("search/<search_key>/", views.deals_by_search_data, name='deals_by_search_data'),
    # path("/signin/", views.signin, name='signin'),
    # path("/signup/", views.signup, name='signup'),
    # url(r'^signin/', views.signin),
    url(r'^signup/', views.signup),


    # path('signin/', views.signin, name='loginpage'),

    # path('profile/', views.profile, name='profile'),
    # path('logout/', views.logout, name='logout'),

   ]
