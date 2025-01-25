$(document).ready(function() {
    // Slide down the notification with animation
    $('.popup-message').hide().slideDown(400);

    // Automatically hide the pop-up after 3 seconds
    setTimeout(function() {
        $('.popup-message').slideUp(400, function() {
            $(this).remove();
        });
    }, 3000);  // Adjust the timeout as needed
});