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
	district = models.ForeignKey('District', related_name="graduation_rates")
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	female_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	male_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	native_american_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	asian_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	black_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	hispanic_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	multiracial_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	white_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	freelunch_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	notfreelunch_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	
	class Meta(object):
		verbose_name = "Graduation Rates"
		verbose_name_plural = "Graduation Rates"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s)' %(self.district.lea_name, self.school_year)


class DisciplineRate(models.Model):
	district = models.ForeignKey('District', related_name="discipline_rates")
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	category = models.CharField(max_length=1)
	school_improvement_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	short_suspensions = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")
	long_suspensions = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")
	expulsions = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")
	crime = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")
	composite_rate = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")

	def calculate_composite_rate(self):
		if self.short_suspensions:
			discipline_sum = self.short_suspensions + self.long_suspensions + self.expulsions
			self.composite_rate = discipline_sum
			self.save()

	class Meta(object):
		verbose_name = "Discipline Rates"
		verbose_name_plural = "Discipline Rates"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s) - %s' %(self.district.lea_name, self.school_year, self.category)


class DisciplineDemographics(models.Model):
	district = models.ForeignKey('District', related_name="discipline_demographics")
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	total = models.IntegerField(max_length=6)
	american_indian_female = models.IntegerField(max_length=6, null=True)
	asian_female = models.IntegerField(max_length=6, null=True)
	hispanic_female = models.IntegerField(max_length=6, null=True)  
	black_female = models.IntegerField(max_length=6, null=True)
	white_female = models.IntegerField(max_length=6, null=True)
	multiracial_female = models.IntegerField(max_length=6, null=True)   
	american_indian_male = models.IntegerField(max_length=6, null=True)
	pacific_islander_male = models.IntegerField(max_length=6, null=True)
	pacific_islander_female = models.IntegerField(max_length=6, null=True) 
	asian_male = models.IntegerField(max_length=6, null=True) 
	hispanic_male = models.IntegerField(max_length=6, null=True)
	black_male = models.IntegerField(max_length=6, null=True)
	white_male = models.IntegerField(max_length=6, null=True)
	multiracial_male  = models.IntegerField(max_length=6, null=True)   
	other_male = models.IntegerField(max_length=6, null=True)
	other_female = models.IntegerField(max_length=6, null=True)
	other = models.IntegerField(max_length=6, null=True)

	class Meta(object):
		verbose_name = "Discipline Demographics"
		verbose_name_plural = "Discipline Demographics"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s) - %s' %(self.district.lea_name, self.school_year, self.category)


class Demographics(models.Model):
	district = models.ForeignKey('District', related_name="demographics")
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	sat_participation = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	sat_average_score = models.IntegerField(max_length=4, null=True)
	expenses_per_pupil = models.DecimalField(max_digits=8, decimal_places=2, null=True)
	percent_native_american = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_asian = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_black = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_hispanic = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_multiracial = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_white = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_pacific_islander = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_male = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_female = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	class Meta(object):
		verbose_name_plural = "Demographics"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s)' %(self.district.lea_name, self.school_year)


class Attendance(models.Model):
	district = models.ForeignKey('District', related_name="attendance_rates")
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	total_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	freelunch_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	notfreelunch_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	black_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	hispanic_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	class Meta(object):
		verbose_name = "Attendance Rate"
		verbose_name_plural = "Attendance Rates"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s)' %(self.district.lea_name, self.school_year)


class GradeLevel(models.Model):
	district = models.ForeignKey('District', related_name="gradelevel_rates")
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	percent_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_freelunch_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_notfreelunch_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_black_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_hispanic_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	class Meta(object):
		verbose_name = "Students At Grade Level"
		verbose_name_plural = "Students At Grade Level"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s)' %(self.district.lea_name, self.school_year)


class SpecialCourses(models.Model):
	district = models.ForeignKey('District', related_name="specialcourse_rates")
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	advanced_course_enrollment = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	vocational_course_enrollment = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	class Meta(object):
		verbose_name = "AP/IB & Vocational Enrollment"
		verbose_name_plural = "AP/IB & Vocational Enrollment"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s)' %(self.district.lea_name, self.school_year)


