function init() {
    var tmpArray, QueryString;
    var URL = document.location.toString();
    QueryString = URL.substring(URL.lastIndexOf("?") + 1, URL.length);
    tmpArray = QueryString.split("=");
    if (tmpArray[1] == "5") {
 		$(".active").removeClass("active");
		$("#hiring-item").addClass("active");

		$("#company-introduction").addClass("hide");
		$("#mentor-team").addClass("hide");
		$("#latest-dynamic").addClass("hide");
		$("#website-notice").addClass("hide");
		$("#hiring").removeClass("hide");
		$("#contact-us").addClass("hide");
		$("#chuangplus-coffee").addClass("hide");
		$("#local-gov").addClass("hide");
    }
    else if (tmpArray[1] == "6") {
		$(".active").removeClass("active");
		$("#contact-us-item").addClass("active");

		$("#company-introduction").addClass("hide");
		$("#mentor-team").addClass("hide");
		$("#latest-dynamic").addClass("hide");
		$("#website-notice").addClass("hide");
		$("#hiring").addClass("hide");
		$("#contact-us").removeClass("hide");
		$("#chuangplus-coffee").addClass("hide");
		$("#local-gov").addClass("hide");
    }
}
window.onload=init;

$(function(){
	$("#company-introduction-item").click(function(){
		$(".active").removeClass("active");
		$("#company-introduction-item").addClass("active");

		$("#company-introduction").removeClass("hide");
		$("#mentor-team").addClass("hide");
		$("#latest-dynamic").addClass("hide");
		$("#website-notice").addClass("hide");
		$("#hiring").addClass("hide");
		$("#contact-us").addClass("hide");
		$("#chuangplus-coffee").addClass("hide");
		$("#local-gov").addClass("hide");
	})

	$("#mentor-team-item").click(function(){
		$(".active").removeClass("active");
		$("#mentor-team-item").addClass("active");

		$("#company-introduction").addClass("hide");
		$("#mentor-team").removeClass("hide");
		$("#latest-dynamic").addClass("hide");
		$("#website-notice").addClass("hide");
		$("#hiring").addClass("hide");
		$("#contact-us").addClass("hide");
		$("#chuangplus-coffee").addClass("hide");
		$("#local-gov").addClass("hide");
	})

	$("#latest-dynamic-item").click(function(){
		$(".active").removeClass("active");
		$("#latest-dynamic-item").addClass("active");

		$("#company-introduction").addClass("hide");
		$("#mentor-team").addClass("hide");
		$("#latest-dynamic").removeClass("hide");
		$("#website-notice").addClass("hide");
		$("#hiring").addClass("hide");
		$("#contact-us").addClass("hide");
		$("#chuangplus-coffee").addClass("hide");
		$("#local-gov").addClass("hide");
	})

	$("#website-notice-item").click(function(){
		$(".active").removeClass("active");
		$("#website-notice-item").addClass("active");

		$("#company-introduction").addClass("hide");
		$("#mentor-team").addClass("hide");
		$("#latest-dynamic").addClass("hide");
		$("#website-notice").removeClass("hide");
		$("#hiring").addClass("hide");
		$("#contact-us").addClass("hide");
		$("#chuangplus-coffee").addClass("hide");
		$("#local-gov").addClass("hide");
	})

	$("#hiring-item").click(function(){
		$(".active").removeClass("active");
		$("#hiring-item").addClass("active");

		$("#company-introduction").addClass("hide");
		$("#mentor-team").addClass("hide");
		$("#latest-dynamic").addClass("hide");
		$("#website-notice").addClass("hide");
		$("#hiring").removeClass("hide");
		$("#contact-us").addClass("hide");
		$("#chuangplus-coffee").addClass("hide");
		$("#local-gov").addClass("hide");
	})

	$("#contact-us-item").click(function(){
		$(".active").removeClass("active");
		$("#contact-us-item").addClass("active");

		$("#company-introduction").addClass("hide");
		$("#mentor-team").addClass("hide");
		$("#latest-dynamic").addClass("hide");
		$("#website-notice").addClass("hide");
		$("#hiring").addClass("hide");
		$("#contact-us").removeClass("hide");
		$("#chuangplus-coffee").addClass("hide");
		$("#local-gov").addClass("hide");
	})

	$("#chuangplus-coffee-item").click(function(){
		$(".active").removeClass("active");
		$("#chuangplus-coffee-item").addClass("active");

		$("#company-introduction").addClass("hide");
		$("#mentor-team").addClass("hide");
		$("#latest-dynamic").addClass("hide");
		$("#website-notice").addClass("hide");
		$("#hiring").addClass("hide");
		$("#contact-us").addClass("hide");
		$("#chuangplus-coffee").removeClass("hide");
		$("#local-gov").addClass("hide");
	})

	$("#local-gov-item").click(function(){
		$(".active").removeClass("active");
		$("#local-gov-item").addClass("active");

		$("#company-introduction").addClass("hide");
		$("#mentor-team").addClass("hide");
		$("#latest-dynamic").addClass("hide");
		$("#website-notice").addClass("hide");
		$("#hiring").addClass("hide");
		$("#contact-us").addClass("hide");
		$("#chuangplus-coffee").addClass("hide");
		$("#local-gov").removeClass("hide");
	})
});