// movement for card animation 
const card = document.querySelector(".card");
const cardContainer = document.querySelector(".card-container");
// moving Animation Listener

cardContainer.addEventListener("mousemove",(event) => {
    let xAxis = (window.innerWidth / 2 - event.pageX) / 28;
    let yAxis = (window.innerHeight/ 2 - event.pageY) / 28;

    card.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
    console.log("hey");
});