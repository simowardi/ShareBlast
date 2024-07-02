// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
	anchor.addEventListener('click', function (e) {
	  e.preventDefault();
	  document.querySelector(this.getAttribute('href')).scrollIntoView({
		behavior: 'smooth'
	  });
	});
  });

  // Add parallax effect to hero section
  window.addEventListener('scroll', function() {
	const scrollPosition = window.pageYOffset;
	document.querySelector('.hero').style.backgroundPositionY = scrollPosition * 0.5 + 'px';
  });