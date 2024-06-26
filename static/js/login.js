// login.js
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            console.log('Login attempt:', { username, password });
            
            // TODO: Implement actual login logic in future versions
            alert('Login functionality will be implemented in future versions.');
        });
    }
});