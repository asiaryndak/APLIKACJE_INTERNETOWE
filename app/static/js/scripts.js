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
                      console.log( "ok." );
                });
            }
        },

        error: function (file, response) {
            file.previewElement.classList.add("dz-error");
        }

    });
});