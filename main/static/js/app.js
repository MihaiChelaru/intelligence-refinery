// $( document ).ready(function() {
//     // Add affix top to element when scrolling up, otherwise remove it.
//     $(window).on('scroll', function (event) {
//         var scrollValue = $(window).scrollTop();
//         if (scrollValue > 70) {
//             $('#scrollSpy').addClass('affix');
//         } else{
//             $('#scrollSpy').removeClass('affix');
//         }
//     });
// });
//Executes your code when the DOM is ready.  Acts the same as $(document).ready().
$(function() {
  //Calls the tocify method on your HTML div.
  var toc = $("#toc").tocify().data("toc-tocify");
  toc.setOption("extendPage", "false");
});