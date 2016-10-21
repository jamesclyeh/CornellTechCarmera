let save = document.querySelector('.save');
let cancel = document.querySelector('.cancel');
let info = document.querySelector('#informationWrapper');
let filter = document.querySelector('.filter');

save.addEventListener('click', function(){
	
	console.log("clicked");
	info.style.visibility = "hidden";
	filter.style.display = "block";

});

cancel.addEventListener('click', function(){

	console.log("clicked");
	info.style.visibility = "hidden";
	filter.style.display = "block";
});

filter.addEventListener('click', function(){

	console.log("clicked");
	info.style.visibility = "visible";
	filter.style.display = "none";
});