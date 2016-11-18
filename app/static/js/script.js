let cancel = document.querySelector('.cancel');
let info = document.querySelector('#infoWrap');
let results = document.querySelector('#results');
let filter = document.querySelector('.filter');
let select = document.querySelector('.select');

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

// $.fn.toggleOpacity = function(t1, t2) {
//     if (this.css() == t1) this.css(t2);
//     else this.css(t1);
//     return this;
// };

select.addEventListener('click', function(){
		// $('#rad1').fadeToggle();
  let numberofChecked = $('input:checkbox:checked').length;
      if ($('.lazy').css('opacity') == '1'){
        $('.lazy').animate({'opacity':0.5});
        $('.rad1').css('display', 'block');
        $('#selector').html("Save Images (" + numberofChecked + ")");


    } else{
        $('.lazy').animate({'opacity':1})
        $('.rad1').css('display', 'none');
        $('#selector').html("Select Images");
    }
  
});

$('#nav1').click(function() {
    $('#nav1').toggleClass("selected-button");
    if ($('#nav1').hasClass("selected-button")) {
        console.log("yo");
        $('#nav2').removeClass("selected-button");
    }
});


$('#nav2').click(function() {
    $('#nav2').toggleClass("selected-button");
    if ($('#nav2').hasClass("selected-button")) {

        $('#nav1').removeClass("selected-button");
    }
});




