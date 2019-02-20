$(window).on('scroll', function (event) {
    var scrollValue = $(window).scrollTop();
    if (scrollValue > 120) {
        $('#scrollSpy').addClass('affix');
    } else{
        $('#scrollSpy').removeClass('affix');
    }
});