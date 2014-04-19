from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from county_info.models import District, Graduation, DisciplineRate, Demographics, Attendance, GradeLevel, SpecialCourses, FreeLunch, State, StateDemographics, StateGraduation, StateAttendance, StateGradeLevel, StateSpecialCourses, StateDiscipline
from county_info.serializers import GraduationSerializer, SatScoreSerializer, FreeLunchSerializer, DisciplineRateSerializer, ExpensesSerializer, DistrictSerializer


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
#	northcarolina = State.objects.get(state_name="North Carolina")
	context = {
#		'northcarolina': northcarolina,
#		'districts': District.objects.all(),
	}
	# ipdb.set_trace()

	# district_input = "Orange County Schools"
	# school_year_input = "2012-2013"
	# district = District.objects.get(lea_name=district_input)
	# graduation_rates = district.graduation_rates.get(school_year=school_year_input)
	# black_graduation_rate = graduation_rates.black_graduation_rate
	
	return render(request, "county_info/home.html", context)


def mobile(request):
	context = {
	}
	return render(request, "county_info/mobile.html", context)


# API Views
@csrf_exempt
def graduation_rates(request):
	if request.method == 'GET':
		graduation_rates = Graduation.objects.filter(school_year='2012-2013')
		serializer = GraduationSerializer(graduation_rates, many=True)
		return JSONResponse(serializer.data)

@csrf_exempt
def sat_scores(request):
	if request.method == 'GET':
		sat_scores = Demographics.objects.filter(school_year='2012-2013')
		serializer = SatScoreSerializer(sat_scores, many=True)
		return JSONResponse(serializer.data)

@csrf_exempt
def freelunch_rates(request):
	if request.method == 'GET':
		freelunch_rates = FreeLunch.objects.filter(school_year='2012-2013')
		serializer = FreeLunchSerializer(freelunch_rates, many=True)
		return JSONResponse(serializer.data)

@csrf_exempt
def discipline_rates(request):
	if request.method == 'GET':
		discipline_rates = DisciplineRate.objects.filter(school_year='2012-2013')
		for discipline_rate in discipline_rates:
			discipline_rate.calculate_composite_rate()
		serializer = DisciplineRateSerializer(discipline_rates, many=True)
		return JSONResponse(serializer.data)

@csrf_exempt
def expenses(request):
	if request.method == 'GET':
		sat_scores = Demographics.objects.filter(school_year='2012-2013')
		serializer = ExpensesSerializer(sat_scores, many=True)
		return JSONResponse(serializer.data)

@csrf_exempt
def district_detail(request, pk):
    """
    Retrieve, update or delete a code district.
    """
    try:
        district = District.objects.get(pk=pk)
    except District.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DistrictSerializer(district)
        return JSONResponse(serializer.data)





