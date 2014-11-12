jQuery(document).ready(function($) {
    $("body").on("keypress click", "input[name='text']", function () {
        $('.has-error').hide();
    });
});
