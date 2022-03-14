//PRELOADER\\

$(window).on('load', function () {  //Makes sure the whole site is loaded
    $('#status').fadeOut();
    $('#preloader').delay(350).fadeOut('slow');
});

// ACTIVITIES OPTION TABS \\
$('#activities-options-tabs').responsiveTabs({
    animation: 'slide'
});