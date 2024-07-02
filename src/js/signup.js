document.querySelector('form').addEventListener('submit', function(e) {
  e.preventDefault();
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirm-password').value;
  
  if (name && email && password && confirmPassword) {
	if (password !== confirmPassword) {
	  alert('Passwords do not match. Please try again.');
	} else {
	  alert(`Welcome to ShareBlast, ${name}! Your account has been created. In a real application, you would now be logged in and redirected to your dashboard.`);
	  window.location.href = '/dashboard?name=' + encodeURIComponent(name) + '&email=' + encodeURIComponent(email);
	}
  } else {
	alert('Please fill in all fields.');
  }
});