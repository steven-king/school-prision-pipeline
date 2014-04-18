from django.forms import widgets
from rest_framework import serializers

from county_info.models import District, Graduation, DisciplineRate, Demographics, Attendance, GradeLevel, SpecialCourses, FreeLunch, State, StateDemographics, StateGraduation, StateAttendance, StateGradeLevel, StateSpecialCourses, StateDiscipline


class GraduationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Graduation
		fields = ('district', 'school_year', 'graduation_rate', 'native_american_graduation_rate', 'asian_graduation_rate', 'black_graduation_rate', 'hispanic_graduation_rate', 'multiracial_graduation_rate', 'white_graduation_rate', 
			'freelunch_graduation_rate')