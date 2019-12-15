function reload_page() {
    $("form").on('submit', function (event) {
        let $btn = $(document.activeElement);
        event.preventDefault();
        let formData = new FormData(this);
        formData.append($btn.attr("name"), '');
        let page_url = $('form').attr('action');
        $.ajax({
            url: page_url,
            data: formData,
            type: "POST",
            async: true,
            success: (data) => {
                $('.modal').modal('hide');
                $('#table-reload').hide().empty();
                $('#table-reload').append($(data).find("#table-reload").html()).slideDown(1200);
            },
            cache: false,
            contentType: false,
            processData: false,
        })
    });

}


$(function () {
    reload_page();
})