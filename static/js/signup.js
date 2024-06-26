// signup.js
document.addEventListener('DOMContentLoaded', function() {
    const signupUserForm = document.getElementById('signup-user-form');
    const signupPublisherForm = document.getElementById('signup-publisher-form');

    if (signupUserForm) {
        signupUserForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            const username = document.getElementById('username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm-password').value;

            if (password !== confirmPassword) {
                alert('Passwords do not match!');
                return;
            }

            console.log('User signup attempt:', { username, email });
            
            // TODO: Implement actual signup logic in future versions
            alert('User signup functionality will be implemented in future versions.');
        });
    }

    if (signupPublisherForm) {
        signupPublisherForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            const companyName = document.getElementById('company-name').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm-password').value;

            if (password !== confirmPassword) {
                alert('Passwords do not match!');
                return;
            }

            console.log('Publisher signup attempt:', { companyName, email });
            
            // TODO: Implement actual signup logic in future versions
            alert('Publisher signup functionality will be implemented in future versions.');
        });
    }
});