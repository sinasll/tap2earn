document.addEventListener('DOMContentLoaded', () => {
    const gameBox = document.getElementById('gameBox');
    const scoreDisplay = document.getElementById('score');
    const countdownDisplay = document.getElementById('countdown');

    let score = 0;
    let countdownTime = 60; // 1 minute in seconds
    let gameInterval;
    let countdownInterval;

    function createSnowflake() {
        const snowflake = document.createElement('div');
        snowflake.classList.add('snowflake');
        snowflake.innerHTML = '&#10052;'; // Unicode for snowflake symbol
        
        // Position snowflake randomly within the width of the game box
        snowflake.style.left = Math.random() * (gameBox.offsetWidth - 30) + 'px';
        snowflake.style.top = '-30px'; // Start snowflake above the visible area
        
        // Append snowflake to the game box
        gameBox.appendChild(snowflake);
        
        // Animate snowflake falling
        let fallInterval = setInterval(() => {
            let currentTop = parseInt(snowflake.style.top);
            currentTop += 2; // Adjust speed of falling
            snowflake.style.top = currentTop + 'px';
            
            // Remove snowflake if it falls out of the game box
            if (currentTop > gameBox.offsetHeight) {
                clearInterval(fallInterval);
                gameBox.removeChild(snowflake);
            }
        }, 20);

        // Add event listener to capture snowflake clicks
        snowflake.addEventListener('click', () => {
            // Increment score
            score++;
            scoreDisplay.textContent = `Score: ${score}`;
            
            // Remove clicked snowflake
            clearInterval(fallInterval);
            gameBox.removeChild(snowflake);
        });
    }

    function updateCountdown() {
        countdownDisplay.textContent = formatTime(countdownTime);
        countdownTime--;

        if (countdownTime < 0) {
            clearInterval(gameInterval);
            clearInterval(countdownInterval);
            countdownDisplay.textContent = "Game Over";
        }
    }

    function formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    }

    function startGame() {
        // Reset score
        score = 0;
        scoreDisplay.textContent = `Score: ${score}`;
        
        // Start the countdown timer
        countdownTime = 60; // Reset to 1 minute
        countdownInterval = setInterval(updateCountdown, 1000); // Update every second

        // Start creating snowflakes
        gameInterval = setInterval(createSnowflake, 1000); // Spawn snowflakes every second
    }

    // Start the game when the page loads
    startGame();
});
