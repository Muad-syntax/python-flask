function bukaModal(id, namaLama){
    var modal = document.getElementById("modalEdit")
    var input = document.getElementById("inputNama")
    var form = document.getElementById("formEdit")

    modal.style.display = "block";
    input.value = namaLama;
    form.action = "/edit" + id;
}

function tutupModal(){
    document.getElementById("modalEdit").style.display = "none";
}

window.onclick = function(event){
    var modal = this.document.getElementById("modalEdit");
    if (event.target == modal){
        modal.style.display = "none"
    }
}