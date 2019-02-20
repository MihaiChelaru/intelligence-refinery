$( document ).ready(function() {
    // Add affix top to element when scrolling up, otherwise remove it.
    $(window).on('scroll', function (event) {
        var scrollValue = $(window).scrollTop();
        if (scrollValue > 70) {
            $('.toc').addClass('affix');
        } else{
            $('.toc').removeClass('affix');
        }
    });
});