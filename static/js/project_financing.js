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
var title_background = ["url(../static/img/project/0.jpg)", "url(../static/img/project/1.jpg)", "url(../static/img/project/2.jpg)"];
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

//筛选菜单逻辑部分
var current_menu = {valid:false};
function showMenu(opt_id, menu_id)
{
	hideMenu('#quanbu');
	hideMenu('#lingyu');
    $(menu_id).css('display','block');
    $(menu_id).css('left',$(opt_id).position().left);
    $(menu_id).css('top',$(opt_id).position().top+$(opt_id).height()+4);
    current_menu = {
    	valid:true,
    	opt:opt_id,
    	menu:menu_id,
    	left:$(opt_id).position().left,
	    top1:$(opt_id).position().top,
	    top2:$(opt_id).position().top + $(opt_id).height() + 4,
	    bottom:$(opt_id).position().top + $(opt_id).height() + 4 + $(menu_id).height(),
	    right1:$(opt_id).position().left + $(opt_id).width(),
	    right2:$(opt_id).position().left + $(menu_id).width()
	};
}

function hideMenu(menu_id)
{
	$(menu_id).css('display','none');
	current_menu.valid=false;
}

$('#opt1').mouseover(function(){
    showMenu('#opt1','#quanbu');
});

$('#opt2').mouseover(function(){
    showMenu('#opt2','#lingyu');
});

function atCurrentMenu(x, y)
{
	with(current_menu)
	{
		if (x<left||x>right2||y<top1||y>bottom||(x>right1&&y<top2))
			return false;
		return true;
	}
}

document.addEventListener('mousemove',function(e)
{
	if (!current_menu.valid)
		return;
	if (!atCurrentMenu(e.x, e.y))
	{
		hideMenu(current_menu.menu);
	}
});

//$(".w300").click(function(){;});