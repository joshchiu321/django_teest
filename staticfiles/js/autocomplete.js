$(function() {
    $('.station-select').autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "{% url 'station_autocomplete' %}",
                dataType: "json",
                data: {
                    term: request.term
                },
                success: function(data) {
                    response(data);
                }
            });
        },
        minLength: 2
    });
});
