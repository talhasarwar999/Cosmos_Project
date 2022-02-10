const currentLocation = location.href;
const menuItem = document.querySelectorAll('.nav-link');
const menuLength = menuItem.length
for (let i = 0; i < menuLength; i++) {
    if (menuItem[i].href === currentLocation) {
        menuItem[i].className = ("nav-link active")
    }
}

$(document).ready(function (e) {


    $("#next-1").click(function (e) {
        e.preventDefault();

        $('.contact-info input:required').each(function () {
            if ($(this).val().length === 0) {
                $(this).css("border", "1px solid red");
            } else {
                $(this).css("border", "1px solid lightgrey");
            }
        });

        var form = document.getElementById("press-form");
        var email = document.getElementById("p_email").value;
        var text = document.getElementById("email-error");
        var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

        if (email.match(pattern) && email != '') {
            form.classList.remove("invalid");
            document.getElementById("email-error").style.display = "none";
            document.getElementsByClassName("contact-info")[0].style.display = "none";
            document.getElementsByClassName("project-info")[0].style.display = "block";
        } else {
            document.getElementById("email-error").style.display = "block";
            form.classList.add("invalid");
            text.innerHTML = '<p class="error">Invalid Email</p>';
        }
    });

    $("#prev-1").click(function (e) {
        $(".project-info").hide();
        $(".contact-info").show();
        e.preventDefault();
    });

    $("#next-2").click(function (e) {
        $(".project-info").hide();
        $(".your_msg").show();
        e.preventDefault();
    });

    $("#prev-2").click(function (e) {
        $(".your_msg").hide();
        $(".project-info").show();
        e.preventDefault();
    });

    $("#p_submit").click(function () {
        // e.preventDefault();
        if ($(".p_msg").val() == '') {
            $("#p_msgError").html('*Message is required.');
            return false;
        } else {
            return true;
        }
    });
    // Press Info End

    $("#next-3").click(function (e) {
        $(".acadmic_info").hide();
        $(".aca-contact-info").show();
        e.preventDefault();
    });

    $("#next-4").click(function (e) {
        e.preventDefault();

        $('.aca-contact-info input:required').each(function () {
            if ($(this).val().length === 0) {
                $(this).css("border", "1px solid red");
            } else {
                $(this).css("border", "1px solid lightgrey");
            }
        });

        var form2 = document.getElementsByClassName("acadmic-form")[0];
        var email2 = document.getElementById("ac_email").value;
        var text2 = document.getElementById("email-error2");
        var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

        if (email2.match(pattern) && email2 != '') {
            form2.classList.remove("invalid");
            document.getElementById("email-error2").style.display = "none";
            document.getElementsByClassName("aca-contact-info")[0].style.display = "none";
            document.getElementsByClassName("ac-project-info")[0].style.display = "block";
        } else {
            document.getElementById("email-error2").style.display = "block";
            form2.classList.add("invalid");
            text2.innerHTML = '<p class="error">Invalid Email</p>';
        }
    });

    $("#prev-4").click(function (e) {
        $(".ac-project-info ").hide();
        $(".aca-contact-info").show();
        e.preventDefault();
    });


    $("#next-5").click(function (e) {
        $(".ac-project-info").hide();
        $(".ac-your_msg").show();
        e.preventDefault();
    });

    $("#prev-5").click(function (e) {
        $(".ac-your_msg").hide();
        $(".ac-project-info").show();
        e.preventDefault();
    });

    $("#ac_submit").click(function () {
        // e.preventDefault();
        if ($(".ac_msg").val() == '') {
            $("#ac_msgError").html('*Message is required.');
            return false;
        } else {
            return true;
        }
    });
    // Acadmic Form End

    $("#next-6").click(function (e) {
        $(".career_info").hide();
        $(".career-contact-info").show();
        e.preventDefault();
    });

    $("#next-7").click(function (e) {
        e.preventDefault();

        $('.career-contact-info input:required').each(function () {
            if ($(this).val().length === 0) {
                $(this).css("border", "1px solid red");
            } else {
                $(this).css("border", "1px solid lightgrey");
            }
        });

        var form3 = document.getElementsByClassName("career-form")[0];
        var email3 = document.getElementById("c_email").value;
        var text3 = document.getElementById("email-error3");
        var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

        if (email3.match(pattern) && email3 != '') {
            form3.classList.remove("invalid");
            document.getElementById("email-error3").style.display = "none";
            document.getElementsByClassName("career-contact-info")[0].style.display = "none";
            document.getElementsByClassName("career-job")[0].style.display = "block";
        } else {
            document.getElementById("email-error3").style.display = "block";
            form3.classList.add("invalid");
            text3.innerHTML = '<p class="error">Invalid Email</p>';
        }
    });

    $("#prev-7").click(function (e) {
        $(".career-job").hide();
        $(".career-contact-info").show();
        e.preventDefault();
    });

    $("#next-8").click(function (e) {
        $(".career-job").hide();
        $(".career-your_msg").show();
        e.preventDefault();
    });

    $("#prev-8").click(function (e) {
        $(".career-your_msg").hide();
        $(".career-job").show();
        e.preventDefault();
    });

    $("#c_submit").click(function () {
        // e.preventDefault();
        if ($(".c_msg").val() == '') {
            $("#c_msgError").html('*Message is required.');
            return false;
        } else {
            return true;
        }
    });

    $("#next-9").click(function (e) {
        e.preventDefault();

        $('.inquery-contact-info input:required').each(function () {
            if ($(this).val().length === 0) {
                $(this).css("border", "1px solid red");
            } else {
                $(this).css("border", "1px solid lightgrey");
            }
        });

        var form4 = document.getElementsByClassName("b_inquery-form")[0];
        var email4 = document.getElementById("b_email").value;
        var text4 = document.getElementById("email-error4");
        var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

        if (email4.match(pattern) && email4 != '') {
            form4.classList.remove("invalid");
            document.getElementById("email-error4").style.display = "none";
            document.getElementsByClassName("inquery-contact-info")[0].style.display = "none";
            document.getElementsByClassName("inquery-your_msg")[0].style.display = "block";
        } else {
            document.getElementById("email-error4").style.display = "block";
            form4.classList.add("invalid");
            text4.innerHTML = '<p class="error">Invalid Email</p>';
        }
    });

    $("#prev-9").click(function (e) {
        $(".inquery-your_msg").hide();
        $(".inquery-contact-info").show();
        e.preventDefault();
    });

    $("#b_submit").click(function () {
        // e.preventDefault();
        if ($(".b_msg").val() == '') {
            $("#b_msgError").html('*Message is required.');
            return false;
        } else {
            return true;
        }
    });

    $("#next-10").click(function (e) {
        e.preventDefault();

        $('.other-contact-info input:required').each(function () {
            if ($(this).val().length === 0) {
                $(this).css("border", "1px solid red");
            } else {
                $(this).css("border", "1px solid lightgrey");
            }
        });

        var form5 = document.getElementsByClassName("other-form")[0];
        var email5 = document.getElementById("o_email").value;
        var text5 = document.getElementById("email-error5");
        var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

        if (email5.match(pattern) && email5 != '') {
            form5.classList.remove("invalid");
            document.getElementById("email-error5").style.display = "none";
            document.getElementsByClassName("other-contact-info")[0].style.display = "none";
            document.getElementsByClassName("other-your_msg")[0].style.display = "block";
        } else {
            document.getElementById("email-error5").style.display = "block";
            form5.classList.add("invalid");
            text5.innerHTML = '<p class="error">Invalid Email</p>';
        }
    });

    $("#prev-10").click(function (e) {
        $(".other-your_msg").hide();
        $(".other-contact-info").show();
        e.preventDefault();
    });

    $("#o_submit").click(function () {

        $('.other-your_msg input:required').each(function () {
            if ($(this).val().length === 0) {
                $(this).css("border", "1px solid red");
            } else {
                $(this).css("border", "1px solid lightgrey");
            }
        });
        // e.preventDefault();
        if ($(".o_msg").val() == '') {
            $("#o_msgError").html('*Message is required.');
            return false;
        } else {
            return true;
        }
    });
    // Other Contact Info End

    // Press Contact Form Select disable on change
    var radio_check = jQuery('.more-info input[type=radio]');
    var select = jQuery('.search-project select#all_projects');
    var reset = jQuery('#r_btn');

    select.click(function () {
        radio_check.attr('disabled', 'disabled');
        radio_check.prop("checked", false);
    });

    radio_check.click(function () {
        select.attr('disabled', 'disabled');
        $('#all_projects').prop('selectedIndex', 0);
    });

    reset.click(function () {
        select.removeAttr("disabled");
        radio_check.removeAttr("disabled");
        radio_check.prop("checked", false);
        $('#all_projects').prop('selectedIndex', 0);
    });

    // Contact Form Select disable on change
    var radio_check2 = jQuery('.ac-more-info input[type=radio]');
    var select2 = jQuery('.ac-search-project select#all_projects');
    var reset2 = jQuery('#r_btn2');

    select2.click(function () {
        radio_check2.attr('disabled', 'disabled');
        radio_check2.prop("checked", false);
    });

    radio_check2.click(function () {
        select2.attr('disabled', 'disabled');
        $('#all_projects').prop('selectedIndex', 0);
    });

    reset2.click(function () {
        select2.removeAttr("disabled");
        radio_check2.removeAttr("disabled");
        radio_check2.prop("checked", false);
        $('#all_projects').prop('selectedIndex', 0);
    });


    $("#ed_history").click(function (e) {
        $("#ed_form, .education_ex .text2").show();
        $(".education_ex .text1").hide();
        $("#ed_history").hide();
        e.preventDefault();
    });


    $("#edu_cancel").click(function (e) {
        var institute = document.getElementById("id_institution");
        var g_year = document.getElementById("g_year");
        var mj_subject = document.getElementById("id_area_of_study");
        var degree = document.getElementById("id_degree");
        $(".education_ex .text1").show();
        $("#ed_form, .education_ex .text2").hide();
        $(".education_ex #ed_history").show();

        degree.value = "";
        institute.value = "";
        g_year.value = "";
        mj_subject.value = "";
        e.preventDefault();
    });

    $("#exp_history").click(function (e) {
        $("#exp_form, .expirence_de .text4").show();
        $(".expirence_de .text3").hide();
        $("#exp_history").hide();
        e.preventDefault();
    });

    $("#exp_cancel").click(function (e) {
        var C = document.getElementById("id_company");
        var j_t = document.getElementById("id_job_title");
        var s_y = document.getElementById("start_year");
        var e_y = document.getElementById("end_year");
        // var rs = document.getElementById("rs");
        $(".expirence_de .text3").show();
        $("#exp_history").show();
        $("#exp_form, .expirence_de .text4").hide();

        C.value = "";
        j_t.value = "";
        s_y.value = "";
        e_y.value = "";
        $('textarea#res').val('');
        // rs.value = "";
        // mj_subject.value = "";
        e.preventDefault();
    });

    // Jobs form Open
    $(".apply-button").click(function (e) {
        $(".job_form").show(),
            $('html, body').animate({
                scrollTop: 0
            }),
            $("#shaded").css('pointer-events', 'none'),
            $("#shaded").css('opacity', '0.5');
        e.preventDefault();
    });

    // Jobs form Close
    $(".close-btn").click(function (e) {
        $(".job_form").hide(),
            $("#shaded").css('pointer-events', ''),
            $("#shaded").css('opacity', '1');
        e.preventDefault();
    });

    $('.close-btn').click(function (e) {
        $('.alert').removeClass("show");
        $('.alert').addClass("hide");
        e.preventDefault();
    });
    // Jobs form Submitted END

    // Blog Post Text Limit ...
    function truncateText(selector, maxLength) {
        var element = document.querySelectorAll(selector);
        for (var i = 0; i <= selector.length; i++) {
            var truncated = element[i].innerText;
            if (truncated.length > maxLength) {
                truncated = truncated.substr(0, maxLength) + '...';
            }
            element[i].innerText = truncated;
        }
    }
    truncateText('.blog h5', 30);
    // truncateText('.Product-Page-Banner-Image h2, .Product-Page-Banner-Heading h2', 60),
    // truncateText('.boxes .box p', 20);

});

