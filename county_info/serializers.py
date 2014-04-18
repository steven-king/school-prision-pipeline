from django.forms import widgets
from rest_framework import serializers

from county_info.models import District, Graduation, DisciplineRate, Demographics, Attendance, GradeLevel, SpecialCourses, FreeLunch, State, StateDemographics, StateGraduation, StateAttendance, StateGradeLevel, StateSpecialCourses, StateDiscipline


class GraduationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Graduation
		fields = ('district', 'school_year', 'graduation_rate')


class SatScoreSerializer(serializers.ModelSerializer):

	class Meta:
		model = Demographics
		fields = ('district', 'school_year', 'sat_average_score')