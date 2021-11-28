from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, get_user_model, logout
from django.contrib.auth.models import User
from django.contrib.auth import login as login1, logout as logout1
from . models import Don_Nghi_Phep
import pandas as pd
import pyrebase
from django.contrib.auth.models import Permission,User,Group
from django import template

#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore
# Create your views here.
config = {
    'apiKey': "AIzaSyDuj71EoOO5uUNS7D8our207Bkd458s354",
    'authDomain': "attendacedatabase.firebaseapp.com",
    'databaseURL': "https://attendacedatabase-default-rtdb.firebaseio.com",
    # 'databaseURL': "https://attendacedatabase.appspot.com",
    'projectId': "attendacedatabase",
    'storageBucket': "attendacedatabase.appspot.com",
    'messagingSenderId': "230822404841",
    'appId': "1:230822404841:web:62c0a61dac3d912141c678",
    'measurementId': "G-84CGL20Y2Y"
}
'''
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "attendacedatabase",
    "private_key_id": "354a8697f2cb2244702e78f3144959593a9d837f",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC37yU2vbDs6D5z\n8oUyWn+tna6sj+OVjs/rcTutqh6HqK2Hnhzg7yUwKHiildTO4PvsBdIKG8efCkc3\nIvH2OySmClzYT6hxNwf+txTCTrpV7Zor2oQsQ4gSF04lI6qa5rrxX029pN2zrUxc\nulkH4CL34QthLXh/fPrHZlFBXWdgKW5xd6XCTRahkfBARqw1HVj1kQtTrtraMa5h\nNnonjs/P+YEg1Hq7Gc40ZansUWR0CEFi8huUj0OZ91FQ8XlL823MzspegGjOXg65\npYJSWh+ymjTunxbUQM8qq02oBhkIZ4ZkW2njGIkbT/w682c5E6UeFcahV3EkmOuS\nLtOYfZgPAgMBAAECggEAAdSqbEHCfCeQ0F4GfF23oQNAq1M6HF5FBh6YGpGzmkpD\nNX/Z4SIQOGTJ7cuLyDL0eI3TehB663bSbNaQtCo0Va2LU6ELV9q73iNCKVYkqnLi\nEqcRb+omKKpWhHq3GbHLnfGcZPntaPq3F8Jh3RKA8DJ4IG0vvCXpNK95UvftupPH\ndHV3SQrmxi6p4Dnsc+B8iGSUmybKIqsp83jckE3NLCb5P/cicC4XGH69fxCnZzjc\nrCxnX/DnfTUyUd0/7FV04n1ELEpb2w8UusOCzZoReLt1NNn/hgS49+SXSlt64TuY\nyUVTyaewoxI5o+TnB9y+qH0q9CjBU9nShuOMtoNmNQKBgQDtWJgFnw+WEZNE7wXN\nyBPSjlywhm/ZbEHzE7zfGJx3he53EGuLo52492m0ciRwPAIbvOjk0kvez8lZgbJp\nYTSCzU5da9fodHJh2h0yJdY3KwqFlcni6a7qyM1apf8lPbbOwn6UAPAMQkN8g9Gs\nxF2QnkOhj9S1xkyrzrGwC9GjPQKBgQDGY+c4zN2UOyF1FXFskuTdnYPyCtMLsGE4\n/h17XIKLA03fvevlRksxOeixTilRC2BB5D/xWtHYDL74X9byuYAUB/VukuzjeqMd\nS3E/689tdGXVc3CMGE/25nSAoHlMwcBecHx21lCPi0dS456jRodUkwqGMOdc+t5o\nsUm56hxtOwKBgQDXMWhEUH81NSItcfn1Jd6zHVh0xK9MlpcE6XRpYksbI1eepEie\nBu7N8aTpckQPbpkKxTDzpqgbkJGikbFNUlDl93eBxHGx1UKP7c5i1WNwCZo0nCa7\nkdyCCyYFdlPrVBUXSciyMFd1Be9iSbIlzrR2lsgDCAF3/h8t9u2sDEs6kQKBgE1z\n32erg65FT5CYaInM55El18d9NlvP5oULoJLy0PxYs+RwD1KZmO2FADWIoFTFrjTL\nWbNuk5JXl478S7zDcx9e5BDhR56f2GKte29LLtY6pS8qPHxVWZK48i7td63hzqqQ\nG+eBUD5aT+QqfVqdRGRea7NsEEeaoY4Z+QCeR67VAoGAaSD4UFizqTpyZVz5sczD\n9MkptxbMsHrSEenp+oDQKKtLdnM/KAfx7XfvTVO2iXPXxhW5hpksN9repA9AxXY8\nb46JFn4JtHM+BT7g/W3xbxuZmgImGUoi7pB7y+zQXv+i8JlCXUBNhfshNifwtMv0\nEKIJ1kiDVwQff4Q7rdumt4g=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-2nop0@attendacedatabase.iam.gserviceaccount.com",
    "client_id": "108178671855854076135",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-2nop0%40attendacedatabase.iam.gserviceaccount.com"
})
'''
#firebase_admin.initialize_app(cred)
firebase = pyrebase.initialize_app(config)
database = firebase.database()