class FreeLunch(models.Model):
	district = models.ForeignKey('District', related_name="freelunch_rates")
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	adm = models.IntegerField(max_length=6, null=True, verbose_name="Average Daily Members")
	reduced_applications = models.IntegerField(max_length=6, null=True)
	free_applications = models.IntegerField(max_length=6, null=True)
	percent_needy = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	class Meta(object):
		verbose_name = "Free & Reduced Lunch Statistics"
		verbose_name_plural = "Free & Reduced Lunch Statistics"
		ordering = ('district__lea_name', '-school_year')

	def __unicode__(self):
		return U'%s (%s)' %(self.district.lea_name, self.school_year)


class State(models.Model):
	state_name = models.CharField(max_length=150, verbose_name="Name", primary_key=True)
	state_abbreviation = models.CharField(max_length=150, verbose_name="Abbreviation")

	class Meta(object):
		ordering = ('state_name',)

	def __unicode__(self):
		return U'%s (%s)' %(self.state_name, self.state_abbreviation)


class StateDemographics(models.Model):
	state = models.ForeignKey('State', related_name="statedemographics")
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	sat_participation = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	sat_average_score = models.IntegerField(max_length=4, null=True)
	expenses_per_pupil = models.DecimalField(max_digits=8, decimal_places=2, null=True)
	percent_native_american = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_asian = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_black = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_hispanic = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_multiracial = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_white = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_pacific_islander = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_male = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_female = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_needy = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	class Meta(object):
		verbose_name = "State Average Student Demographics"
		verbose_name_plural = "State Average Student Demographics"
		ordering = ('state__state_name', '-school_year')

	def __unicode__(self):
		return U'%s' %(self.state)


class StateGraduation(models.Model):
	state = models.ForeignKey('State', related_name="stategraduation_rates")
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	native_american_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	asian_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	black_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	hispanic_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	multiracial_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	white_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	freelunch_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	notfreelunch_graduation_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	
	class Meta(object):
		verbose_name = "State Average Graduation Rates"
		verbose_name_plural = "State Average Graduation Rates"
		ordering = ('state__state_name', '-school_year')

	def __unicode__(self):
		return U'%s' %(self.state)


class StateAttendance(models.Model):
	state = models.ForeignKey('State', related_name="stateattendance_rates")
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	total_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	freelunch_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	notfreelunch_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	black_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	hispanic_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	asian_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	native_american_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	multiracial_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	white_attendance_rate = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	class Meta(object):
		verbose_name = "State Average Attendance Rate"
		verbose_name_plural = "State Average Attendance Rates"
		ordering = ('state__state_name', '-school_year')

	def __unicode__(self):
		return U'%s' %(self.state)


class StateGradeLevel(models.Model):
	state = models.ForeignKey('State', related_name="stategradelevel_rates")
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	percent_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_freelunch_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_notfreelunch_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_black_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	percent_hispanic_on_grade_level = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	class Meta(object):
		verbose_name = "State Average Students At Grade Level"
		verbose_name_plural = "State Average Students At Grade Level"
		ordering = ('state__state_name', '-school_year')

	def __unicode__(self):
		return U'%s' %(self.state)


class StateSpecialCourses(models.Model):
	state = models.ForeignKey('State', related_name="statespecialcourse_rates")
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	advanced_course_enrollment = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	vocational_course_enrollment = models.DecimalField(max_digits=6, decimal_places=3, null=True)

	class Meta(object):
		verbose_name = "State Average AP/IB & Vocational Enrollment"
		verbose_name_plural = "State Average AP/IB & Vocational Enrollment"
		ordering = ('state__state_name', '-school_year')

	def __unicode__(self):
		return U'%s' %(self.state)


class StateDiscipline(models.Model):
	state = models.ForeignKey('State', related_name="statediscipline_rates")
	school_year = models.CharField(max_length=10, verbose_name="School Year")
	category = models.CharField(max_length=1)
	school_improvement_percent = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	short_suspensions = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")
	long_suspensions = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")
	expulsions = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")
	crime = models.IntegerField(max_length=4, null=True, help_text="Number Per 1000 Students")

	class Meta(object):
		verbose_name = "State Average Discipline Rates"
		verbose_name_plural = "State Average Discipline Rates"
		ordering = ('state__state_name', '-school_year')

	def __unicode__(self):
		return U'%s' %(self.state)


