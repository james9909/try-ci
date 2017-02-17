var current = 0;
$('#increment').click(function(){
    var input = {'n':current};
    $.ajax({
        url: '/fib',
        type: 'GET',
        data: input,
        success: function(d){
            if (d == 'error'){
                console.log("I cri");
            } else {
                current = current + 1
                d = JSON.parse(d);
                fibn = parseFloat(d['result']);
                $('#counterThing').html(fibn);
            };
        }
    });
});
