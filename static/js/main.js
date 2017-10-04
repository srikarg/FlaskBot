$(document).ready(function() {
    var logMessage = function (message, user, log) {
        var user = user === 'flaskbot' ? 'Flaskbot' : 'You';
        log.append('<li><span class="user">' + user + '</span><span class="message">' + message + '</span></li>');
        $('html, body').animate({
            scrollTop: $(document).height()
        }, '400');
    }

    var log = $('.log ul');
    var input = $('.input');
    var form = $('.form');
    input.focus();

    form.on('submit', function (event) {
        event.preventDefault();

        var text = input.val().trim();
        input.val('');
        logMessage(text, 'you', log);

        if (text === '!clear') {
            log.empty();
            return;
        } else if (text === '!hide') {
            log.find('span.user').each(function () {
                if ($(this).text().trim() === 'You') {
                    $(this).parent('li').remove();
                }
            });
            return;
        }

        if (text !== '') {
            $.ajax({
                type: 'POST',
                url: '/',
                data: {
                    message: text
                },
                success: function (data) {
                    logMessage(data.message, 'flaskbot', log);
                    input.focus();
                }
            });
        }
    });
});

