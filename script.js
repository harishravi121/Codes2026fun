document.addEventListener('DOMContentLoaded', () => {
    const button5 = document.getElementById('btn-5');
    const resultDisplay = document.getElementById('result');
    
    const directions = ['Left', 'Right', 'Up', 'Down'];

    button5.addEventListener('click', () => {
        // Generate a random index between 0 and 3
        const randomIndex = Math.floor(Math.random() * directions.length);
        const chosenDirection = directions[randomIndex];
        
        // Update the UI
        resultDisplay.textContent = `Direction: ${chosenDirection}`;
        console.log(`Random Direction: ${chosenDirection}`);
    });
});
