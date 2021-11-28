from django.conf.urls import url,include
from . import views
from django.urls import path
urlpatterns = [
	url('login',views.Login),
	url('dash',views.Home1),
	url('logout',views.Logout),
	url('forms',views.Forms),
	url('chart',views.Charts),
	url('file_csv',views.File_csv),
	url('gv',views.Forms_gv),
	path('donxinphep/<slug:slug>/',views.Don_view),

]