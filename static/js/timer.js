let time = 1800;

setInterval(() => {
    let min = Math.floor(time / 60);
    let sec = time % 60;
    document.getElementById("timer").innerText =
        min + ":" + (sec < 10 ? "0" + sec : sec);
    time--;
    if (time <= 0) window.location.href = "/completed";
}, 1000);
