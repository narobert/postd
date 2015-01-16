function loadAll() {
  profile();
  realComments();
  yourProfile();
  firstLooking();
}
window.onload = loadAll;

$(document).ready(function() {
    $('.search input:text').focus(function() {
        $('.search-button').css("background", "#3b5998");
        document.getElementById("changePic").src="/images/zoom_white.png";
    });
    $('.search input:text').blur(function() {
        $('.search-button').css("background", "white");
        document.getElementById("changePic").src="/images/zoom_black.png";
    });
});

function profile() {
    $.ajax({
        url: "/ajax/posted/picture",
        type: "POST",
        dataType: "json",
        success: function(data) {
            if (data["status"] == "OK") {
                var images = "";
                var image = data["imaged"][0];
                var you = image.path;
                $('#username_picture').html("<img class=photo src=/media/" + you + "></img>");
                $('#delete').html("<p>Delete</p>");
            } else {
                $('#username_picture').html("Empty");
            }
        },
    });
}

function yourProfile() {
    $.ajax({
        url: "/ajax/posted/load",
        type: "POST",
        dataType: "json",
        success: function(data) {
            if (data["status"] == "YAYA") {
                var pictures = "";
                for (var i = 0; i < data["pictured"].length; i++) {
                    var picture = data["pictured"][i];
                    var your = picture.paths;
                    var enlarge = picture.id_picture;
                    pictures += "<div class=img-wrapper><a href=/upload/" + enlarge + "><img class=photo2 src=/media/" + your + "></a></div>";
                }
                $('#your_picture').html(pictures);
            } else {
                $('#your_picture').html("Empty");
            }
        },
    });
}

function firstLooking() {
    $.ajax({
        url: "/ajax/posted/firstLook",
        type: "POST",
        dataType: "json",
        success: function(data) {
            if (data["status"] == "YEE") {
                var pictures = "";
                for (var i = 0; i < data["pictured"].length; i++) {
                    var picture = data["pictured"][i];
                    var your = picture.paths;
                    var enlarge = picture.id_picture;
                    var username_from = picture.username_from;
                    pictures += "<li class=item><a href=/upload/" + enlarge + ">" + username_from + " sent you a pic!</a></li>";
                }
                $('#pre_picture').html(pictures);
                $('#count').html(i);
            } else {
                $('#pre_picture').html("Empty");
                $('#count').html("");
            }
        },
    });
}

$('body').delegate('#user', 'click', function() {
    loadProfiles($(this).attr("data-id"));
}); 

function loadProfiles(id) {
  if (id) {
    var _this = this;
    $.ajax({
        url: "/ajax/posted/getProfile",
        data: ({ id: id }),
        type: "POST",
        dataType: "json",
        success: function(data) {
            if (data["status"] == "OK") {
                var profiles = ""
                var profile = data["profiled"][0];
                var me = profile.username;
                window.location.href = "/user/" + me + "";
            }
        },
    });
  }
};

function realComments() {
    $.ajax({
        url: "/ajax/posted/everyonePics",
        type: "POST",
        dataType: "json",
        success: function(data) {
            if (data["status"] == "OHK") {
                var pictures = "";
                for (var i = 0; i < data["pictured"].length; i++) {
                    var picture = data["pictured"][i];
                    var enlarge = picture.id_picture;
                    viewComments(enlarge);
                }
            }
        },
    });
};

function viewComments(id) {
  if (id) {
    var _this = this;
    $.ajax({
        url: "/ajax/posted/everyone",
        data: ({ id: id }),
        type: "POST",
        dataType: "json",
        success: function(data) {
            if (data["status"] == "OHYEA") {
              var comments = "";
                for (var i = 0; i < data["commented"].length; i++) {
                    var comment = data["commented"][i];
                    var comment_user = comment.user_comment;
                    var comment_title = comment.title;
                    var comment_id = comment.id;
                    var comment_userid = comment.id_user;
                    var comment_image = comment.image;
                    comments += "<div class=row><div class=span1 style=width:45px;><img class=photo_smaller src=/media/" + comment_image + "></img></div><div class=span2 style=margin-left:0px;><a id=user data-id=" + comment_userid + ">" + comment_user + "</a><p class=comment2>" + comment_title + "</p></div></div>";
                }
                $('#comment_picture' + comment_id + '').html(comments);
            } else {
                $('#comment_picture').html("No comments");
            }
        },
    });
  }
};

$('#accepts').click(function() {
    acceptPicture($(this).attr("data-id"));
});

function acceptPicture(id) {
  if (id) {
    var _this = this;
    $.ajax({
        url: "/ajax/posted/accept",
        data: ({ id: id }),
        type: "POST",
        dataType: "json",
        success: function(data) {
            if (data["status"] == "WOO") {
              window.location.href = "/dashboard/";
            }
        },
    });
  }
};

$('#rejects').click(function() {
    rejectPicture($(this).attr("data-id"));
});

function rejectPicture(id) {
  if (id) {
    var _this = this;
    $.ajax({
        url: "/ajax/posted/reject",
        data: ({ id: id }),
        type: "POST",
        dataType: "json",
        success: function(data) {
            if (data["status"] == "WOOP") {
              window.location.href = "/dashboard/";
            }
        },
    });
  }
};

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
