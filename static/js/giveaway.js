// static/js/giveaway.js

// Logic to handle countdown timer and other client-side interactions
document.addEventListener('DOMContentLoaded', function() {
    const countdownElement = document.getElementById('countdown');
    const endDate = new Date(countdownElement.textContent);

    function updateCountdown() {
        const now = new Date();
        const diff = endDate - now;

        if (diff <= 0) {
            countdownElement.textContent = "This giveaway has ended.";
            clearInterval(timerInterval);
            location.reload(); // Reload the page to fetch the winner information
            return;
        }

        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((diff % (1000 * 60)) / 1000);

        countdownElement.textContent = `${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds`;
    }

    const timerInterval = setInterval(updateCountdown, 1000);
});
