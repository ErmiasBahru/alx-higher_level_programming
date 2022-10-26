/**
 * Script that fetches and prints how to say “Hello” depending on the language
 *
 * translation fetched when the user clicks on INPUT#btn_translate
 * OR presses ENTER when the focus is on INPUT#language_code
 */
function makeTranslate() {
    const url = 'https://www.fourtonfish.com/hellosalut/?';
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), (data) => {
        $('DIV#hello').html(data.hello);
    });
}

$('document').ready(() => {
    $('INPUT#btn_translate').click(makeTranslate);
    $('INPUT#language_code').focus(() => {
        $(this).keydown((e) => {
            if (e.keyCode === 13) {
                makeTranslate();
            }
        });
    });
});
