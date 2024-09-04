function limpiar() {
    const inputText = document.getElementById("input-text").value;
    fetch('/api/v1.0.0/limpiar_env', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({content: inputText})
    })
    .then(response => {
        response.json().then(data => {
            document.getElementById("output-text").value = data.result;
        });
    })
   
}

function convertir() {
    const inputText = document.getElementById("input-text").value;
    fetch('/api/v1.0.0/convertir_env', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({content: inputText})
    })
    .then(response => {
        response.json().then(data => {
            document.getElementById("output-text").value = data.result;
        });
    })
    
}

function copiar() {
    const outputText = document.getElementById("output-text");
    outputText.select();
    document.execCommand("copy");
    alert("Texto copiado al portapapeles");
}


function clear_campos(){
    document.getElementById("output-text").value = "";
    document.getElementById("input-text").value = "";
}