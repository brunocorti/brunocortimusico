var args = location.search.substr(1).split('&');
// lee los argumentos pasados a este formulario
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}
console.log(args)
document.getElementById("txtId").value = parts[0][1]
document.getElementById("txtDia").value = parts[1][1]
document.getElementById("txtMes").value = parts[2][1]
document.getElementById("txtLocacion").value = decodeURI(parts[3][1])
document.getElementById("txtLugar").value = decodeURI(parts[4][1])
document.getElementById("txtDireccion").value = decodeURI(parts[5][1])
document.getElementById("txtHorario").value = decodeURI(parts[6][1])

function modificar() {
    let id = parseInt(document.getElementById("txtId").value)
    let d = parseInt(document.getElementById("txtDia").value)
    let m = parseInt(document.getElementById("txtMes").value)
    let lo = document.getElementById("txtLocacion").value
    let lu = document.getElementById("txtLugar").value
    let di = document.getElementById("txtDireccion").value
    let h = document.getElementById("txtHorario").value
    let fecha = {
        id: id,
        dia: d,
        mes: m,
        locacion: lo,
        lugar: lu,
        direccion: di,
        horario: h
    }
    let url = "http://localhost:5000/fechas/"+id
    var options = {
        body: JSON.stringify(fecha),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            console.error(err);
            alert("Error al Modificar")
        })      
}