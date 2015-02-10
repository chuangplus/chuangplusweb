/**
 * Created by Charlotte on 1/25/2015.
 */
console.log($(".banner").height());
//window.setTimeoutInterval(500);
var titleNumber = 0;
var title1 = ["什么是关注项目？", "什么是邀请路演？", "什么是直接联系？"];
var title2 = ["创+会把您关注的项目放到个人页面您关注的项目内，这样您就可以持续获得您关注的项目的最新信息。",
    "创+每周都会举行线上路演，你可以邀请感兴趣的项目进行线下路演，与您面对面交流，，我们每两周会选取获得邀请数最多的项目，进行线下路演。",
    "线上路演的过程中，如果您对某个项目非常感兴趣，则可以选择直接联系，创+会在48小时内受理，联系团队与投资人直接对接。"];
var title_background = ["url(../static/img/base-financing/0.jpg)", "url(../static/img/base-financing/1.jpg)", "url(../static/img/base-financing/2.jpg)"];
$("#banner1").click(function(){
        titleNumber = (titleNumber + 2) % 3;
        $(".title1")[0].innerText = title1[titleNumber];
        $(".title2")[0].innerText = title2[titleNumber];
        $("#content-financing").css("background-image", title_background[titleNumber]);
});
$("#banner2").click(function(){
    titleNumber = (titleNumber + 1) % 3;
    $(".title1")[0].innerText = title1[titleNumber];
    $(".title2")[0].innerText = title2[titleNumber];
    $("#content-financing").css("background-image", title_background[titleNumber]);
});

