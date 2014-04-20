from django.forms import widgets
from rest_framework import serializers

from county_info.models import District, Graduation, DisciplineRate, Demographics, Attendance, GradeLevel, SpecialCourses, FreeLunch, State, StateDemographics, StateGraduation, StateAttendance, StateGradeLevel, StateSpecialCourses, StateDiscipline, DisciplineDemographics


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

class DisciplineDemographicsSerializer(serializers.ModelSerializer):
	class Meta:
		model = DisciplineDemographics
		fields = ('total', 'white_male', 'white_female', 'black_male', 'black_female', 'hispanic_male', 'hispanic_female', 'multiracial_male', 'multiracial_female', 'asian_male', 'asian_female', 'pacific_islander_male', 'pacific_islander_female', 'other_male', 'other_female', 'other')

class DistrictSerializer(serializers.ModelSerializer):
	graduation_rates = GraduationDetailSerializer(many=True)
	demographics = DemographicsDetailSerializer(many=True)
	discipline_rates = DisciplineRateDetailSerializer(many=True)
	freelunch_rates = FreeLunchDetailSerializer(many=True)
	discipline_demographics = DisciplineDemographicsSerializer(many=True)

	class Meta:
		model = District
		fields = ('lea_name', 'lea_code', 'graduation_rates', 'demographics', 'discipline_rates', 'freelunch_rates', 'discipline_demographics')


class StateDemographicsSerializer(serializers.ModelSerializer):
	class Meta:
		model = StateDemographics
		fields = ('school_year', 'expenses_per_pupil', 'percent_needy', 'sat_participation', 'sat_average_score', 'percent_native_american','percent_asian', 'percent_black', 'percent_hispanic', 'percent_white', 'percent_multiracial', 'percent_pacific_islander')

class StateGraduationSerializer(serializers.ModelSerializer):
	class Meta:
		model = StateGraduation
		fields = ('school_year', 'graduation_rate', 'freelunch_graduation_rate')

class StateDisciplineSerializer(serializers.ModelSerializer):
	class Meta:
		model = StateDiscipline
		fields = ('school_year', 'category', 'composite_rate')

class StateSerializer(serializers.ModelSerializer):
	statedemographics = StateDemographicsSerializer(many=True)
	stategraduation_rates = StateGraduationSerializer(many=True)
	statediscipline_rates = StateDisciplineSerializer(many=True)

	class Meta:
		model = State
		fields = ('state_name', 'state_abbreviation', 'statedemographics', 'stategraduation_rates', 'statediscipline_rates')










