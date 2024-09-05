$(document).ready(() => {
    $('.nav-link').each(function () {
        console.log($(this))
        $(this).attr('href') == window.location.pathname?
            $(this).addClass('active')
        : $(this).removeClass('active')
    })
})