var count = 999;
var ms = 5;
var countdown = document.getElementById('counter');
var day = countdown.dataset.date;

var counter = setTimeout(timer, ms);

function timer() {
    if ( count >= day ) {
        document.getElementById('counter-day').innerHTML = count;

        if ( count - day > 50 ) {
            count = count - 3;
            var counter = setTimeout(timer, ms);
        } else if ( count - day > 10 ) {
            count = count - 1;
            var counter = setTimeout(timer, 20);
        } else if ( count - day > 1 ){
            count = count - 1;
            var counter = setTimeout(timer, 100);
        } else {
            count = count - 1;
            var counter = setTimeout(timer, 150);
        }
    }
}
function add_mail()
{
mail = $("#email-subscribe").val();
$.post({
    url: 'add_mail',

        headers: {
            'Cache-Control': 'no-cache, no-store',
            'Pragma': 'no-cache',
            'Expires': '0'
        },
        cache: false,
        data: mail,
        dataType: 'json',
        success: function (jsonObj) {
            generate_info(jsonObj);
        },
        error: function () {
            linked(0);
        }
})

}