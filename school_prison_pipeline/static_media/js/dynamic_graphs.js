function lunchGraph (dataArray) {
	for (i=0; i < 3; i++) {
		var height = 280 * dataArray[i];
		var top = 280 - height;
		$("#lunch-"+i).css("height", height);
		$("#lunch-"+i).css("margin-top", top);
		var readable = Math.round(dataArray[i]*100);
		readable = readable + "%";
		$("#lunch-p-"+i).html(readable);

		if (height <= 40) {
			$("#lunch-p-"+i).css("top", "-30px");
			$("#lunch-p-"+i).css("color", "#000");
			$("#lunch-p-"+i).css("font-family", "latoregular");
		}
		else {
			$("#lunch-p-"+i).css("top", "10px");
			$("#lunch-p-"+i).css("color", "#fff");
			$("#lunch-p-"+i).css("font-family", "latolight");
		}
	}
}

function expensesGraph (dataArray) {
	for (i=0; i < 3; i++) {
		var height = dataArray[i] - 5000;
		height = height * 0.035;
		var top = 280 - height;
		$("#expenses-"+i).css("height", height);
		$("#expenses-"+i).css("margin-top", top);

		var readable = "$"+ dataArray[i];
		var periods = readable.split(".");
		var length = periods[0].length-3;
		var first = periods[0].substr(0,length);
		var last = periods[0].substr(length, periods[0].length);
		var final = first + "," + last;
		$("#expenses-p-"+i).html(final);

		if (height <= 40) {
			$("#expenses-p-"+i).css("top", "-30px");
			$("#expenses-p-"+i).css("color", "#000");
			$("#expenses-p-"+i).css("font-family", "latoregular");
		}
		else {
			$("#expenses-p-"+i).css("top", "10px");
			$("#expenses-p-"+i).css("color", "#fff");
			$("#expenses-p-"+i).css("font-family", "latolight");
		}
	}
}

function disciplineGraph (dataArray) {
}

function graduationGraph (dataArray) {
	for (i=0; i < 3; i++) {
		var height = 250 * dataArray[i];
		var top = 280 - height;
		$("#graduation-"+i).css("height", height);
		$("#graduation-"+i).css("margin-top", top);
		var readable = Math.round(dataArray[i]*100);
		readable = readable + "%";
		$("#graduation-p-"+i).html(readable);

		if (height <= 40) {
			$("#graduation-p-"+i).css("top", "-30px");
			$("#graduation-p-"+i).css("color", "#000");
			$("#graduation-p-"+i).css("font-family", "latoregular");
		}
		else {
			$("#graduation-p-"+i).css("top", "10px");
			$("#graduation-p-"+i).css("color", "#fff");
			$("#graduation-p-"+i).css("font-family", "latolight");
		}
	}
}

function satGraph (dataArray) {
	for (i=0; i < 3; i++) {
		var height = dataArray[i] - 600;
		height = height * 0.46666;
		var top = 280 - height;
		$("#sat-"+i).css("height", height);
		$("#sat-"+i).css("margin-top", top);

		$("#sat-p-"+i).html(dataArray[i]);

		if (height <= 40) {
			$("#sat-p-"+i).css("top", "-30px");
			$("#sat-p-"+i).css("color", "#000");
			$("#sat-p-"+i).css("font-family", "latoregular");
		}
		else {
			$("#sat-p-"+i).css("top", "10px");
			$("#sat-p-"+i).css("color", "#fff");
			$("#sat-p-"+i).css("font-family", "latolight");
		}
	}
}

