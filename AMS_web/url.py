from django.conf.urls import url
from . import views

urlpatterns = [
	url('home',views.Home, name = 'home'),
	url('Download',views.Download, name = 'download'),
	url('Documents',views.Documents, name = 'documents'),
	url('Contact',views.Contact, name = 'contact'),



]