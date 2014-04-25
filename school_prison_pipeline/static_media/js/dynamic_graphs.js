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

function disciplineGraph () {
	var total = [0, 0, 0];

	for (var i=0; i<districtA.discipline_rates.length; i++) {
		if (districtA.discipline_rates[i].school_year == "2012-2013") {
			if ((districtA.discipline_rates[i].category == "H") || (districtA.discipline_rates[i].category == "M") || (districtA.discipline_rates[i].category == "E")) {
				total[0] = total[0] + districtA.discipline_rates[i].composite_rate;
			}
		}
	}
	for (var i=0; i<districtB.discipline_rates.length; i++) {
		if (districtB.discipline_rates[i].school_year == "2012-2013") {
			if ((districtB.discipline_rates[i].category == "H") || (districtB.discipline_rates[i].category == "M") || (districtB.discipline_rates[i].category == "E")) {
				total[1] = total[1] + districtB.discipline_rates[i].composite_rate;
			}
		}
	}
	for (var i=0; i<districtC.discipline_rates.length; i++) {
		if (districtC.discipline_rates[i].school_year == "2012-2013") {
			if ((districtC.discipline_rates[i].category == "H") || (districtC.discipline_rates[i].category == "M") || (districtC.discipline_rates[i].category == "E")) {
				total[2] = total[2] + districtC.discipline_rates[i].composite_rate;
			}
		}
	}
	var height =[];
	height[0] = total[0]*2;	
	height[1] = total[1]*2;
	height[2] = total[2]*2;
	console.log(total);

	if (height[0]>200 || height[1]>200 || height[2]>200) {
		height[0] = height[0]/2;
		height[1] = height[1]/2;
		height[2] = height[2]/2;
	}
	console.log(height);
	for (var i=0; i<3; i++){
		var top = 280-height[i];
		$("#discipline-"+i).css("height", height[i]);
		$("#discipline-"+i).css("margin-top", top);
		$("#discipline-p-"+i).html(total[i]);

		if (height[i] <= 40) {
			$("#discipline-p-"+i).css("top", "-30px");
			$("#discipline-p-"+i).css("color", "#000");
			$("#discipline-p-"+i).css("font-family", "latoregular");
		}
		else {
			$("#discipline-p-"+i).css("top", "10px");
			$("#discipline-p-"+i).css("color", "#fff");
			$("#discipline-p-"+i).css("font-family", "latolight");
		}
	}	
	
}

function graduationGraph (dataArray) {
	for (i=0; i < 3; i++) {
		var height = 250 * dataArray[i] - 30;
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
	$(".preloader-c").hide();
	$(".preloader").hide();
}



