from django.urls import path

from web.user.views import signin, signup, logout

urlpatterns = [
    # login/signup
    path('', signin, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),

]
