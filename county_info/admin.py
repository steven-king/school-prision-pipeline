from django.contrib import admin
from county_info.models import District, Graduation, DisciplineRate, Demographics, Attendance, GradeLevel, SpecialCourses, FreeLunch, State, StateDemographics, StateGraduation, StateAttendance, StateGradeLevel, StateSpecialCourses, StateDiscipline

# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
	list_display = ('lea_name', 'lea_code', 'lea_city', 'lea_state', 'lea_superintendent', 'lea_email', 'lea_website')
	search_fields = ('lea_name', 'lea_city')

admin.site.register(District, DistrictAdmin)


class GraduationAdmin(admin.ModelAdmin):
	list_display = ('district', 'school_year', 'graduation_rate', 'female_graduation_rate', 'male_graduation_rate', 'freelunch_graduation_rate', 'black_graduation_rate', 'hispanic_graduation_rate')
	search_fields = ('district__lea_name', 'school_year')

admin.site.register(Graduation, GraduationAdmin)


class DisciplineRateAdmin(admin.ModelAdmin):
	list_display = ('district', 'school_year', 'category', 'short_suspensions', 'long_suspensions', 'expulsions', 'crime')
	search_fields = ('district__lea_name', 'school_year')

admin.site.register(DisciplineRate, DisciplineRateAdmin)


class DemographicsAdmin(admin.ModelAdmin):
	list_display = ('district', 'school_year', 'sat_average_score', 'percent_native_american', 'percent_asian', 'percent_black', 'percent_hispanic', 'percent_white', 'percent_multiracial')
	search_fields = ('district__lea_name', 'school_year')

admin.site.register(Demographics, DemographicsAdmin)


class AttendanceAdmin(admin.ModelAdmin):
	list_display = ('district', 'school_year', 'total_attendance_rate', 'freelunch_attendance_rate', 'black_attendance_rate', 'hispanic_attendance_rate')
	search_fields = ('district__lea_name', 'school_year')

admin.site.register(Attendance, AttendanceAdmin)


class GradeLevelAdmin(admin.ModelAdmin):
	list_display = ('district', 'school_year', 'percent_on_grade_level', 'percent_freelunch_on_grade_level', 'percent_black_on_grade_level', 'percent_hispanic_on_grade_level')
	search_fields = ('district__lea_name', 'school_year')

admin.site.register(GradeLevel, GradeLevelAdmin)


class SpecialCoursesAdmin(admin.ModelAdmin):
	list_display = ('district', 'school_year', 'advanced_course_enrollment', 'vocational_course_enrollment')
	search_fields = ('district__lea_name', 'school_year')

admin.site.register(SpecialCourses, SpecialCoursesAdmin)


class FreeLunchAdmin(admin.ModelAdmin):
	list_display = ('district', 'school_year', 'adm', 'percent_needy')
	search_fields = ('district__lea_name', 'school_year')

admin.site.register(FreeLunch, FreeLunchAdmin)


class StateAdmin(admin.ModelAdmin):
	list_display = ('state_name', 'state_abbreviation')
	search_fields = ('state_name', 'state_abbreviation')

admin.site.register(State, StateAdmin)


class StateDemographicsAdmin(admin.ModelAdmin):
	list_display = ('state', 'school_year', 'percent_needy', 'sat_average_score', 'percent_native_american', 'percent_asian', 'percent_black', 'percent_hispanic', 'percent_white', 'percent_multiracial')
	search_fields = ('state__state_name', 'state__state_abbreviation', 'school_year')

admin.site.register(StateDemographics, StateDemographicsAdmin)


class StateGraduationAdmin(admin.ModelAdmin):
	list_display = ('state', 'school_year', 'graduation_rate', 'freelunch_graduation_rate', 'black_graduation_rate', 'hispanic_graduation_rate', 'white_graduation_rate')
	search_fields = ('state__state_name', 'state__state_abbreviation', 'school_year')

admin.site.register(StateGraduation, StateGraduationAdmin)


class StateAttendanceAdmin(admin.ModelAdmin):
	list_display = ('state', 'school_year', 'total_attendance_rate', 'freelunch_attendance_rate', 'black_attendance_rate', 'hispanic_attendance_rate')
	search_fields = ('state__state_name', 'state__state_abbreviation', 'school_year')

admin.site.register(StateAttendance, StateAttendanceAdmin)


class StateGradeLevelAdmin(admin.ModelAdmin):
	list_display = ('state', 'school_year', 'percent_on_grade_level', 'percent_freelunch_on_grade_level', 'percent_black_on_grade_level', 'percent_hispanic_on_grade_level')
	search_fields = ('state__state_name', 'state__state_abbreviation', 'school_year')

admin.site.register(StateGradeLevel, StateGradeLevelAdmin)


class StateSpecialCoursesAdmin(admin.ModelAdmin):
	list_display = ('state', 'school_year', 'advanced_course_enrollment', 'vocational_course_enrollment')
	search_fields = ('state__state_name', 'state__state_abbreviation', 'school_year')

admin.site.register(StateSpecialCourses, StateSpecialCoursesAdmin)


class StateDisciplineAdmin(admin.ModelAdmin):
	list_display = ('state', 'school_year', 'category', 'short_suspensions', 'long_suspensions', 'expulsions', 'crime')
	search_fields = ('state__state_name', 'state__state_abbreviation', 'school_year')

admin.site.register(StateDiscipline, StateDisciplineAdmin)