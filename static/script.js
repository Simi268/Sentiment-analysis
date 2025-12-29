function countChars() {
    const text = document.getElementById("reviewText").value;
    document.getElementById("charCount").innerText = text.length;
}

function showLoader() {
    document.getElementById("loader").classList.remove("hidden");
}
window.onload = () => {
    const bar = document.querySelector(".progress-bar-fill");
    const valueText = document.getElementById("confidenceValue");

    if (!bar || !valueText) return;

    const target = parseInt(bar.dataset.confidence);
    let current = 0;

    // Animate bar
    setTimeout(() => {
        bar.style.width = target + "%";
    }, 300);

    // Animate number count-up
    const counter = setInterval(() => {
        if (current >= target) {
            clearInterval(counter);
        } else {
            current++;
            valueText.innerText = current;
        }
    }, 15);
};