'''
register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 
'''
def Login(request):
	if request.user.is_staff or request.user.is_superuser:

		return HttpResponseRedirect("dash")

	user = request.POST.get("user")
	password = request.POST.get("password")
	print(user, password)

	user = authenticate(request, username=user, password=password)
	if user:
		if user.is_active:
			login1(request, user)
			return HttpResponseRedirect('dash')
	return render(request, 'login.html')


def Home1(request):
	if request.user.is_staff or request.user.is_superuser:
		Username = request.user.username
		return render(request, 'home1.html', {'username': Username})
	else:
		return HttpResponseRedirect('login')


def Forms(request):
	Username = request.user.username
	name_hs = request.POST.get("name_hs")
	id_hs = request.POST.get("id_hs")
	name_ph = request.POST.get("name_ph")
	reason = request.POST.get("reason")
	tg_nghi_from = request.POST.get("tg_nghi_from")
	tg_nghi_to = request.POST.get("tg_nghi_to")
	print(name_hs, id_hs, name_ph, reason)
	try:
		database.child(u'Manager').child(u'Khoi' + id_hs[0]).child(u'Lop ' + id_hs[0] + '-' + id_hs[1:3]).child(u'SBD:'+id_hs[3:6]).child(u'TTHS').child(u'status').set({"2021-11-17":"Vắng - có phép"})
	except:
		pass
	try:
		don_nghi_phep = Don_Nghi_Phep.objects.create(name_hs=name_hs, id_hs=id_hs, name_ph=name_ph,
	reason=reason, tg_nghi=str(tg_nghi_from)+' to '+str(tg_nghi_to))
	except:
		pass
	return render(request, 'forms.html', {'username': Username})


def Forms_gv(request):
	Username = request.user.username
	don_nghi_phep = Don_Nghi_Phep.objects.all()
	if request.user.groups.filter(name = 'GV'):
		print('ffdfdfdfdfff')
	else:
		print('faillllllllllllllllllllll')
	tim_hs = request.GET.get("tim_hs")
	if tim_hs:
		don_nghi_phep = don_nghi_phep.filter(name_hs=tim_hs)
	return render(request, 'forms_gv.html',{'username':Username, 'don_nghi_phep':don_nghi_phep})

def Charts(request):
	Username = request.user.username
	return render(request, 'chart.html',{'username':Username})

def File_csv(request):
	Username = request.user.username
	l = []
	file_atd = pd.read_csv('C:/Users/LENOVO/Desktop/Attendance/pyfile/myData.csv',encoding = 'utf-8')
	print(file_atd)
	for i in range(len(file_atd['stt'])):
		stt = file_atd.iloc[i]
		l.append(stt)
	return render(request, 'file_csv.html',{'username':Username,  'stt':l})

def Don_view(request,slug = None):
	Username = request.user.username
	intance = Don_Nghi_Phep.objects.get(slug = slug)
	print(intance)
	context = {

	'name_hs':intance.name_hs,
	'id_hs':intance.id_hs,
	'name_ph':intance.name_ph,
	'reason': intance.reason,
	'slug': slug,
	'username':Username

	}
	return render(request, 'doc.html',context)
def Logout(request):
	logout1(request)
	return HttpResponseRedirect('login')