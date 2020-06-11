function checkWordCount(){
    s = document.getElementById("keywords").value;
    if (s.split(" ").length < 5) {
        alert("Atleast 5 Keywords required...");
        return false;
    }
}   