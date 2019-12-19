var t;      // Current topic

$( document ).ready(function() {
    // Add event handler for changes in selection to the topics dropdown menu
    $("#topics").on('change', function() {
        t = $(this).val();
        var qs = questions[t];
        
        $('#questions').find('option').remove().end();

        // Add the default option
        $('#questions').append("<option value=\"none\" selected disabled hidden>--</option>");
        for (let step = 0; step < qs.length; step++) {
            // Adds the current questions to the question id.
            //console.log(qs[step]);
            $( "#questions" ).append( "<option value=" + step + ">" + 
            qs[step] + "</option>" );
        }
    });
});