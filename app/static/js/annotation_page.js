$('#mark-button').click(function() {
    $('#mark-button').toggleClass("selected-button");
    if ($('#mark-button').hasClass("selected-button")) {
        $('#tag-button').removeClass("selected-button");
    }
});


$('#tag-button').click(function() {
    $('#tag-button').toggleClass("selected-button");
    if ($('#tag-button').hasClass("selected-button")) {

        $('#mark-button').removeClass("selected-button");

    }
});

$.fn.toggleText = function(t1, t2) {
    if (this.text() == t1) this.text(t2);
    else this.text(t1);
    return this;
};

$('#tags').click(function() {
    $('#sug').slideToggle();
    $('#tags span').toggleText("Tags +", "Tags -");
});

$('#sensor-data').click(function() {
    $('#sensor-data-item').slideToggle();
    $('#sensor-data span').toggleText("Sensor Data +", "Sensor Data -");
});