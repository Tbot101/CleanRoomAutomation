const numRoom = 3;
let curRoom = 1;

const setRoom = (roomX) => {
	let roomHide = document.getElementsByClassName(`room${curRoom}`);
	let roomShow = document.getElementsByClassName(`room${roomX}`);
	for (let i of roomHide) {
		i.style.display = "none";
	}
	for (let i of roomShow) {
		i.style.display = "block";
	}
	const roomHideBtn = document.getElementById(`room${curRoom}styles`);
	roomHideBtn.style.outline = "none";
	const roomShowBtn = document.getElementById(`room${roomX}styles`);
	roomShowBtn.style.outline = "1px solid #0AFFEF";
	document.cookie = `room=room${roomX};path=/;`
	curRoom = roomX;
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

const setfanSlider = (val) => {
	try {
		document.getElementById(`room${val}fanslider`).value = getroomValue(val);
	} catch (e) {
		console.log(`Room${val} fan is off.`);
	}
}

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

const airConEdit = (room, dir) => {
	let val = parseInt(document.getElementById(`room${room}settemp`).value);
	val += dir;
	val = Math.max(Math.min(30, val), 19);
	document.getElementById(`room${room}settemp`).value = val;
};

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

function setairconvalue(number){
	var airconsrc = document.getElementById("airconmodebutton"+number);
	localStorage.setItem("room"+number+"_aircon", airconsrc);
}

function getairconvalue(){
		return localStorage.getItem("airconmodebutton");
}


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

// Execute after page loaded
document.addEventListener("DOMContentLoaded", () => {
	// read cookie
	const url = document.cookie;
	setRoom(url.slice(url.length-1));
	// read fan
	for (let i = 1; i <= numRoom; ++i) {
		setfanSlider(i)
	}
	try {
		// Warning: hardcode to room 3 now, might need changes!
		document.getElementById("room3settemp").value = gettempvalue(3);
		document.getElementById("fanspeedimageroom3").src = getfanvalue(3);
		document.getElementById(getairconvalue()).classList.add('airconmodeclicked');
	} catch (e) {
		console.log(`Room3 air con is off`);
	}
	$('.airconmode button').on('click', function() {
		$('.airconmode button').removeClass('airconmodeclicked');
		$(this).addClass('airconmodeclicked');

		var thisBtn = $(this);
		thisBtn.addClass('active').siblings().removeClass('active');
		localStorage.setItem("airconmodebutton", $(this).attr('id'));
		condVal["mode3"] = thisBtn.val();
	});
});
