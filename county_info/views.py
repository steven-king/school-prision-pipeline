from county_info.models import District, Graduation, DisciplineRate, Demographics, Attendance, GradeLevel, SpecialCourses, FreeLunch, State, StateDemographics, StateGraduation, StateAttendance, StateGradeLevel, StateSpecialCourses, StateDiscipline
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
	context = {
		'northcarolina': State.objects.get(state_name="North Carolina"),
		'districts': District.objects.all(),
		'graduation_rates': Graduation.objects.all(),
		'discipline_rates': DisciplineRate.objects.all(),
		'demographics': Demographics.objects.all(),
		'attendance_rates': Attendance.objects.all(),
		'gradelevel_rates': GradeLevel.objects.all(),
		'specialcourse_rates': SpecialCourses.objects.all(),
		'freelunch_rates': FreeLunch.objects.all(),
		'stategraduation_rates': StateGraduation.objects.all(),
		'statediscipline_rates': StateDiscipline.objects.all(),
		'statedemographics': StateDemographics.objects.all(),
		'stateattendance_rates': StateAttendance.objects.all(),
		'stategradelevel_rates': StateGradeLevel.objects.all(),
		'statespecialcourse_rates': StateSpecialCourses.objects.all(),
	}
	return render(request, "county_info/home.html", context)

def mobile(request):
	context = {
		'northcarolina': State.objects.get(state_name="North Carolina"),
		'districts': District.objects.all(),
		'graduation_rates': Graduation.objects.all(),
		'discipline_rates': DisciplineRate.objects.all(),
		'demographics': Demographics.objects.all(),
		'attendance_rates': Attendance.objects.all(),
		'gradelevel_rates': GradeLevel.objects.all(),
		'specialcourse_rates': SpecialCourses.objects.all(),
		'freelunch_rates': FreeLunch.objects.all(),
		'stategraduation_rates': StateGraduation.objects.all(),
		'statediscipline_rates': StateDiscipline.objects.all(),
		'statedemographics': StateDemographics.objects.all(),
		'stateattendance_rates': StateAttendance.objects.all(),
		'stategradelevel_rates': StateGradeLevel.objects.all(),
		'statespecialcourse_rates': StateSpecialCourses.objects.all(),
	}
	return render(request, "county_info/mobile.html", context)