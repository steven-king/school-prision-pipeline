from django.db import models

# Create your models here.

class District(models.Model):
	lea_code = models.CharField(max_length=4, verbose_name="Code")
	lea_name = models.CharField(max_length=150, verbose_name="Name")
	lea_city = models.CharField(max_length=150, verbose_name="City")
	lea_state = models.CharField(max_length=150, verbose_name="State")
	lea_school_year = models.CharField(max_length=10, verbose_name="School Year")
	lea_type = models.CharField(max_length=1, verbose_name="Type")
	lea_email = models.CharField(max_length=100, null=True, verbose_name="Email")
	lea_superintendent = models.CharField(max_length=100, null=True, verbose_name="Superintendent")
	lea_website = models.URLField(max_length=250, null=True, verbose_name="Website")

	class Meta(object):
		verbose_name = "School District"
		verbose_name_plural = "School Districts"
		ordering = ('lea_name', 'lea_school_year')

	def __unicode__(self):
		return U'%s (%s)' %(self.lea_name, self.lea_school_year)
