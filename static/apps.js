var main = function() {

  $("#horse").delay(200).queue(function(next) {
  $(this).addClass("horseEnter");
  next();
});

  $("#yourMove").delay(1200).queue(function(next) {
  $(this).addClass("moveEnter");
  next();
});

  $("#yourMove").delay(2000).queue(function(next) {
  $(this).removeClass("moveEnter");
  next();
});

  $(window).scroll(function() {
    $('#spinHorse').each(function(){
    var imagePos = $(this).offset().top;

    var topOfWindow = $(window).scrollTop();
      if (imagePos < topOfWindow+600) {
        $(this).addClass("spin");
      }
    });
  });

  $(window).scroll(function() {
    $('#checkmark').each(function(){
    var imagePos = $(this).offset().top;

    var topOfWindow = $(window).scrollTop();
      if (imagePos < topOfWindow+800) {
        $(this).addClass("fadeIn");
      }
    });
  });

    $(window).scroll(function() {
    $('#cloud').each(function(){
    var imagePos = $(this).offset().top;

    var topOfWindow = $(window).scrollTop();
      if (imagePos < topOfWindow+800) {
        $(this).addClass("rubberBand");
      }
    });
  });

    $(window).scroll(function() {
    $('#team').each(function(){
    var imagePos = $(this).offset().top;

    var topOfWindow = $(window).scrollTop();
      if (imagePos < topOfWindow+800) {
        $(this).addClass("flash");
      }
    });
  });

    $(window).scroll(function() {
    $('#hexButton').each(function(){
    var imagePos = $(this).offset().top;

    var topOfWindow = $(window).scrollTop();
      if (imagePos < topOfWindow+800) {
        $(this).addClass("pulse");
      }
    });
  });

    $(window).scroll(function() {
    $('#browsers').each(function(){
    var imagePos = $(this).offset().top;

    var topOfWindow = $(window).scrollTop();
      if (imagePos < topOfWindow+800) {
        $(this).addClass("swing");
      }
    });
  });

    $(window).scroll(function() {
    $('#social').each(function(){
    var imagePos = $(this).offset().top;

    var topOfWindow = $(window).scrollTop();
      if (imagePos < topOfWindow+800) {
        $(this).addClass("tada");
      }
    });
  });

}

$(document).ready(main);