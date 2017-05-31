var fileName = '';

$(document).ready(function () {
    Dropzone.autoDiscover = false;
    $("#file-upload").dropzone({
        addRemoveLinks: false,
        dictDefaultMessage: 'Przyciągnij tutaj plik',
        maxFiles: 1,
        maxFilesize: 10,
        acceptedFiles: ".xls",

        init: function () {
            this.on("maxfilesexceeded", function (file) {
                alert("Możesz wysłać tylko jeden plik!");
            });
            this.on("dictInvalidFileType", function (file) {
                alert("Możesz wysłać tylko dokumeny programu Microsoft Excel!");
            });
        },

        success: function (file, response) {
            if (response.success == true) {
                fileName = response.data.name;
                $('html, body').stop().animate({
                    scrollTop: ($('#step-3').offset().top)
                }, 1250, 'easeInOutExpo');

                $.get("api/uid/" + fileName, function (response) {
                    $("#step-3").removeClass('hidden');
                    $("#scheet-name").text(response.data.name).fadeIn(500);
                    drawChart();
                    getPrecision();
                    getDownloadUrl();
                    $("#step-4").removeClass('hidden');
                });
            }
        },

        error: function (file, response) {
            file.previewElement.classList.add("dz-error");
        }

    });
});


function getPrecision() {
    $.get("api/precision/uid/" + fileName, function (response) {
        $("#precision").text(response.data.precision).fadeIn(500);
    });
}

function getDownloadUrl() {
    $.get("api/download/uid/" + fileName, function (response) {
        $("#downloadButton").attr("href", "/static/files/" + response.data.name);
    });
}

function drawChart() {


    var ctx = document.getElementById("lineChart").getContext('2d');
    $.get("api/chart/cars/uid/" + fileName, function (response) {
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: response.data.labels,
                datasets: [{
                    // label: 'Ryzyko w zależności od wieku kierowcy. 1 to ryzyko wysokie a 0 to ryzyko niskie',
                    label: 'Wysokość składki w zależności od wieku kierowcy',
                    data: response.data.values,
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    });


    var ctx2 = document.getElementById("lineChart-2").getContext('2d');
    $.get("api/chart/cars2/uid/" + fileName, function (response) {
        var myChart2 = new Chart(ctx2, {
            type: 'pie',
            data: {
                // labels: response.data.labels,
                labels: ["Sedan", "Kombi", "Hatchback", "Van", "Kabriolet", "Sportowe"],
                datasets: [{
                    // label: 'Ryzyko w zależności od wieku kierowcy. 1 to ryzyko wysokie a 0 to ryzyko niskie',
                    // label: 'Ilość samochodów każdego typu',
                    // data: [10, 15, 30, 32, 21, 9],
                    data: response.data.values,
                    /*backgroundColor: [
                     'rgba(220,220,220,0.2)',
                     'rgba(220,120,120,0.2)',
                     'rgba(220,220,220,0.2)',
                     'rgba(1,20,50,0.2)',
                     'rgba(46,180,50,0.2)',
                     'rgba(30,220,100,0.2)',
                     ], */
                    backgroundColor: [
                        "#2ecc71",
                        "#3498db",
                        "#95a5a6",
                        "#9b59b6",
                        "#f1c40f",
                        "#e74c3c"
                    ],
                    // borderWidth: 1
                }]
            },
           /* options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }*/
        });
    });


}
