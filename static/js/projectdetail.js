$(function(){
	$("#roadshowlabel").click(function(){
		$("#textlabel").removeClass("tab-active");
		$("#roadshowlabel").addClass("tab-active");
		$("#roadshowpanel").removeClass("hide");
		$("#textpanel").addClass("hide");
		$("#xiaojiao1").removeClass("hide");
		$("#xiaojiao2").addClass("hide");
	})

	$("#textlabel").click(function(){
		$("#roadshowlabel").removeClass("tab-active");
		$("#textlabel").addClass("tab-active");
		$("#textpanel").removeClass("hide");
		$("#roadshowpanel").addClass("hide");
		$("#xiaojiao1").addClass("hide");
		$("#xiaojiao2").removeClass("hide");
	})
});