$('#usernames').click(function() {
    $.ajax({
        url: "/ajax/posted/picture",
        type: "POST",
        dataType: "json",
        success: function(data) {
            if (data["status"] == "OK") {
                var images = "";
                var image = data["imaged"][0];
                var you = image.path;
                $('#username_picture').html("<img style=width:200px;height:200px; src=/media/" + you + ">");
                $('#delete').html("<p>Delete</p>");
            } else {
                $('#username_picture').html("Empty");
            }
        },
    });
});

$('#delete').click(function() {
    $.ajax({
        url: "/ajax/posted/delete",
        type: "POST",
        dataType: "json",
        success: function(data) {
            if (data["status"] == "Deleted") {
                $('#username_picture').html("Picture deleted");
                $('#delete').html("");
            }
        },
    });
});
