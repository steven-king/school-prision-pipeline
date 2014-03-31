from django.contrib import admin
from county_info.models import District, Graduation, DisciplineRate, Demographics

# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
	list_display = ('lea_name', 'lea_code', 'lea_city', 'lea_state', 'lea_superintendent', 'lea_email', 'lea_website')
	search_fields = ('lea_name', 'lea_city')

admin.site.register(District, DistrictAdmin)

class GraduationAdmin(admin.ModelAdmin):
	list_display = ('district', 'school_year', 'graduation_rate', 'female_graduation_rate', 'male_graduation_rate', 'freelunch_graduation_rate', 'black_graduation_rate', 'hispanic_graduation_rate')
	search_fields = ('district', 'school_year')

admin.site.register(Graduation, GraduationAdmin)

class DisciplineRateAdmin(admin.ModelAdmin):
	list_display = ('district', 'school_year', 'category', 'short_suspensions', 'long_suspensions', 'expulsions', 'crime')
	search_fields = ('district', 'school_year')

admin.site.register(DisciplineRate, DisciplineRateAdmin)

class DemographicsAdmin(admin.ModelAdmin):
	list_display = ('district', 'school_year', 'sat_participation', 'sat_average_score', 'expenses_per_pupil')
	search_fields = ('district', 'school_year')

admin.site.register(Demographics, DemographicsAdmin)