$(document).ready(function () {

    // Banner Page Text Limit ...
    function truncateText(selector, maxLength) {
        var element = document.querySelectorAll(selector);
        for (var i = 0; i <= selector.length; i++) {
            var truncated = element[i].innerText;
            if (truncated.length > maxLength) {
                truncated = truncated.substr(0, maxLength) + '...';
            }
            element[i].innerText = truncated;
        }
    }
    truncateText('.Product-Page-Banner-Image h2, .Product-Page-Banner-Heading h2', 60);

    // Reset Filters
    $('form').each(function () {
        var form = $(this),
            reset = form.find(':reset'),
            inputs = form.find(':input');

        reset.on('click', function () {
            setTimeout(function () {
                inputs.trigger('change');
            }, 50);
        });
    });

});

// Font Page Related News
$(document).ready(function () {
    function truncateText(selector, maxLength) {
        var element = document.querySelectorAll(selector);
        for (var i = 0; i <= selector.length; i++) {
            var truncated = element[i].innerText;
            if (truncated.length > maxLength) {
                truncated = truncated.substr(0, maxLength) + '...';
            }
            element[i].innerText = truncated;
        }
    }
    truncateText('.boxes .box p', 130);
});

window.onscroll = function () {

    if (window.pageYOffset > 20) {
        $("nav.navbar.navbar-expand-lg.fixed-top.navbar-light.bg-light").addClass("active");
    } else {
        $("nav.navbar.navbar-expand-lg.fixed-top.navbar-light.bg-light").removeClass("active");
    }
};

$(document).ready(function () {
    var mybutton = document.getElementById("myBtn");

    function topFunction() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0;
    }
});