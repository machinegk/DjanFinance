function pageLoader() {
$("a.menu-link").each(function () {
    $(this).click((e) => {
        e.preventDefault();
        let page_url = $(this).attr('href');

        $.ajax({
            url: page_url,
            type:"GET",
            async: true,
            success: (data) => {
                console.log(data)
                $('#page-content').empty();
                $('#page-content').append($(data).filter("div").html())
            }
        })
    })
})

    
}





$(document).ready(function () {
    pageLoader()
})
// $(document).ajaxStop(function () {
//     pageLoader()
// })