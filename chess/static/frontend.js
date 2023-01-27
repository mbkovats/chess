let before = ""
function move(square){
    console.log(square)
    let elem = document.getElementById(square);
    if(before == ""){
        if(elem.innerHTML.includes("img")){
            before = square;
        }
    }
    else{
        const request = new XMLHttpRequest();
        request.open("POST", '/move');
        request.send(JSON.stringify(before + square));
        before = "";
    }
}
document.getElementById("A8").addEventListener("click", move("A8"));
document.getElementById("B8").addEventListener("click", move("B8"));
document.getElementById("C8").addEventListener("click", move("C8"));
document.getElementById("D8").addEventListener("click", move("D8"));
document.getElementById("E8").addEventListener("click", move("E8"));
document.getElementById("F8").addEventListener("click", move("F8"));
document.getElementById("G8").addEventListener("click", move("G8"));7
document.getElementById("H8").addEventListener("click", move("H8"));
document.getElementById("A7").addEventListener("click", move("A7"));
document.getElementById("B7").addEventListener("click", move("B7"));
document.getElementById("C7").addEventListener("click", move("C7"));
document.getElementById("D7").addEventListener("click", move("D7"));
document.getElementById("E7").addEventListener("click", move("E7"));
document.getElementById("F7").addEventListener("click", move("F7"));
document.getElementById("G7").addEventListener("click", move("G7"));
document.getElementById("H7").addEventListener("click", move("H7"));
document.getElementById("A6").addEventListener("click", move("A6"));
document.getElementById("B6").addEventListener("click", move("B6"));
document.getElementById("C6").addEventListener("click", move("C6"));
document.getElementById("D6").addEventListener("click", move("D6"));
document.getElementById("E6").addEventListener("click", move("E6"));
document.getElementById("F6").addEventListener("click", move("F6"));
document.getElementById("G6").addEventListener("click", move("G6"));
document.getElementById("H6").addEventListener("click", move("H6"));
document.getElementById("A5").addEventListener("click", move("A5"));
document.getElementById("B5").addEventListener("click", move("B5"));
document.getElementById("C5").addEventListener("click", move("C5"));
document.getElementById("D5").addEventListener("click", move("D5"));
document.getElementById("E5").addEventListener("click", move("E5"));
document.getElementById("F5").addEventListener("click", move("F5"));
document.getElementById("G5").addEventListener("click", move("G5"));
document.getElementById("H5").addEventListener("click", move("H5"));
document.getElementById("A4").addEventListener("click", move("A4"));
document.getElementById("B4").addEventListener("click", move("B4"));
document.getElementById("C4").addEventListener("click", move("C4"));
document.getElementById("D4").addEventListener("click", move("D4"));
document.getElementById("E4").addEventListener("click", move("E4"));
document.getElementById("F4").addEventListener("click", move("F4"));
document.getElementById("G4").addEventListener("click", move("G4"));
document.getElementById("H4").addEventListener("click", move("H4"));
document.getElementById("A3").addEventListener("click", move("A3"));
document.getElementById("B3").addEventListener("click", move("B3"));
document.getElementById("C3").addEventListener("click", move("C3"));
document.getElementById("D3").addEventListener("click", move("D3"));
document.getElementById("E3").addEventListener("click", move("E3"));
document.getElementById("F3").addEventListener("click", move("F3"));
document.getElementById("G3").addEventListener("click", move("G3"));
document.getElementById("H3").addEventListener("click", move("H3"));
document.getElementById("A2").addEventListener("click", move("A2"));
document.getElementById("B2").addEventListener("click", move("B2"));
document.getElementById("C2").addEventListener("click", move("C2"));
document.getElementById("D2").addEventListener("click", move("D2"));
document.getElementById("E2").addEventListener("click", move("E2"));
document.getElementById("F2").addEventListener("click", move("F2"));
document.getElementById("G2").addEventListener("click", move("G2"));
document.getElementById("H2").addEventListener("click", move("H2"));
document.getElementById("A1").addEventListener("click", move("A1"));
document.getElementById("B1").addEventListener("click", move("B1"));
document.getElementById("C1").addEventListener("click", move("C1"));
document.getElementById("D1").addEventListener("click", move("D1"));
document.getElementById("E1").addEventListener("click", move("E1"));
document.getElementById("F1").addEventListener("click", move("F1"));
document.getElementById("G1").addEventListener("click", move("G1"));
document.getElementById("H1").addEventListener("click", move("H1"));
