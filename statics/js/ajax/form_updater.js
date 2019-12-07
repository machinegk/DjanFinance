function formUpdater() {
    $("#update-form").submit(function (event) {
        event.preventDefault();
        let formData = new FormData(this);
        $('html,body').animate({scrollTop: 0}, 'slow');
        $.ajax(
            {
                type: "POST",
                async: true,
                url: $("#update-form").attr('action'),
                data: formData,
                dataType: 'json',
                success: (data) => {
                    $('#messages').empty();
                    if (data['success']) {
                        $("#messages").append("<div class=\"alert alert-success\" role=\"alert\">" + data['success'] + "<div style='text-align: right'>[" + data['timestamp'] + "]</div>" + "</div>")
                    } else if (data['error']) {
                        $("#messages").append("<div class=\"alert alert-danger\" role=\"alert\">" + data['error'] + "<div style='text-align: right'>[" + data['timestamp'] + "]</div>" + "</div>")

                    }
                },
                error: () => {
                    $('#messages').empty();
                    $("#messages").append("<div class=\"alert alert-danger\" role=\"alert\">" + "Transferring error occurred" + "<div style='text-align: right'>[" + data['timestamp'] + "]</div>" + "</div>")
                },
                cache: false,
                contentType: false,
                processData: false,
            }
        )
    })
}


$(document).ready(function () {
    formUpdater();

    $(function () {
        $("#datepicker").datepicker({
            dateFormat: "yy-mm-dd",
            autoSize: true,
            showAnim: "fadeIn",
            changeYear: true,
            changeMonth: true,
            yearRange: "1950:2019"
        });
    });

    $("#country_selector").countrySelect();

})
$(document).ajaxStop(function () {
    formUpdater()
})