/* ABOUT PAGE CARDS */

// movement for card animation 
const cards = document.querySelectorAll(".card");
const cardContainer = document.querySelector(".card-container");
// moving Animation Listener

for (card of cards) {
    console.log(card)
    card.addEventListener("mousemove",(event) => {
        let xAxis = (window.innerWidth / 2 - event.pageX) / 28;
        let yAxis = (window.innerHeight/ 2 - event.pageY) / 28;
   
        event.target.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
        console.log(event.target)
    });
 }
