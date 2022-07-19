function guardar() {

    let d = parseInt(document.getElementById("txtDia").value)
    let m = parseInt(document.getElementById("txtMes").value)
    let lo = document.getElementById("txtLocacion").value
    let lu = document.getElementById("txtLugar").value
    let di = document.getElementById("txtDireccion").value
    let h = document.getElementById("txtHorario").value

    let fecha = {
        dia: d,
        mes: m,
        locacion: lo,
        lugar: lu,
        direccion: di,
        horario: h
    }
    let url = "https://brunocorti.pythonanywhere.com/fechas"
    var options = {
        body: JSON.stringify(fecha),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
       // redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")

            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}