from django.db import models

# Create your models here.
# class DistrictManager(models.Manager):
    # def get_by_natural_key(self, lea_code, lea_school_year):
        # return self.get(lea_code=lea_code, lea_school_year=lea_school_year)

class District(models.Model):
	# objects = DistrictManager()

	lea_code = models.CharField(max_length=3, verbose_name="Code", primary_key=True)
	lea_name = models.CharField(max_length=150, verbose_name="Name")
	lea_city = models.CharField(max_length=150, verbose_name="City")
	lea_state = models.CharField(max_length=150, verbose_name="State")
	# lea_school_year = models.CharField(max_length=10, verbose_name="School Year")
	lea_type = models.CharField(max_length=1, verbose_name="Type")
	lea_email = models.CharField(max_length=100, null=True, verbose_name="Email")
	lea_superintendent = models.CharField(max_length=100, null=True, verbose_name="Superintendent")
	lea_website = models.URLField(max_length=250, null=True, verbose_name="Website")

	class Meta(object):
		verbose_name = "School District"
		verbose_name_plural = "School Districts"
		ordering = ('lea_name',)
		# unique_together = (('lea_code', 'lea_school_year'),)

	def __unicode__(self):
		return U'%s (%s)' %(self.lea_name, self.lea_code)

	# def natural_key(self):
		# return (self.lea_code, self.lea_school_year)

class Graduation(models.Model):
	district = models.ForeignKey('District')
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	# district = models.ForeignKey('District')
	graduation_rate = models.DecimalField(max_digits=6, decimal_places=5, null=True)
	female_graduation_rate = models.DecimalField(max_digits=6, decimal_places=5, null=True)
	male_graduation_rate = models.DecimalField(max_digits=6, decimal_places=5, null=True)
	native_american_graduation_rate = models.DecimalField(max_digits=6, decimal_places=5, null=True)
	asian_graduation_rate = models.DecimalField(max_digits=6, decimal_places=5, null=True)
	black_graduation_rate = models.DecimalField(max_digits=6, decimal_places=5, null=True)
	hispanic_graduation_rate = models.DecimalField(max_digits=6, decimal_places=5, null=True)
	multiracial_graduation_rate = models.DecimalField(max_digits=6, decimal_places=5, null=True)
	white_graduation_rate = models.DecimalField(max_digits=6, decimal_places=5, null=True)
	freelunch_graduation_rate = models.DecimalField(max_digits=6, decimal_places=5, null=True)
	notfreelunch_graduation_rate = models.DecimalField(max_digits=6, decimal_places=5, null=True)
	

	class Meta(object):
		verbose_name = "Graduation Rates"
		verbose_name_plural = "Graduation Rates"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s)' %(self.district.lea_name, self.school_year)
