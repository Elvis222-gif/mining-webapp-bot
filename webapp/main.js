let coins = 0;
let mining = false;

function startMining() {
  if (!mining) {
    mining = true;
    setInterval(() => {
      coins += 1;
      document.getElementById("coins").innerText = coins;
    }, 1000);
  }
}
