from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from county_info.models import District, Graduation, DisciplineRate, Demographics, Attendance, GradeLevel, SpecialCourses, FreeLunch, State, StateDemographics, StateGraduation, StateAttendance, StateGradeLevel, StateSpecialCourses, StateDiscipline
from county_info.serializers import GraduationSerializer, SatScoreSerializer, FreeLunchSerializer, DisciplineRateSerializer, ExpensesSerializer, DistrictSerializer, StateSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# Create your views here.
def home(request):
	context = {
	}
	
	return render(request, "county_info/home.html", context)


def mobile(request):
	context = {
	}
	return render(request, "county_info/mobile.html", context)

def mobile_detail(request, pk):
	district = District.objects.get(pk=pk)
	demographics = district.demographics.get(school_year='2012-2013')
	freelunch = district.freelunch_rates.get(school_year='2012-2013')
	graduation = district.graduation_rates.get(school_year='2012-2013')
	discipline_e = district.discipline_rates.get(school_year='2012-2013', category='E')
	discipline_e.calculate_composite_rate()
	discipline_m = district.discipline_rates.get(school_year='2012-2013', category='M')
	discipline_m.calculate_composite_rate()
	discipline_h = district.discipline_rates.get(school_year='2012-2013', category='H')
	discipline_h.calculate_composite_rate()
	discipline = discipline_e.composite_rate + discipline_m.composite_rate + discipline_h.composite_rate
	discipline_demographics = district.discipline_demographics.get(district=district)
	context = {
		'district': district,
		'demographics': demographics,
		'freelunch_rates': freelunch,
		'graduation_rates': graduation,
		'discipline_rates': discipline,
		'discipline_demographics': discipline_demographics,
	}
	return render(request, "county_info/mobile_detail.html", context)


# API Views
def graduation_rates(request):
	if request.method == 'GET':
		graduation_rates = Graduation.objects.filter(school_year='2012-2013')
		serializer = GraduationSerializer(graduation_rates, many=True)
		return JSONResponse(serializer.data)

def sat_scores(request):
	if request.method == 'GET':
		sat_scores = Demographics.objects.filter(school_year='2012-2013')
		serializer = SatScoreSerializer(sat_scores, many=True)
		return JSONResponse(serializer.data)

def freelunch_rates(request):
	if request.method == 'GET':
		freelunch_rates = FreeLunch.objects.filter(school_year='2012-2013')
		serializer = FreeLunchSerializer(freelunch_rates, many=True)
		return JSONResponse(serializer.data)

def discipline_rates(request):
	if request.method == 'GET':
		discipline_rates = DisciplineRate.objects.filter(school_year='2012-2013')
		for discipline_rate in discipline_rates:
			discipline_rate.calculate_composite_rate()
		serializer = DisciplineRateSerializer(discipline_rates, many=True)
		return JSONResponse(serializer.data)

def expenses(request):
	if request.method == 'GET':
		sat_scores = Demographics.objects.filter(school_year='2012-2013')
		serializer = ExpensesSerializer(sat_scores, many=True)
		return JSONResponse(serializer.data)

def district_detail(request, pk):
    """
    Retrieve, update or delete a code district.
    """
    try:
        district = District.objects.get(pk=pk)
    except District.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
    	discipline_rates = DisciplineRate.objects.filter(school_year='2012-2013')
    	for discipline_rate in discipline_rates:
			discipline_rate.calculate_composite_rate()
        serializer = DistrictSerializer(district)
        return JSONResponse(serializer.data)

def state_detail(request, pk):
    """
    Retrieve, update or delete a code district.
    """
    try:
        state = State.objects.get(pk=pk)
    except State.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
    	discipline_rates = StateDiscipline.objects.all()
    	for discipline_rate in discipline_rates:
			discipline_rate.calculate_composite_rate()
        serializer = StateSerializer(state)
        return JSONResponse(serializer.data)





