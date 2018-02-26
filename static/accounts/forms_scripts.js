$( document ).ready(function() {

    $('.form-container').find('input').on('keyup blur focusin focusout', function (e) {

        var $this = $(this);
        var label = $this.prev('label');

        if (e.type === 'keyup') {
            if ($this.val() === '') {
                label.removeClass('active');
                label.parent().css( 'background-color', '#d9ecee' );
            } else {
                label.addClass('active');
                label.parent().css( 'background-color', 'white' );
            }
        } else if (e.type === 'blur') {
            if( $this.val() === '' ) {
                label.removeClass('active');
            } else {
                label.parent().css( 'background-color', '#d9ecee' );
            }
        } else if (e.type === 'focusin') {
                label.parent().css( 'background-color', 'white' );
        } else if (e.type === 'focusout') {
                label.parent().css( 'background-color', '#d9ecee' );
        }

    });

    $('#label_focus').focus();

    activeForm = $('#auth_container');
    unactiveForm = $('#reg_container');
    flagActiveForm = true;
    console.log('activeForm: ', activeForm);
    console.log('unactiveForm: ', unactiveForm);
    console.log('flagActiveForm: ', flagActiveForm);

    $('#reg_container').click(function () {
        if(flagActiveForm){
            swapForm();
        };
    });

    $('#auth_container').click(function () {
        if(!flagActiveForm){
            swapForm();
        };
    });

});

//---------------------------------------------------------

function swapForm() {

    activeForm.css('top', '50px');
    activeForm.css('left', '50px');
    activeForm.css('z-index', '0');
    activeForm.css('background-color', '#1c7430');
    activeForm.css('border-color', '#1c7430');
    activeForm.find('.swap-forms-btn').css('background-color', '#1c7430');
    activeForm.find('.swap-forms-btn').fadeIn(2000);
    activeForm.find('.form-container').fadeOut();

    unactiveForm.css('top', '0');
    unactiveForm.css('left', '0');
    unactiveForm.css('z-index', '1');
    unactiveForm.css('background-color', '#6D64FF');
    unactiveForm.css('border-color', '#E84AE3');
    unactiveForm.find('.swap-forms-btn').css('background-color', '#E84AE3');
    unactiveForm.find('.swap-forms-btn').fadeOut();
    unactiveForm.find('.form-container').fadeIn(2000);

    if(flagActiveForm){
        console.log('ififif');
        unactiveForm = $('#auth_container');
        activeForm = $('#reg_container');
        flagActiveForm = false;
        console.log('activeForm: ', activeForm);
        console.log('unactiveForm: ', unactiveForm);
        console.log('flagActiveForm: ', flagActiveForm);
    } else if(!flagActiveForm) {
        console.log('elseelse');
        activeForm = $('#auth_container');
        unactiveForm = $('#reg_container');
        flagActiveForm = true;
        console.log('activeForm: ', activeForm);
        console.log('unactiveForm: ', unactiveForm);
        console.log('flagActiveForm: ', flagActiveForm);
    };

};

