// Handle form submissions
$(function() { //shorthand document.ready function
    $('#keyword-form').on('submit', function(e) {
        document.getElementById('output').innerText = 'Results: Loading...';
        e.preventDefault();  //prevent form from submitting
        var data = $("#keyword-form :input").serializeArray();
        console.log(data);
        $.post('http://localhost:8080', data.value, function(data, status){
            document.getElementById('output').innerText = 'Results: Score is ' + data;
        });
    });
});