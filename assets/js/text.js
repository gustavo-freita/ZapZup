const text = document.querySelector(".sec-text");

const textLoad = () => {
    setTimeout(() => {
        text.textContent = "Brincadeiras";
    }, 0);
    setTimeout(() => {
        text.textContent = "Baladinhas";
    }, 4000);
    setTimeout(() => {
        text.textContent = "Iluminação";
    }, 8000);
    setTimeout(() => {
        text.textContent = "Som com DJ";
    }, 12000);
}

textLoad();
setInterval(textLoad, 16000);