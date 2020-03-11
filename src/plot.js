setInterval(consume,50);

function consume(){
    fetch("./consume")
    .then((response) => {
        var voltage = document.getElementById('voltage');
        const body = response.json().then((result)=>{
            voltage.innerHTML = result["Voltage"]
        })
    })
}