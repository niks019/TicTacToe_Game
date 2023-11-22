var resetButton = document.querySelector("#reset");

var allsquares = document.querySelectorAll("td");

function resetFunc(){
    for(var i = 0; i < allsquares.length; i++) {
        allsquares[i].textContent = "";
    }
}

resetButton.addEventListener("click", resetFunc);

function changeMarker(){
    if(this.textContent === ""){
        this.textContent = "X";
    }
    else if(this.textContent === "X"){
        this.textContent = "O";
    }
    else{
        this.textContent = "";
    }
}
for (var index = 0; index < allsquares.length; index++) {
    allsquares[index].addEventListener("click", changeMarker)    
}



console.log("Hello");