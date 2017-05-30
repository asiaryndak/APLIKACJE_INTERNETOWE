var fileName = '';

$(document).ready(function () {
    Dropzone.autoDiscover = false;
    $("#file-upload").dropzone({
        addRemoveLinks: false,
        dictDefaultMessage: 'Przyciągnij tutaj plik',
        maxFiles: 1,
        maxFilesize: 10,
        acceptedFiles: ".xls",

        init: function() {
            this.on("maxfilesexceeded", function(file){
                alert("Możesz wysłać tylko jeden plik!");
            });
            this.on("dictInvalidFileType", function(file){
                alert("Możesz wysłać tylko dokumeny programu Microsoft Excel!");
            });
          },

        success: function (file, response) {
            if(response.success == true){
                fileName = response.data.name;
                $('html, body').stop().animate({
                    scrollTop: ($('#step-3').offset().top)
                }, 1250, 'easeInOutExpo');

                $.get( "api/uid/" + fileName, function( response ) {
                      $( "#scheet-name" ).text( response.data.name ).fadeIn(500);
                      drawChart()
                      console.log( "ok." );
                });
            }
        },

        error: function (file, response) {
            file.previewElement.classList.add("dz-error");
        }

    });
});



    function drawChart(){


        var ctx = document.getElementById("lineChart").getContext('2d');
        $.get( "api/chart/cars/uid/" + fileName, function( response ) {
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
        $.get( "api/chart/cars/uid/" + fileName, function( response ) {
            var myChart2 = new Chart(ctx2, {
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


     }
