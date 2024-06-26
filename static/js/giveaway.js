// giveaway.js
document.addEventListener('DOMContentLoaded', function() {
    const enterGiveawayButton = document.getElementById('enter-giveaway');
    const countdownElement = document.getElementById('countdown');

    if (enterGiveawayButton) {
        enterGiveawayButton.addEventListener('click', function() {
            // TODO: Implement actual giveaway entry logic in future versions
            alert('You have entered the giveaway! Good luck!');
        });
    }

    if (countdownElement) {
        // Simple countdown timer (replace with actual end time in future versions)
        let timeLeft = 172800; // 48 hours in seconds

        function updateCountdown() {
            const days = Math.floor(timeLeft / 86400);
            const hours = Math.floor((timeLeft % 86400) / 3600);
            const minutes = Math.floor((timeLeft % 3600) / 60);
            const seconds = timeLeft % 60;

            countdownElement.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`;

            if (timeLeft > 0) {
                timeLeft--;
                setTimeout(updateCountdown, 1000);
            } else {
                countdownElement.textContent = 'Giveaway ended';
                enterGiveawayButton.disabled = true;
            }
        }

        updateCountdown();
    }
});