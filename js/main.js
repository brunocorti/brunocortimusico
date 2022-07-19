if (document.getElementById("app")) {
    const app = new Vue({
        el: "#app",
        data: {
            fechas: [],
            errored: false,
            loading: true
        },
        created() {
            var url = 'https://brunocorti.pythonanywhere.com/fechas'
            this.fetchData(url)
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.fechas = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })
            },
            eliminar(fecha) {
                const url = 'https://brunocorti.pythonanywhere.com/fecha/' + fecha;
                var options = {
                    method: 'DELETE',
                }
                fetch(url, options)
                    .then(res => res.text()) // or res.json()
                    .then(res => {
                        location.reload();
                    })
            }
        }
    })
}