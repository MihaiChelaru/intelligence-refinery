$( document ).ready(function() {
    // Add affix top to element when scrolling up, otherwise remove it.
    $(window).on('scroll', function (event) {
        var scrollValue = $(window).scrollTop();
        if (scrollValue > 70) {
            $('#scrollSpy').addClass('affix');
        } else{
            $('#scrollSpy').removeClass('affix');
        }
    });
});