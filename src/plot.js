
response = setInterval(consume(),2000);

var voltage = document.getElementById('h2');
voltage.innerHTML = response;

function consume(){
    fetch("localhost:8081/consume")
    .then((response) => {
        return response.text();
    })
}