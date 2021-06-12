/*
	Dopetrope by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

$.fn.commentCards = function(){

	return this.each(function(){
  
	  var $this = $(this),
		  $cards = $this.find('.card'),
		  $current = $cards.filter('.card--current'),
		  $next;
  
	  $cards.on('click',function(){
		if ( !$current.is(this) ) {
		  $cards.removeClass('card--current card--out card--next');
		  $current.addClass('card--out');
		  $current = $(this).addClass('card--current');
		  $next = $current.next();
		  $next = $next.length ? $next : $cards.first();
		  $next.addClass('card--next');
		}
	  });
  
	  if ( !$current.length ) {
		$current = $cards.last();
		$cards.first().trigger('click');
	  }
  
	  $this.addClass('cards--active');
  
	})
  
  };
  
  $('.cards').commentCards();

(function($) {

	var	$window = $(window),
		$body = $('body');

	// Breakpoints.
		breakpoints({
			xlarge:  [ '1281px',  '1680px' ],
			large:   [ '981px',   '1280px' ],
			medium:  [ '737px',   '980px'  ],
			small:   [ null,      '736px'  ]
		});

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Dropdowns.
		$('#nav > ul').dropotron({
			mode: 'fade',
			noOpenerFade: true,
			alignment: 'center'
		});

	// Nav.

		// Title Bar.
			$(
				'<div id="titleBar">' +
					'<a href="#navPanel" class="toggle"></a>' +
				'</div>'
			)
				.appendTo($body);

		// Panel.
			$(
				'<div id="navPanel">' +
					'<nav>' +
						$('#nav').navList() +
					'</nav>' +
				'</div>'
			)
				.appendTo($body)
				.panel({
					delay: 500,
					hideOnClick: true,
					hideOnSwipe: true,
					resetScroll: true,
					resetForms: true,
					side: 'left',
					target: $body,
					visibleClass: 'navPanel-visible'
				});

})(jQuery);