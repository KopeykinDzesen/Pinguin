$(document).ready(function () {

    var href = window.location.href;
    if (href.indexOf('login') > 0){
        $('#nav_link_login').addClass('active');
    }
    else if (href.indexOf('registration') > 0){
        $('#nav_link_registr').addClass('active');
    }
    else if (href.indexOf('contacts') > 0){
        $('#nav_link_contacts').addClass('active');
    };

});
