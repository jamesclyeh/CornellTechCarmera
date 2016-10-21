let cancel = document.querySelector('.cancel');
let info = document.querySelector('#infoWrap');
let results = document.querySelector('#results');
let filter = document.querySelector('.filter');

cancel.addEventListener('click', function(){
	info.style.display = "none";
	results.style.display = "block";
  $('#imageWrap').show();
});

filter.addEventListener('click', function(){
	info.style.display = "block";
	results.style.display = "none";
  $('#imageWrap').hide();
});
