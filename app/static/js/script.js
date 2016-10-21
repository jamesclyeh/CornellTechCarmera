let save = document.querySelector('.save');
let cancel = document.querySelector('.cancel');

save.addEventListener('click', function(){
	let info = document.getElementByID('#informationWrapper');
	info.toggleSlide();
});