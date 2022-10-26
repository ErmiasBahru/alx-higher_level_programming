/**
 * Script that fetches and prints how to say “Hello”
 * depending on the language
 */
$(document).ready(() => {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
    $('INPUT#btn_translate').click(() => {
        $.get(url + $.param({ lang: $('INPUT#language_code').val() }), (data) => {
            $('DIV#hello').html(data.hello);
        });
    });
});
