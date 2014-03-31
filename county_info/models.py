from django.db import models

# Create your models here.
class District(models.Model):
	lea_code = models.CharField(max_length=3, verbose_name="Code", primary_key=True)
	lea_name = models.CharField(max_length=150, verbose_name="Name")
	lea_city = models.CharField(max_length=150, verbose_name="City")
	lea_state = models.CharField(max_length=150, verbose_name="State")
	lea_type = models.CharField(max_length=1, verbose_name="Type")
	lea_email = models.CharField(max_length=100, null=True, verbose_name="Email")
	lea_superintendent = models.CharField(max_length=100, null=True, verbose_name="Superintendent")
	lea_website = models.URLField(max_length=250, null=True, verbose_name="Website")

	class Meta(object):
		verbose_name = "School District"
		verbose_name_plural = "School Districts"
		ordering = ('lea_name',)

	def __unicode__(self):
		return U'%s (%s)' %(self.lea_name, self.lea_code)


class Graduation(models.Model):
	district = models.ForeignKey('District')
	school_year = models.CharField(max_length=10, verbose_name="School Year")
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


class DisciplineRate(models.Model):
	district = models.ForeignKey('District')
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	category = models.CharField(max_length=1)
	school_improvement_percent = models.DecimalField(max_digits=6, decimal_places=5, null=True)
	short_suspensions = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")
	long_suspensions = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")
	expulsions = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")
	crime = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")

	class Meta(object):
		verbose_name = "Discipline Rates"
		verbose_name_plural = "Discipline Rates"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s) - %s' %(self.district.lea_name, self.school_year, self.category)


class Demographics(models.Model):
	district = models.ForeignKey('District')
	school_year = models.CharField(max_length=10, verbose_name="School Year")

	class Meta(object):
		verbose_name_plural = "Demographics"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s) - %s' %(self.district.lea_name, self.school_year, self.category)

