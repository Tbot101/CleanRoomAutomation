/* function changeCSS(cssFile, cssLinkIndex) {

    var oldlink = document.getElementsByTagName("link").item(cssLinkIndex);

    var newlink = document.createElement("link");
    newlink.setAttribute("rel", "stylesheet");
    newlink.setAttribute("type", "text/css");
    newlink.setAttribute("href", cssFile);

    document.getElementsByTagName("head").item(0).replaceChild(newlink, oldlink);
} */


function room1function(){
	var x = document.getElementsByClassName("room1");
	var i;
	for (i = 0; i < x.length; i++) {
	x[i].style.display = "block";
	}
	var y = document.getElementsByClassName("room2");
	var j;
	for (j = 0; j < y.length; j++) {
	y[j].style.display = "none";
	}
	var z = document.getElementsByClassName("room3");
	var k;
	for (k = 0; k < z.length; k++) {
	z[k].style.display = "none";
	}
	const room1button = document.getElementById("room1styles");
	room1button.style.outline = "1px solid #0AFFEF";
	const room2button = document.getElementById("room2styles");
	room2button.style.outline = "none";
	const room3button = document.getElementById("room3styles");
	room3button.style.outline = "none";
	//var value = document.getElementById("room1fanslider").value;
	document.cookie = "room=room1;path=/;"

}

function room2function(){
	var x = document.getElementsByClassName("room1");
	var i;
	for (i = 0; i < x.length; i++) {
	x[i].style.display = "none";
	}
	var y = document.getElementsByClassName("room2");
	var j;
	for (j = 0; j < y.length; j++) {
	y[j].style.display = "block";
	}
	var z = document.getElementsByClassName("room3");
	var k;
	for (k = 0; k < z.length; k++) {
	z[k].style.display = "none";
	}
	const room1button = document.getElementById("room1styles");
	room1button.style.outline = "none";
	const room2button = document.getElementById("room2styles");
	room2button.style.outline = "1px solid #0AFFEF";
	const room3button = document.getElementById("room3styles");
	room3button.style.outline = "none";
	//var value = document.getElementById("room2fanslider").value;
	document.cookie = "room=room2;path=/;"

}

function room3function(){
	var x = document.getElementsByClassName("room1");
	var i;
	for (i = 0; i < x.length; i++) {
	x[i].style.display = "none";
	}
	var y = document.getElementsByClassName("room2");
	var j;
	for (j = 0; j < y.length; j++) {
	y[j].style.display = "none";
	}
	var z = document.getElementsByClassName("room3");
	var k;
	for (k = 0; k < z.length; k++) {
	z[k].style.display = "block";
	}
	const room1button = document.getElementById("room1styles");
	room1button.style.outline = "none";
	const room2button = document.getElementById("room2styles");
	room2button.style.outline = "none";
	const room3button = document.getElementById("room3styles");
	room3button.style.outline = "1px solid #0AFFEF";
	//var value = document.getElementById("room3fanslider").value;
	document.cookie = "room=room3;path=/;"

}


var condVal = {
	/*"mode1": "AUTO",
	"tempVal1": 22,
	"fanVal1": "FANLOW"
	"mode2": "AUTO",
	"tempVal2": 22,
	"fanVal2": "FANLOW"*/
	"mode3": "AUTO",
	"tempVal3": 22,
	"fanVal3": "FANLOW"
};

const roomXfunction = {
	"room1": room1function,
	"room2": room2function,
	"room3": room3function,
};

const onPageLoad = () => {
	const url = document.cookie;
	Object.entries(roomXfunction).forEach(([key, value]) => {
		if (url.includes(key)) {
			value();
		}
	});
};
onPageLoad();

function buttonChange(sign, number) {
	var slider = document.getElementById("room"+number+"fanslider");
	slider.value = parseInt(slider.value) + parseInt(sign) * 10;
}

function setroomValue(number){
			var roomvalue = document.getElementById("room"+number+"fanslider").value;
			localStorage.setItem("room"+number+"_value", roomvalue);
	}

	function getroomValue(number){
			if (localStorage.getItem("room"+number+"_value") === null) {// Check if there is selected date.
						return "0";
			}
			return localStorage.getItem("room"+number+"_value");
	}

/* function fanloop(){
	var i;
	for (i=0; i < 4; i++){
		document.getElementById("room"+i+"fanslider").value = getroomValue(i);
		};
	};

fanloop(); */
document.getElementById("room1fanslider").value = getroomValue(1);
document.getElementById("room2fanslider").value = getroomValue(2);
document.getElementById("room3fanslider").value = getroomValue(3);
const airConEdit = (room, dir) => {
	let val = parseInt(document.getElementById(`room${room}settemp`).value);
	val += dir;
	val = Math.max(Math.min(30, val), 19);
	document.getElementById(`room${room}settemp`).value = val;
};



$(document).ready(function() {
	// $('.qty-minus').click(function () {
	// 	var $input = $(this).parent().find('input');
	// 	var count = parseInt($input.val()) - parseInt(1);
	// 	count = count < 19 ? 19 : count;
	// 	$input.val(count);
	// 	$input.change();
	// });
	// $('.qty-plus').click(function () {
	// 	var $input = $(this).parent().find('input');
	// 	var count = (parseInt($input.val()) + parseInt(1));
	// 	count = count > 30 ? 30 : count;
	// 	$input.val(count);
	// 	$input.change();
	// });

		// Get click event, assign button to var, and get values from that var
	$('.airconmode button').on('click', function() {
		$('.airconmode button').removeClass('airconmodeclicked')
			$(this).addClass('airconmodeclicked');

		var thisBtn = $(this);
		thisBtn.addClass('active').siblings().removeClass('active');
		localStorage.setItem("airconmodebutton", $(this).attr('id'));
	});
});

