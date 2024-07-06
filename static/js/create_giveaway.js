<script>
document.getElementById('giveawayForm').addEventListener('submit', function(e) {
	e.preventDefault();
	
	// Update preview
	document.getElementById('previewTitle').textContent = document.getElementById('title').value;
	document.getElementById('previewDescription').textContent = document.getElementById('description').value;
	document.getElementById('previewImage').src = document.getElementById('picture').value;
	document.getElementById('previewEndTime').textContent = new Date(document.getElementById('endTime').value).toLocaleString();

	// Here you would typically send the form data to your server
	alert('Giveaway created successfully! (Note: This is a simulation, no actual data is being sent)');
});

// Real-time preview updates
['title', 'description', 'picture', 'endTime'].forEach(function(id) {
	document.getElementById(id).addEventListener('input', function(e) {
		if (id === 'title') {
			document.getElementById('previewTitle').textContent = e.target.value;
		} else if (id === 'description') {
			document.getElementById('previewDescription').textContent = e.target.value;
		} else if (id === 'picture') {
			document.getElementById('previewImage').src = e.target.value;
		} else if (id === 'endTime') {
			document.getElementById('previewEndTime').textContent = new Date(e.target.value).toLocaleString();
		}
	});
});
</script>