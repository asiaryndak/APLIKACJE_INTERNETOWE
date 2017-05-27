$(document).ready(function () {
    var fileName = '';
    Dropzone.autoDiscover = false;
    $("#file-upload").dropzone({
        addRemoveLinks: true,
        dictDefaultMessage: 'Przyciągnij tutaj plik',
        maxFiles: 1,

        init: function() {
            this.on("maxfilesexceeded", function(file){
                alert("Możesz wysłać tylko jeden plik!");
            });
          },

        success: function (file, response) {
            if(response.success == true){
                fileName = response.data.name;
                $('html, body').stop().animate({
                    scrollTop: ($('#step-3').offset().top)
                }, 1250, 'easeInOutExpo');
            }
        },
        error: function (file, response) {
            file.previewElement.classList.add("dz-error");
        }
    });
});