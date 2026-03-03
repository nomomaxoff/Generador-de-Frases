document.getElementById("BotNuevaFrase").addEventListener("click", loadQuote);

function loadQuote() {

    fetch("/frase-aleatoria")
        .then(response => response.json())
        .then(data => {
            document.getElementById("frase").innerText = `"${data.frase}"`;
            document.getElementById("autor").innerText = `- ${data.autor}`;
        })
        .catch(error => {
            console.error("Error:", error);
            document.getElementById("frase").innerText = "No se pudo cargar la frase.";
            document.getElementById("autor").innerText = "";
        });
}