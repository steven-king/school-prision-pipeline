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


