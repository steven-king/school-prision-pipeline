from county_info.models import District, Graduation, DisciplineRate, Demographics, Attendance, GradeLevel, SpecialCourses, FreeLunch, State, StateDemographics, StateGraduation, StateAttendance, StateGradeLevel, StateSpecialCourses, StateDiscipline
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
	context = {
		'districts': District.objects.all()
	}
	return render(request, "county_info/home.html", context)

def mobile(request):
	context = {
		'districts': District.objects.all()
	}
	return render(request, "county_info/mobile.html", context)