
	$('#findSa').click((function(e){
		var sid = $('#sid1').val();
		if(sid != ''){
		   $.ajax({
			  url: '/getStud',
			  type: 'post',
			  data: {sid: sid},

			  success: function(response){
					if (response["Find"] == "Found"){
						$("#uname_response").html("");
				  $('#formview').css({'display':'block'});
				  $('#stuDelete').css({'display':'block'});
				  $('#upname').val(response["Name"]);
				  $('#updat').val(response["DOB"]);
				  $('#gender-select2').val(response["Gender"]);
				  $('#Branch2').val(response["Branch"]);
				  $('#cgpa2').val(response["CGPA"]);
				  $('#gradyear2').val(response["Graduation Year"]);
				  $('#placement2').val(response["Placement Status"]);
				  $('#higher-std2').val(response["Higher Studies"]);
					$('#email2').val(response["Email"]);
					$('#sid').val(response["Student ID"]);
					$('#sid3').val(response["Student ID"]);

					}else{
						$('#uname_response').html(response["Find"]).css({'color':'red', 'text-align':'right'});
						$('#formview').css({'display':'none'})
						$('#stuDelete').css({'display':'none'});
					}
			   }
		   });
		}else{
		   $("#uname_response").html("");
		}
	}))
