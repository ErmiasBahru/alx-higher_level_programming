/**
 * script that adds, removes and clears LI elements
 * from a list when the user clicks
 */
$(document).ready(() => {
    $('DIV#add_item').click(() => {
        $('UL.my_list').append('<li> Item </li>');
    });
    $('DIV#remove_item').click(() => {
        $('UL.my_list li:last-child').remove();
    });
    $('DIV#clear_list').click(() => {
        $('UL.my_list').empty();
    });
});
