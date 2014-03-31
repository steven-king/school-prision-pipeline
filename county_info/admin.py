from django.contrib import admin
from county_info.models import District, Graduation, DisciplineRate, Demographics, Attendance, GradeLevel, SpecialCourses

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


class AttendanceAdmin(admin.ModelAdmin):
	list_display = ('district', 'school_year', 'total_attendance_rate', 'freelunch_attendance_rate', 'black_attendance_rate', 'hispanic_attendance_rate')
	search_fields = ('district', 'school_year')

admin.site.register(Attendance, AttendanceAdmin)


class GradeLevelAdmin(admin.ModelAdmin):
	list_display = ('district', 'school_year', 'percent_on_grade_level', 'percent_freelunch_on_grade_level', 'percent_black_on_grade_level', 'percent_hispanic_on_grade_level')
	search_fields = ('district', 'school_year')

admin.site.register(GradeLevel, GradeLevelAdmin)


class SpecialCoursesAdmin(admin.ModelAdmin):
	list_display = ('district', 'school_year', 'advanced_course_enrollment', 'vocational_course_enrollment')
	search_fields = ('district', 'school_year')

admin.site.register(SpecialCourses, SpecialCoursesAdmin)