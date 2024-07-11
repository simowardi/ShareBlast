function copyLeads() {
	const textarea = document.getElementById('leads-textarea');
	textarea.select();
	document.execCommand('copy');
}

function filterLeads() {
	const checkbox = document.getElementById('show-emails');
	const showEmailsOnly = checkbox.checked;
	const textarea = document.getElementById('leads-textarea');
	
	{% if show_emails_only %}
	textarea.value = "{% for username, email in leads %}\n{{ email }}\n{% endfor %}";
	{% else %}
	textarea.value = "{% for username, email in leads %}\n{{ username }}, {{ email }}\n{% endfor %}";
	{% endif %}
}