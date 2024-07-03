const giveawayId = window.location.search.split('=')[1];
fetch(`/giveaway/${giveawayId}`)
	.then(response => response.json())
	.then(data => {
		document.getElementById('giveaway-title').textContent = data.title;
		document.getElementById('giveaway-image').src = data.image_url;
		document.getElementById('giveaway-description').textContent = data.description;
		let countdownElement = document.getElementById('countdown');
		let enterGiveawayButton = document.getElementById('enter-giveaway');
		let endDate = new Date(data.end_date);
		let timeLeft = (endDate - Date.now()) / 1000;
		updateCountdown(countdownElement, timeLeft);
		enterGiveawayButton.addEventListener('click', function() {
			// TODO: Implement actual giveaway entry logic in future versions
			alert('You have entered the giveaway! Good luck!');
		});
	})
	.catch(error => console.error(error));