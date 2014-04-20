from django.forms import widgets
from rest_framework import serializers

from county_info.models import District, Graduation, DisciplineRate, Demographics, Attendance, GradeLevel, SpecialCourses, FreeLunch, State, StateDemographics, StateGraduation, StateAttendance, StateGradeLevel, StateSpecialCourses, StateDiscipline


class GraduationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Graduation
		fields = ('district', 'school_year', 'graduation_rate')

class GraduationDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Graduation
		fields = ('school_year', 'graduation_rate', 'freelunch_graduation_rate')

class SatScoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Demographics
		fields = ('district', 'school_year', 'sat_average_score')

class FreeLunchSerializer(serializers.ModelSerializer):
	class Meta:
		model = FreeLunch
		fields = ('district', 'school_year', 'percent_needy')

class FreeLunchDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = FreeLunch
		fields = ('school_year', 'percent_needy')

class DisciplineRateSerializer(serializers.ModelSerializer):
	class Meta:
		model = DisciplineRate
		fields = ('district', 'school_year', 'category', 'composite_rate')

class DisciplineRateDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = DisciplineRate
		fields = ('school_year', 'category', 'composite_rate')

class ExpensesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Demographics
		fields = ('district', 'school_year', 'expenses_per_pupil')

class DemographicsDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Demographics
		fields = ('school_year', 'expenses_per_pupil', 'sat_participation', 'sat_average_score', 'percent_native_american','percent_asian', 'percent_black', 'percent_hispanic', 'percent_white', 'percent_multiracial', 'percent_pacific_islander')

class DistrictSerializer(serializers.ModelSerializer):
	graduation_rates = GraduationDetailSerializer(many=True)
	demographics = DemographicsDetailSerializer(many=True)
	discipline_rates = DisciplineRateDetailSerializer(many=True)
	freelunch_rates = FreeLunchDetailSerializer(many=True)

	class Meta:
		model = District
		fields = ('lea_name', 'lea_code', 'graduation_rates', 'demographics', 'discipline_rates', 'freelunch_rates')



