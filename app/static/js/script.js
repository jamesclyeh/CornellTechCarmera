let save = document.querySelector('.save');
let cancel = document.querySelector('.cancel');
let info = document.querySelector('#infoWrap');
let results = document.querySelector('#results');
let filter = document.querySelector('.filter');

save.addEventListener('click', function(){
	
	console.log("clicked");
	info.style.display = "none";
	results.style.display = "block";

});

cancel.addEventListener('click', function(){

	console.log("clicked");
	info.style.display = "none";
	results.style.display = "block";
});

filter.addEventListener('click', function(){

	console.log("clicked");
	info.style.display = "block";
	results.style.display = "none";
});