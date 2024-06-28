// Zoom-in/Zoom-out animation
function zoomIn() {
	document.getElementById("zoom").style.transform = "scale(1.2)";
	document.getElementById("zoom").style.transition = "transform 0.5s";
}

function zoomOut() {
	document.getElementById("zoom").style.transform = "scale(1)";
	document.getElementById("zoom").style.transition = "transform 0.5s";
}
window.onload = function() {
    var header = document.querySelector('.artist-header');
    header.classList.add('explode');
  }
  
// Reviews/Rating mechanism
function submitReview() {
	// Get user input
	var name = document.getElementById("name").value;
	var rating = document.querySelector('input[name="rating"]:checked').value;
	var review = document.getElementById("review").value;

	// Create a new row in the table
	var table = document.getElementById("review-table");
	var row = table.insertRow(-1);
	var nameCell = row.insertCell(0);
	var ratingCell = row.insertCell(1);
	var reviewCell = row.insertCell(2);

	// Add user input to the new row
	nameCell.innerHTML = name;
	ratingCell.innerHTML = rating;
	reviewCell.innerHTML = review;

	// Clear user input
	document.getElementById("name").value = "";
	document.querySelector('input[name="rating"]:checked').checked = false;
	document.getElementById("review").value = "";
}

// Countdown timer
var releaseDate = new Date("June 30, 2023 00:00:00").getTime();

var x = setInterval(function() {

	var now = new Date().getTime();

	var distance = releaseDate - now;

	var days = Math.floor(distance / (1000 * 60 * 60 * 24));
	var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
	var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
	var seconds = Math.floor((distance % (1000 * 60)) / 1000);

	document.getElementById("countdown").innerHTML = days + "d " + hours + "h "
	+ minutes + "m " + seconds + "s ";

	if (distance < 0) {
		clearInterval(x);
		document.getElementById("countdown").innerHTML = "EXPIRED";
	}
}, 1000);
