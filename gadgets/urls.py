from django.urls import path
from gadgets import views
from SmartDog import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login,logout

urlpatterns = [
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('experts/',views.expert,name='expert'),
    path('login/',login,{'template_name':'gadgets/login.html'},name='login'),
    path('dog_training/',views.dogtrain,name='dogtrain'),
    path('dog_grooming/',views.doggroom,name='doggroom'),
    path('dog_selfwash/',views.dogwash,name='dogwash'),
    path('dog_sitting/',views.dogsit,name='dogsit'),
    path('veterinary_care/',views.vetercare,name='vetercare'),
    path('pet_adoptions/',views.petadopt,name='petadopt'),
    path('<slug:menu>',views.summary,name='summary'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)