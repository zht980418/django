from django.contrib import admin

from django.urls import path

from django.urls import include

from django.conf import settings

from django.conf.urls.static import static

from rango import views

from registration.backends.simple.views import RegistrationView

from django.urls import reverse



class MyRegistrationView(RegistrationView):

    def get_success_url(self, user):

        return reverse('rango:register_profile')



urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),

    path('rango/', include('rango.urls')),

    path('admin/', admin.site.urls),

    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),

    path('accounts/', include('registration.backends.simple.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)