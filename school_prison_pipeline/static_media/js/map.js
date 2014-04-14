function lunchMap () {
	$("#map-description").html("Percentage of students receiving either free or reduced lunch");
	$("#key-1").html("0-20%");
	$("#key-2").html("21-40%");
	$("#key-3").html("41-60%");
	$("#key-4").html("61-80%");
	$("#key-5").html("81-100%");

	var data = getFreeLunch();
	console.log(data);
	for (var i=0; i < data.length; i++) {
		console.log(data[i].fields.district);
	}
}