function demoDisciplineGraph (district) {
	console.log(district);
	console.log(district.american_indian_female);
	var total = district.total;
	$("#total-discipline").html(total + " incidents in 2011-2012");

	var incidents = {"Hispanic": 0, "White": 0, "Black": 0, 
		"Asian": 0, "American_Indian": 0, "Multi_racial": 0, };
	
	if (district.hispanic_female == 2.5) {
		incidents.Hispanic = incidents.Hispanic + 4;
	} else if (district.hispanic_female == undefined) {
	} else {incidents.Hispanic = incidents.Hispanic + district.hispanic_female;}
	if (district.hispanic_male == 2.5) {
		incidents.Hispanic = incidents.Hispanic + 4;
	} else if (district.hispanic_male == undefined) {
	} else {incidents.Hispanic = incidents.Hispanic + district.hispanic_male;}
	console.log(incidents.Hispanic);

	if (district.white_female == 2.5) {
		incidents.White = incidents.White + 4;
	} else if (district.white_female == undefined) {
	} else {incidents.White = incidents.White + district.white_female;}
	if (district.white_male == 2.5) {
		incidents.White = incidents.White + 4;
	} else if (district.white_male == undefined) {
	} else {incidents.White = incidents.White + district.white_male;}
	console.log(incidents.White);

	if (district.black_female == 2.5) {
		incidents.Black = incidents.Black + 4;
	} else if (district.black_female == undefined) {
	} else {incidents.Black = incidents.Black + district.black_female;}
	if (district.black_male == 2.5) {
		incidents.Black = incidents.Black + 4;
	} else if (district.black_male == undefined) {
	} else {incidents.Black = incidents.Black + district.black_male;}
	console.log(incidents.Black);

	if (district.asian_female == 2.5) {
		incidents.Asian = incidents.Asian + 4;
	} else if (district.asian_female == undefined) {
	} else {incidents.Asian = incidents.Asian + district.asian_female;}
	if (district.asian_male == 2.5) {
		incidents.Asian = incidents.Asian + 4;
	} else if (district.asian_male == undefined) {
	} else {incidents.Asian = incidents.Asian + district.asian_male;}
	console.log(incidents.Asian);

	if (district.american_indian_female == 2.5) {
		incidents.American_Indian = incidents.American_Indian + 4;
	} else if (district.american_indian_female == undefined) {
	} else {incidents.American_Indian = incidents.American_Indian + district.american_indian_female;}
	if (district.american_indian_male == 2.5) {
		incidents.American_Indian = incidents.American_Indian + 4;
	} else if (district.american_indian_male == undefined) {
	} else {incidents.American_Indian = incidents.American_Indian + district.american_indian_male;}
	console.log(incidents.American_Indian);
	
	if (district.multiracial_female == 2.5) {
		incidents.Multi_racial = incidents.Multi_racial + 4;
	} else if (district.multiracial_female == undefined) {
	} else {incidents.Multi_racial = incidents.Multi_racial + district.multiracial_female;}
	if (district.multiracial_male == 2.5) {
		incidents.Multi_racial = incidents.Multi-racial + 4;
	} else if (district.multiracial_male == undefined) {
	} else {incidents.Multi_racial = incidents.Multi_racial + district.multiracial_male;}
	console.log(incidents.Multi_racial);

	var sortable = [];
	for (var key in incidents) {
    	sortable.push([key, incidents[key]]);
    }
	sortable.sort(function(a, b) {return a[1] - b[1]});
	console.log(sortable[2][1]);

	for (var i=0; i<6; i++) {
		if (sortable[i][0] == "Black") {
			sortable[i][0] = "African American";
		}
		else if (sortable[i][0] == "Multi_racial") {
			sortable[i][0] = "Multi-racial";
		}
		else if (sortable[i][0] == "American_Indian") {
			sortable[i][0] = "American Indian";
		}
		$("#d-"+i).attr("title", sortable[i][1] + " - " + sortable[i][0]);

		var width = Math.round((sortable[i][1]/(total/1.5))*100);
		width = width +"%";
		console.log(width);
		$("#d-"+i).css("width", width);
	}

}