function settempvalue(number){
			var tempvalue = document.getElementById("room"+number+"settemp").value;
			localStorage.setItem("room"+number+"_temp", tempvalue);
	}

	function gettempvalue(number){
			if (localStorage.getItem("room"+number+"_temp") === null) {// Check if there is selected date.
						return "22";
			}
			return localStorage.getItem("room"+number+"_temp");
	}
document.addEventListener('DOMContentLoaded', function() {
	/*document.getElementById("room1settemp").value = gettempvalue(1);
	document.getElementById("room2settemp").value = gettempvalue(2);*/
	document.getElementById("room3settemp").value = gettempvalue(3);
}, false);


function fanlow(number){
	var fanspeedimages = document.getElementById("fanspeedimageroom"+number)
	fanspeedimages.src="/static/images/fanlow.png";
};

function fanhigh(number){
	var fanspeedimages = document.getElementById("fanspeedimageroom"+number)
	fanspeedimages.src="/static/images/fanhigh.png";
};

function setfanvalue(number){
			var fansrc = document.getElementById("fanspeedimageroom"+number).src;
			localStorage.setItem("room"+number+"_fan", fansrc);
	}

	function getfanvalue(number){
			if (localStorage.getItem("room"+number+"_fan") === null) {// Check if there is selected date.
						return "/static/images/fanlow.png";
			}
			return localStorage.getItem("room"+number+"_fan");
	}

/*document.getElementById("fanspeedimageroom1").src = getfanvalue(1);
document.getElementById("fanspeedimageroom2").src = getfanvalue(2);*/
document.getElementById("fanspeedimageroom3").src = getfanvalue(3);

function setairconvalue(number){
			var airconsrc = document.getElementById("airconmodebutton"+number);
	localStorage.setItem("room"+number+"_aircon", airconsrc);
	}

	function getairconvalue(){
			return localStorage.getItem("airconmodebutton");
	}

var localstorageaircon = getairconvalue();
document.getElementById(localstorageaircon).classList.add('airconmodeclicked');


function getairconsignal(number){
	var temp = document.getElementById("room"+number+"settemp");
	var tempvalue = temp.value;
	condVal["tempVal"+number] = tempvalue;

	var fan = document.getElementById("fanspeedimageroom"+number);
	var fansrc = fan.src;
	if (fansrc.includes("fanlow")){
		var fanvalue = "FANLOW";
	}
	else{
		var fanvalue = "FANHIGH";
	}
	condVal["fanVal"+number] = fanvalue;

	console.log("ON_"+condVal["mode"+number]+"_"+condVal["fanVal"+number]+"_"+condVal["tempVal"+number]);
};

$('.airconmode button').on('click', function() {
	var thisBtn = $(this);
	condVal["mode3"] = thisBtn.val();
	console.log("ON_"+condVal["mode3"]+"_"+condVal["fanVal3"]+"_"+condVal["tempVal3"]);
});


/*
var roomXfunction = {
	1: room1function,
	2: room2function,
	3: room3function
};

let onPageLoad = () =>
{
	Object.entries(roomXfunction).forEach(([key, value]) => {
	if (window.location.href.includes(key)) {
		roomXfunction[value]();
};
*/

/*
let body = document.body;

let room1Btn = document.getElementById('room1sensor');
let room2Btn = document.getElementById('room2sensor');
let room3Btn = document.getElementById('room3sensor');

room1Btn.addEventListener('click', () => {
	body.classList.add('room1');
	body.classList.remove('room2');
	body.classList.remove('room3');
});

room2Btn.addEventListener('click', () => {
	body.classList.remove('room1');
	body.classList.add('room2');
	body.classList.remove('room3');
});

room3Btn.addEventListener('click', () => {
	body.classList.remove('room1');
	body.classList.remove('room2');
	body.classList.add('room3');
});
*/
/*
function room1function(){
    document.getElementsByClassName("room1").style.display = "block";
    document.getElementsByClassName("room2").style.display = "none";
    document.getElementsByClassName("room3").style.display = "none";
}
room1function()

function room2function(){
    document.getElementsByClassName("room1").style.display = "none";
    document.getElementsByClassName("room2").style.display = "block";
    document.getElementsByClassName("room3").style.display = "none";
}
room2function()

function room3function(){
    document.getElementsByClassName("room1").style.display = "none";
    document.getElementsByClassName("room2").style.display = "none";
    document.getElementsByClassName("room3").style.display = "block";
}
room3function()


document.getElementById("aircon_on_button").onclick = function(){
	document.getElementById("aircon_on_button").style = '#0AFFEF';
    document.getElementById("aircon_off_button").style = '#8A959D';
    document.getElementById("airconimage").src = '/static/images/airconon.png';
}
document.getElementById("aircon_off_button").onclick = function(){
	document.getElementById("aircon_on_button").style = '#8A959D';
    document.getElementById("aircon_off_button").style = '#E32626';
    document.getElementById("airconimage").src = '/static/images/airconoff.png';
}

*/
