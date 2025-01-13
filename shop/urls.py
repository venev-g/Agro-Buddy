from django.urls import path
from shop.views import login_view, signup_view, home_view  

urlpatterns = [
    path('login/', login_view, name='Login.html'),    # URL for login
    path('signup/', signup_view, name='signup'),  # URL for signup
    path('home/', home_view, name='home'),        # URL for home page
    path('', home_view, name='home'),             # Root URL to home page (optional)
    
]
