from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.
class Don_Nghi_Phep(models.Model):
	name_hs = models.CharField(max_length = 50)
	id_hs = models.CharField(max_length = 50)
	name_ph = models.CharField(max_length = 50)
	reason = models.TextField()
	tg_nghi = models.CharField(max_length = 50)
	date_time = models.DateTimeField(auto_now_add = True, auto_now = False)
	slug = models.SlugField(max_length=250, null = True, blank = True, unique = True)
	def save(self, *args, **kwargs):
		if self.slug is None or self.slug == '':
			self.slug = slugify(self.name_hs)
		super(Don_Nghi_Phep,self).save(*args, **kwargs)
	def __unicode__(self):
		return self.name_hs
	def __str__(self):
		return self.name_hs + ' - Đơn Xin Phép'
	def get_absolute_url(self):
		return reverse('Don_view', kwargs={"slug":self.slug})