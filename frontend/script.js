document.addEventListener('DOMContentLoaded', function () {
    fetch('http://127.0.0.1:5000/predict')
        .then(response => response.json())
        .then(data => {
            const picksContainer = document.getElementById('picks');
            data.forEach(match => {
                const matchElement = document.createElement('div');
                matchElement.innerHTML = `
                    <strong>${match.home_team}</strong> vs <strong>${match.away_team}</strong>:
                    <br>Likely Goal Scorer: ${match.likely_goal_scorer}
                    <br>Over/Under 2.5 Goals: ${match.over_under_2.5 ? 'Over' : 'Under'}
                    <br>Both Teams to Score: ${match.btts ? 'Yes' : 'No'}
                    <br>Outcome: ${match.outcome}
                `;
                picksContainer.appendChild(matchElement);
            });
        });
});
