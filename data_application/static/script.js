var t, id;      // Topic, question id
var questions = {
    "politics":{ 0 : "Who is the cringiest politician?",
        1 : "Who is currently the most trended American polician?"},
    "soccer":{ 0 : "Who is currently the most trended soccer player?",
                1 : "Who is the GOAT? (Greatest of all time)"},
    "brands":{ 0 : "Which is most associated with Nike?",
               1 :  "Which is most associated with Adidas?"
    }
}

$( document ).ready(function() {
    // Add event handler for changes in selection to the topics dropdown menu
    $("#topics").on('change', function() {
        t = $(this).val();
        var qs = questions[t];
        console.log(Object.keys(qs).length);
        $('#questions').find('option').remove().end();
        
        // Add the default option
        $('#questions').append("<option value=\"none\" selected disabled hidden>--</option");
        for (let step = 0; step < Object.keys(qs).length; step++) {
            // Adds the current questions to the question id.
            console.log(qs[step]);
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

    var u = 'localhost:8000/result/topicName=' + t +
            '&questionIndex=' + id +
            '&src=tw';
    $.ajax({
        url: u,
        type: "POST", //send it through get method
        data: { 
            topic: t, 
            id: id},
        success: function(response) {
            //Do Something
        },
        error: function(xhr) {
            //Do Something to handle error
        }
    });
}