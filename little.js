    jQuery.expr[':'].Contains = function (a, i, m) {
        return (a.textContent || a.innerText || "").toUpperCase().indexOf(m[3].toUpperCase()) >= 0;
    };

 
function search() {
	var list = $("#ulHouses");
    var filter = $("#searchBox").val();
    if (filter) {
        $(list).find("a:not(:Contains(" + filter + "))").parent().addClass("hide");
        $(list).find("a:not(:Contains(" + filter + "))").parent().prev(".nav-header").addClass("hide");
    	$(list).find("a:Contains(" + filter + ")").parent().prevAll(".nav-header:first").removeClass("hide");
        $(list).find("a:Contains(" + filter + ")").parent().removeClass("hide");


    } else {
        $(list).find("li").removeClass("hide");
        $("#noResults").addClass("hide");

    }
    $("#liEnd").addClass("hide");
}

function sortObject(o) {
    var sorted = {},
    key, a = [];

    for (key in o) {
        if (o.hasOwnProperty(key)) {
                a.push(key);
        }
    }

    a.sort();

    for (key = 0; key < a.length; key++) {
        sorted[a[key]] = o[a[key]];
    }
    return sorted;
}

var useremail;
function joinGroup() {
	var email = $("#useremailjoin").val();
	useremail = email;
	var groupid = $("#usergroupid").val();
	$.ajax({
	  type: "GET",
	  url: "groups/join",
	  data: 'email='+email+'&groupid='+groupid,
	  datatype: "html",
	  success: function(result){
			   if(result == true) {
			   		//the user joined the group
			   		showCurrentGroupTab();
			   } else {
			   		//the groupid doesn't exist or another problem
			   }
			   
	      }
	  });

}


function createGroup() {
	var email = $("#useremailcreate").val();
	useremail = email;
	JSON.stringify(selectedRooms)
	$.ajax({
	  type: "GET",
	  url: "groups/join",
	  data: 'email='+email,
	  datatype: "html",
	  success: function(result){
			   if(result == true) {
			   		//group created
			   } else {
			   		//group cannot be created
			   }
	      }
	  });

}

function sendRoomData() {
	var email = $("#useremailcreate").val();
	$.ajax({
	  type: "GET",
	  url: "rooms/final",
	  data: 'email='+email+'&selected='+JSON.stringify(selectedRooms),
	  datatype: "html",
	  success: function(result){
			   if(result == true) {
			   		//group created
			   } else {
			   		//group cannot be created
			   }
	      }
	  });

}

function selectedRoomUpdate() {
	$("#modalSelectedRooms").html(" ");
	selectedRooms.forEach(function(room){
		$("#modalSelectedRooms").append('<span class="label label-success">'+room[0] + ' '+room[1]+'</span> ');
	});
	
}