$( document ).ready(function() {

    console.log('sljcwboeucbawec');

    activeForm = $('.form-signin');
    unactiveForm = $('.form-signup');
    flagActiveForm = true;

    $('#nav-signin').click(function () {
        if(!flagActiveForm){
            console.log('#nav-signin');
            $('#nav-signup').removeClass('form-nav-text-active');
            $('#nav-signin').addClass('form-nav-text-active');
            $('.form-signin').css('display', 'block');
            $('.form-signup').css('display', 'none');
            flagActiveForm = true;
        };
    });

    $('#nav-signup').click(function () {
        if(flagActiveForm){
            console.log('#nav-signup');
            $('#nav-signup').addClass('form-nav-text-active');
            $('#nav-signin').removeClass('form-nav-text-active');
            $('.form-signin').css('display', 'none');
            $('.form-signup').css('display', 'block');
            flagActiveForm = false;
        };
    });

});