function joinGroup() {
	var email = $("#useremailjoin").val();
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