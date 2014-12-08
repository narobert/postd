function loadAll() {
  profile();
  everyoneImages();
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

function everyoneImages() {
    $.ajax({
        url: "/ajax/posted/everyone",
        type: "POST",
        dataType: "json",
        success: function(data) {
            if (data["status"] == "BOMB") {
                var pictures = "";
                for (var i = 0; i < data["pictured"].length; i++) {
                    var picture = data["pictured"][i];
                    var your = picture.paths;
                    var userid = picture.id;
                    var userid_from = picture.id_from;
                    var title = picture.name;
                    var time = picture.time;
                    var username = picture.username;
                    var username_from = picture.username_from;
                    pictures += "<div class=imageBackground><div class=row><div class=span6><div id=enlarge><img src=/media/" + your + "></div></div><div class=span2><p>Posted on " + time + "</p><p style=margin-top:-10px;>To: <a id=user data-id=" + userid + ">" + username + "</a></p><p style=margin-top:-10px;margin-bottom:20px;>From: <a id=user data-id=" + userid_from + ">" + username_from + "</a></p><div id=caption><p>" + title + "</p></div></div></div></div>";
                }
                $('#everyone_picture').html(pictures);
            } else {
                $('#everyone_picture').html("Empty");
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
