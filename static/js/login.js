// login.js
document.querySelector('form').addEventListener('submit', function(e) {
	e.preventDefault();
	const email = document.getElementById('email').value;
	const password = document.getElementById('password').value;
	
	if (email && password) {
	  alert(`Welcome back! In a real application, you would now be logged in and redirected to your dashboard. Email used: ${email}`);
	  window.location.href = '/dashboard?email=' + encodeURIComponent(email);
	} else {
	  alert('Please enter both email and password.');
	}
  });