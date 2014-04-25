function disciplineMap () {
	$("#map-description").html("Short-/long-term suspensions and expulsions per 1000 students");
	$("#key-1").html("less than 20");
	$("#key-2").html("21-40");
	$("#key-3").html("41-100");
	$("#key-4").html("101-200");
	$("#key-5").html("200 or more");

	var data = getDiscipline();

	var currDistrictID = data[0].district;
	var total = 0;

	for (var i=0; i < data.length; i++) {
		if (currDistrictID == data[i].district) {
			if ((data[i].category == "H") || (data[i].category == "M") || (data[i].category == "E")) {
				total = total + data[i].composite_rate;
			}
		}
		else {
			var currDistrict= "#" + currDistrictID;
			var districtName = $(currDistrict).attr('class');
			$(currDistrict).attr("title", districtName+': '+total);

			if (total <=20 ) {
				$(currDistrict).attr('style', orange1);
			}
			else if (total <=40 ) {
				$(currDistrict).attr('style', orange2);
			}
			else if (total <100 ) {
				$(currDistrict).attr('style', orange3);
			}
			else if (total <=200 ) {
				$(currDistrict).attr('style', orange4);
			}
			else if (total <=400 ) {
				$(currDistrict).attr('style', orange5);
			}

			currDistrictID = data[i].district;
			total = data[i].composite_rate;
		}
	}
	var currDistrict= "#" + currDistrictID;
	var districtName = $(currDistrict).attr('class');
	$(currDistrict).attr("title", districtName+': '+total);

	if (total <=20 ) {
		$(currDistrict).attr('style', orange1);
	}
	else if (total <=40 ) {
		$(currDistrict).attr('style', orange2);
	}
	else if (total <60 ) {
		$(currDistrict).attr('style', orange3);
	}
	else if (total <=100 ) {
		$(currDistrict).attr('style', orange4);
	}
	else if (total <=250 ) {
		$(currDistrict).attr('style', orange5);
	}
}

function lunchMap () {
	$("#map-description").html("Percent who qualify for free or reduced lunch");
	$("#key-1").html("0-20%");
	$("#key-2").html("21-40%");
	$("#key-3").html("41-60%");
	$("#key-4").html("61-80%");
	$("#key-5").html("over 80%");

	var data = getFreeLunch();
	for (var i=0; i < data.length; i++) {
		var currDistrict= "#" + data[i].fields.district;
		var currLunch = data[i].fields.percent_needy;

		//tooltip
		var readable = Math.round(currLunch*100);
		readable = readable + "%";
		var districtName = $(currDistrict).attr('class');
		$(currDistrict).attr("title", districtName+ ": "+readable);

		//fill shapes
		if (currLunch <=0.2 ) {
			$(currDistrict).attr('style', orange1);
		}
		else if (currLunch <=0.4 ) {
			$(currDistrict).attr('style', orange2);
		}
		else if (currLunch <=0.6 ) {
			$(currDistrict).attr('style', orange3);
		}
		else if (currLunch <=0.8 ) {
			$(currDistrict).attr('style', orange4);
		}
		else if (currLunch <=1 ) {
			$(currDistrict).attr('style', orange5);
		}

	}
}
//fill colors for map
var orange1 = "fill:#E4A482";
var orange2 = "fill:#DA835A";
var orange3 = "fill:#D16436";
var orange4 = "fill:#99472C";
var orange5 = "fill:#632D1D";

function graduationMap () {
	//set up map key
	$("#map-description").html("Percent who graduated from high school in 2013");
	$("#key-1").html("less than 75%");
	$("#key-2").html("76-80%");
	$("#key-3").html("81-85%");
	$("#key-4").html("86-90%");
	$("#key-5").html("over 90%");

	var data = getGraduation();

	for (var i=0; i < data.length; i++) {
		if (data[i].fields.school_year == "2012-2013") {
		
			var currDistrict= "#" + data[i].fields.district;
			var currGrad = data[i].fields.graduation_rate;

			//tooltip
			var readable = Math.round(currGrad*100);
			readable = readable + "%";
			var districtName = $(currDistrict).attr('class');
			$(currDistrict).attr("title", districtName + ':  ' + readable);

			//fill shapes
			if (currGrad <=0.75 ) {
				$(currDistrict).attr('style', orange1);
			}
			else if (currGrad <=0.8 ) {
				$(currDistrict).attr('style', orange2);
			}
			else if (currGrad <=0.85 ) {
				$(currDistrict).attr('style', orange3);
			}
			else if (currGrad <=0.9 ) {
				$(currDistrict).attr('style', orange4);
			}
			else if (currGrad <=1 ) {
				$(currDistrict).attr('style', orange5);
			}
		}
	}
}

function satMap () {
	$.ajax({
		url: "http://school-discipline.herokuapp.com/api/sat_scores",
		dataType: "json",
		success: function(data) {
			console.log(data);
			

			//set up map key
			$("#map-description").html("Average SAT scores from 2013 (out of 1600)");
			$("#key-1").html("700-800");
			$("#key-2").html("801-900");
			$("#key-3").html("901-1000");
			$("#key-4").html("1001-1100");
			$("#key-5").html("1101-1200");

			//var data = getSat();

			for (var i=0; i < data.length; i++) {
				if (data[i].school_year == "2012-2013") {
				
					var currDistrict= "#" + data[i].district;
					var currSat = data[i].sat_average_score;

					//tooltip
					var districtName = $(currDistrict).attr('class');
					$(currDistrict).attr("title", districtName + ':  ' + currSat);

					//fill shapes
					if (currSat <=800 ) {
						$(currDistrict).attr('style', orange1);
					}
					else if (currSat <=900 ) {
						$(currDistrict).attr('style', orange2);
					}
					else if (currSat <=1000 ) {
						$(currDistrict).attr('style', orange3);
					}
					else if (currSat <=1100 ) {
						$(currDistrict).attr('style', orange4);
					}
					else if (currSat <=1200 ) {
						$(currDistrict).attr('style', orange5);
					}
				}
			}
		}
	});
}

function expensesMap () {
	//set up map key
	$("#map-description").html("Spending per student in 2013");
	$("#key-1").html("$8,000 or less");
	$("#key-2").html("$8,001-9,000");
	$("#key-3").html("$9,001-10,000");
	$("#key-4").html("$10,001-11,001");
	$("#key-5").html("$11,001 or more");

	var data = getExpenses();

	for (var i=0; i < data.length; i++) {
		if (data[i].fields.school_year == "2012-2013") {
		
			var currDistrict= "#" + data[i].fields.district;
			var currExpenses = data[i].fields.expenses_per_pupil;

			//tooltip
			var readable = "$"+ currExpenses;
			var periods = readable.split(".");
			var length = periods[0].length-3;
			var first = periods[0].substr(0,length);
			var last = periods[0].substr(length, periods[0].length);
			var final = first + "," + last;
			var districtName = $(currDistrict).attr('class');
			$(currDistrict).attr("title", districtName + ': ' + final);

			//fill shapes
			if (currExpenses <=8000 ) {
				$(currDistrict).attr('style', orange1);
			}
			else if (currExpenses <=8500 ) {
				$(currDistrict).attr('style', orange2);
			}
			else if (currExpenses <=10000 ) {
				$(currDistrict).attr('style', orange3);
			}
			else if (currExpenses <=11500 ) {
				$(currDistrict).attr('style', orange4);
			}
			else {
				$(currDistrict).attr('style', orange5);
			}
			
		}
	}

}









