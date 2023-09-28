// // Get all elements with the "icon" class
// const icons = document.querySelectorAll('#icon');

// // Loop through each icon
// icons.forEach(icon => {
//     const value = icon.getAttribute('data-value');
   
//     // Add a class based on the value
//     if (value === 'positive') {
//         icon.classList.add('positive');
//     } else if (value === 'negative') {
//         icon.classList.add('negative');
//     } else {
//         icon.classList.add('neutral');
//     }
// });



var playButton = document.getElementById('playButton');


function toggleAudio(id) {
    var audio = document.getElementById(id);
    console.log(audio);
    if (audio.paused) {
        playButton.className = "fa fa-square";
        audio.play();
        playButton.className = "fa fa-toggle-right";
        playButton.style="color:blue;";
    } else {
        audio.pause();
        playButton.style="color:green;";
        playButton.className = "fa fa-toggle-right";
    }
}

// // Update the icon when audio playback ends
// audio.addEventListener('ended', function() {
//     playIcon.src = 'play.png'; // Change the icon to play
// });