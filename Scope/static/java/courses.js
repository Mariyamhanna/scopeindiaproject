

function show_mobile_menu(){
	if(document.getElementById("mobile_menu").style.display == "inline-block"){
		document.getElementById("mobile_menu").style.display = "none";
	}else{
		document.getElementById("mobile_menu").style.display = "inline-block";
	}
}


function showFloatButtons(){
	document.getElementById("container_right_float_items").style.display = "block";
}

// Timer is set to call the showAd function in 3 seconds after the page is loaded
// const timer= setTimeout(showFloatButtons, 3000);
// interval_id = setInterval(showFloatButtons, 10000);


// ============ scrollToTop =============
window.onscroll = function() {
  let button = document.getElementById("up_button");
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    button.style.display = "block"; 
  } else {
    button.style.display = "none"; 
  }
};
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}


// JQUERY --------------------------------------------------------------------------//

$(document).ready(function(){


  $("#mobile_menu_button, #mobile_menu").click(function(){
  	//alert("test");
    $("#mobile_menu").fadeToggle(500);
    $("#container_right_float_items").fadeToggle(500);
  });

  $(".close_button_float_box").click(function(){
  	//alert("test");
    $("#container_right_float_items").fadeToggle(500);
  });

  $("#callback_title").click(function(){
      $("#call_back_form_set").slideToggle(500);
  });

  $("#callback_button").click(function(e) {
    e.preventDefault();
  
    let client_name = $("#call_back_visitor_name").val().trim();
    let client_contact = $("#call_back_visitor_phone").val().trim();
    let name_error = $("#name_error");
    let phone_error = $("#phone_error");
    let isValid = true;
  
    name_error.text("").hide();
    phone_error.text("").hide();
  
    if (!/^[A-Za-z\s]+$/.test(client_name) || client_name.length < 4) {
      name_error.text("Please enter a valid name").show();
      name_error.append('<br>')
      isValid = false;
    }
  
    if (!/^\+?\d{10,13}$/.test(client_contact)) {
      phone_error.text("Please enter a valid phone number").show();
      isValid = false;
    }
  
    if (isValid) {
      name_error.text("").hide();
      phone_error.text("").hide();
  
      $("#call_back_visitor_name, #call_back_visitor_phone").val("");
      $("#callback_button").prop("disabled", true);
  
      $.post("https://scopeindia.org/php/callback-email.php", {
        call_back_visitor_name: client_name,
        call_back_visitor_phone: client_contact
      }, function(data) {
        console.log(data);
        $("#callback_button").prop("disabled", false);
  
        $("#callback_message").text("We have received your request, we will be back to you ASAP.")
          .fadeIn(2000).delay(7000).fadeOut(1000).append('<br>');
      }).fail(function() {
        $("#callback_button").prop("disabled", false);
        $("#callback_message").text("Something went wrong, please try again later.")
          .fadeIn(2000).delay(7000).fadeOut(1000);
      });
    }
  });
  

  $("#callback_button1").click(function(e){

    window.location.href = "tel:+919745936073";

    e.preventDefault();
    let client_name = $("#call_back_visitor_name").val().trim();
    let client_contact = $("#call_back_visitor_phone").val().trim();
    let name_error = $("#name_error");
    let phone_error = $("#phone_error");
    let isValid = true;

    name_error.text("").hide();
    phone_error.text("").hide();

    if((client_name.length<4)){
        isValid = false;
    }

    if(client_contact.length < 10 || client_contact.length > 13){
      isValid = false;
   }

    if (isValid) {
      name_error.text("").hide();
      phone_error.text("").hide();

      $("#callback_message").text("We have received your request, we will be back to you ASAP.")
        .fadeIn(1000).delay(7000).fadeOut(1000);
      
      $("#call_back_visitor_name, #call_back_visitor_phone").val("");

      $.post("https://scopeindia.org/php/callback-email.php", {
        call_back_visitor_name: client_name,
        call_back_visitor_phone: client_contact
      }, function(data) {
        
      });
    }

  });

  function showPopup() {
    $('#call_back_overlay').css('display', 'flex').fadeIn(500);
  }

  $('#call_back_form_pop').click(function () {
    showPopup();
  });


  $('.close_button_overlay').click(function () {

    let name_error = $("#name_error");
    let phone_error = $("#phone_error");

    name_error.text("").hide();
    phone_error.text("").hide();
    $('#call_back_visitor_name, #call_back_visitor_phone').val("");
    $('#call_back_overlay').fadeOut(500); 

    setTimeout(showPopup, 30000);

  });

  setTimeout(function () {
    showPopup();
  }, 20000);

// $('#call_back_overlay').click(function() {
//   $('#call_back_overlay').fadeOut();
// });


  $('#reg_date_of_birth').on('click', function(){
    var today = new Date().toISOString().split('T')[0];
    $(this).attr('max', today);
  });

  $('#back_to_courses').click(function(){
    window.location.href = "courses-scope-india.html";
  });

  // if we want to disable right click
  
  // $(document).on('contextmenu', function(e) {
  //   e.preventDefault();
  // });
});

// JQUERY --------------------------------------------------------------------------//