/*var orange = 
{
	"lea_name": "Orange County Schools",
	"lea_code": "680", 
	"graduation_rates": [
		{	"school_year": "2012-2013", 
			"graduation_rate": "0.825", 
			"freelunch_graduation_rate": "0.680"
		}, {
			"school_year": "2011-2012", 
			"graduation_rate": "0.854", 
			"freelunch_graduation_rate": "0.715"
		}, {
			"school_year": "2010-2011", 
			"graduation_rate": "0.828", 
			"freelunch_graduation_rate": "0.720"
		}, {
			"school_year": "2009-2010", 
			"graduation_rate": "0.831", 
			"freelunch_graduation_rate": "0.690"
		}, {
			"school_year": "2008-2009", 
			"graduation_rate": "0.814", 
			"freelunch_graduation_rate": "0.732"
		}, {
			"school_year": "2007-2008", 
			"graduation_rate": "0.763", 
			"freelunch_graduation_rate": "0.583"
		}], 
	"demographics": [
		{	"school_year": "2012-2013", 
			"expenses_per_pupil": "9745.94", 
			"sat_participation": "0.656", 
			"sat_average_score": 1038, 
			"percent_native_american": "0.004", 
			"percent_asian": "0.007", 
			"percent_black": "0.162", 
			"percent_hispanic": "0.157", 
			"percent_white": "0.637", 
			"percent_multiracial": null, 
			"percent_pacific_islander": "0.000"}, {"school_year": "2011-2012", "expenses_per_pupil": "9354.40", "sat_participation": "0.696", "sat_average_score": 1044, "percent_native_american": "0.004", "percent_asian": "0.007", "percent_black": "0.161", "percent_hispanic": "0.140", "percent_white": "0.657", "percent_multiracial": "0.027", "percent_pacific_islander": "0.001"}, {"school_year": "2010-2011", "expenses_per_pupil": "9477.49", "sat_participation": "0.740", "sat_average_score": 1043, "percent_native_american": "0.004", "percent_asian": "0.006", "percent_black": "0.170", "percent_hispanic": "0.125", "percent_white": "0.667", "percent_multiracial": "0.027", "percent_pacific_islander": "0.001"}, {"school_year": "2009-2010", "expenses_per_pupil": "9348.05", "sat_participation": "0.731", "sat_average_score": 1044, "percent_native_american": "0.003", "percent_asian": "0.009", "percent_black": "0.207", "percent_hispanic": "0.109", "percent_white": "0.671", "percent_multiracial": null, "percent_pacific_islander": null}, {"school_year": "2008-2009", "expenses_per_pupil": "9861.69", "sat_participation": "0.639", "sat_average_score": 1039, "percent_native_american": "0.003", "percent_asian": "0.010", "percent_black": "0.210", "percent_hispanic": "0.092", "percent_white": "0.684", "percent_multiracial": null, "percent_pacific_islander": null}, {"school_year": "2007-2008", "expenses_per_pupil": "9796.00", "sat_participation": "0.775", "sat_average_score": 1043, "percent_native_american": "0.003", "percent_asian": "0.009", "percent_black": "0.215", "percent_hispanic": "0.081", "percent_white": "0.692", "percent_multiracial": null, "percent_pacific_islander": null}], "discipline_rates": [{"school_year": "2012-2013", "category": "H", "composite_rate": 9}, {"school_year": "2012-2013", "category": "E", "composite_rate": 2}, {"school_year": "2012-2013", "category": "T", "composite_rate": 145}, {"school_year": "2012-2013", "category": "M", "composite_rate": 15}, {"school_year": "2011-2012", "category": "T", "composite_rate": null}, {"school_year": "2011-2012", "category": "E", "composite_rate": null}, {"school_year": "2011-2012", "category": "H", "composite_rate": null}, {"school_year": "2011-2012", "category": "M", "composite_rate": null}, {"school_year": "2010-2011", "category": "T", "composite_rate": null}, {"school_year": "2010-2011", "category": "E", "composite_rate": null}, {"school_year": "2010-2011", "category": "H", "composite_rate": null}, {"school_year": "2010-2011", "category": "M", "composite_rate": null}, {"school_year": "2009-2010", "category": "T", "composite_rate": null}, {"school_year": "2009-2010", "category": "E", "composite_rate": null}, {"school_year": "2009-2010", "category": "H", "composite_rate": null}, {"school_year": "2009-2010", "category": "M", "composite_rate": null}, {"school_year": "2008-2009", "category": "M", "composite_rate": null}, {"school_year": "2008-2009", "category": "E", "composite_rate": null}, {"school_year": "2008-2009", "category": "H", "composite_rate": null}, {"school_year": "2008-2009", "category": "T", "composite_rate": null}, {"school_year": "2007-2008", "category": "M", "composite_rate": null}, {"school_year": "2007-2008", "category": "E", "composite_rate": null}, {"school_year": "2007-2008", "category": "H", "composite_rate": null}, {"school_year": "2007-2008", "category": "T", "composite_rate": null}], "freelunch_rates": [{"school_year": "2012-2013", "percent_needy": "0.419"}, {"school_year": "2011-2012", "percent_needy": "0.416"}, {"school_year": "2010-2011", "percent_needy": "0.398"}, {"school_year": "2009-2010", "percent_needy": "0.390"}], "discipline_demographics": [{"total": 499, "white_male": 215, "white_female": 51, "black_male": 134, "black_female": 38, "hispanic_male": 35, "hispanic_female": 11, "multiracial_male": 5, "multiracial_female": 7, "asian_male": 2, "asian_female": null, "pacific_islander_male": null, "pacific_islander_female": null, "other_male": null, "other_female": null, "american_indian_male": 2, "american_indian_female": null, "other": null}]}
*/

