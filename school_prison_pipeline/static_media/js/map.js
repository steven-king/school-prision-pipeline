function lunchMap () {
	$("#map-description").html("Percentage who qualify for free or reduced lunch");
	$("#key-1").html("0-20%");
	$("#key-2").html("21-40%");
	$("#key-3").html("41-60%");
	$("#key-4").html("61-80%");
	$("#key-5").html("81-100%");

	var data = getFreeLunch();
	for (var i=0; i < data.length; i++) {
		var currDistrict= "#" + data[i].fields.district;
//		var currName = $("#currDistrict").attr("class");
		var currLunch = data[i].fields.percent_needy;

//		var readable = Math.round(currLunch*100);
//		readable = readable + "%";
//		$("#currDistrict").attr("title", currName+ ": "+readable);

		if (currLunch <=0.2 ) {
			$(currDistrict).attr('style', "fill:#FF7A42");
		}
		else if (currLunch <=0.4 ) {
			$(currDistrict).attr('style', "fill:#D16436");
		}
		else if (currLunch <=0.6 ) {
			$(currDistrict).attr('style', "fill:#B2552E");
		}
		else if (currLunch <=0.8 ) {
			$(currDistrict).attr('style', "fill:#914525");
		}
		else if (currLunch <=1 ) {
			$(currDistrict).attr('style', "fill:#612E19");
		}

	}
}
var yellow = "fill:#C19438";
var blue = "fill:#004E79";
var orange = "fill:#D16436";
var gray = "fill:#BDAA91";
var brown = "fill:#88765D";

function graduationMap () {
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

			if (currGrad <=0.75 ) {
				$(currDistrict).attr('style', gray);
			}
			else if (currGrad <=0.8 ) {
				$(currDistrict).attr('style', brown);
			}
			else if (currGrad <=0.85 ) {
				$(currDistrict).attr('style', blue);
			}
			else if (currGrad <=0.9 ) {
				$(currDistrict).attr('style', yellow);
			}
			else if (currGrad <=1 ) {
				$(currDistrict).attr('style', orange);
			}
		}
	}
}

function satMap () {
	$("#map-description").html("Average SAT scores from 2013 (out of 1600)");
	$("#key-1").html("700-800");
	$("#key-2").html("801-900");
	$("#key-3").html("901-1000");
	$("#key-4").html("1001-1100");
	$("#key-5").html("1101-1200");

	var data = getSat();

	for (var i=0; i < data.length; i++) {
		if (data[i].fields.school_year == "2012-2013") {
		
			var currDistrict= "#" + data[i].fields.district;
			var currSat = data[i].fields.sat_average_score;
			$(currDistrict).attr("title", currSat);

			if (currSat <=800 ) {
				$(currDistrict).attr('style', gray);
			}
			else if (currSat <=900 ) {
				$(currDistrict).attr('style', brown);
			}
			else if (currSat <=1000 ) {
				$(currDistrict).attr('style', blue);
			}
			else if (currSat <=1100 ) {
				$(currDistrict).attr('style', yellow);
			}
			else if (currSat <=1200 ) {
				$(currDistrict).attr('style', orange);
			}
		}
	}
}

function expensesMap () {
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

			if (currExpenses <=8000 ) {
				$(currDistrict).attr('style', gray);
			}
			else if (currExpenses <=8500 ) {
				$(currDistrict).attr('style', brown);
			}
			else if (currExpenses <=10000 ) {
				$(currDistrict).attr('style', blue);
			}
			else if (currExpenses <=11500 ) {
				$(currDistrict).attr('style', yellow);
			}
			else {
				$(currDistrict).attr('style', orange);
			}
			
		}
	}

}









