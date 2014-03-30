from django.contrib import admin
from county_info.models import District, Graduation

# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
	search_fields = ('lea_name', 'lea_city')

admin.site.register(District, DistrictAdmin)

class GraduationAdmin(admin.ModelAdmin):
	search_fields = ('code',)

admin.site.register(Graduation, GraduationAdmin)
