var t, id;      // Topic, question id
var questions = {
    "politics":{ 0 : "Who is the cringiest politician?",
        1 : "Who is currently the most trended American polician?"},
    "soccer":{ 0 : "Who is currently the most trended soccer player?",
                1 : "Who is the GOAT? (Greatest of all time)"},
    "brands":{ 0 : "Which word is most associated with Nike?",
               1 :  "Which word is most associated with Adidas?"
    }
}

$( document ).ready(function() {
    // Add event handler for changes in selection to the topics dropdown menu
    $("#topics").on('change', function() {
        t = $(this).val();
        var qs = questions[t];
        
        $('#questions').find('option').remove().end();
        var m = JSON.stringify(myqs);
        console.log(m);
        console.log(typeof(m));
        // Add the default option
        $('#questions').append("<option value=\"none\" selected disabled hidden>--</option>");
        for (let step = 0; step < Object.keys(qs).length; step++) {
            // Adds the current questions to the question id.
            //console.log(qs[step]);
            $( "#questions" ).append( "<option value=" + step + ">" + 
            qs[step] + "</option>" );
        }
    });

    // Add event handler for changes in selection to the questions dropdown menu
    $("#questions").on('change', function() {
        id = $(this).val();
        
        console.log('Current question: ' + id);
    });
});

function submitForm() {
    // Construct the URL
    var v = 'http://localhost:8000/result/topicName=' + t +
            '&questionIndex=' + id +
            '&src=tw';
    var u = 'http://localhost:8000/result/topicName=' + t + '&questionIndex=' + id + '&src=tw'
    $.ajax({
        url: u,
        type: "GET", //send it through get method
        data: { 
            topic: t, 
            id: id},
        success: function(response) {
            console.log(response)
            //Do Something
        },
        error: function(xhr) {
            //Do Something to handle error
        }
    });
}