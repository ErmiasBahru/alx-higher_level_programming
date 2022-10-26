/**
 * Script that updates the text of the <header>
 * element to New Header!!! when the user clicks
 * on DIV#update_header
 */
$('DIV#update_header').click(() => {
    $('header').text('New Header!!!');
});
