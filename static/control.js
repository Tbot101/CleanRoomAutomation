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
	roomHideBtn.style.border = "none";
	const roomShowBtn = document.getElementById(`room${roomX}styles`);
	roomShowBtn.style.border = "1px solid #0AFFEF";
	document.cookie = `room=room${roomX};path=/;`
	curRoom = roomX;
}
var condVal = {}
for (let i = 1; i<= numRoom; i++){
	condVal.push = ({
		key: "mode"+i,
		value: "COOL",
		key: "tempVal"+i,
		value: 22,
		key: "fanVal"+i,
		value: "FANLOW",
		});
	}
console.log(condVal);

const setfanSlider = (val) => {
	try {
		document.getElementById(`room${val}fanslider`).value = getroomValue(val);
	} catch (e) {
		console.log(`Room${val} fan is off.`);
	}
}

function buttonChange(sign, room) {
	var slider = document.getElementById("room"+room+"fanslider");
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

function airconmodeformat(room, number){
	var children = document.getElementById("airconmode"+room).children;
	var temp = document.getElementById("settempwrapper"+room);
	temp.style.visibility = 'visible';
	for (var i=0; i<children.length; i++){
		children[i].style.color="#8A959D";
	}
	var airconbutton = document.getElementById("airconmodebutton"+number);
	airconbutton.style.color = "#0AFFEF";
	if(airconbutton.id.charAt(airconbutton.id.length-1) == 3){
		temp.style.visibility = 'hidden';
		}
}


function setairconvalue(room, number){
	var airconsrc = document.getElementById("airconmodebutton"+number).id;
	localStorage.setItem("room"+room+"_aircon", airconsrc);
}

function getairconvalue(number){
		if (localStorage.getItem("room"+number+"_aircon") === null) {// Check if there is selected date.
					return "airconmodebutton"+number+"1";
		}
		return localStorage.getItem("room"+number+"_aircon");
}

function sendControl(room, forName) {
	var r = new XMLHttpRequest();
	r.open("GET","/aircon/" + room + "/" + forName);
	r.setRequestHeader('Cache-Control', 'no-cache');
	r.send();
}

function airconoff(number){
	sendControl("Room"+number, "OFF")
}

function airconon(number){
	
	var temp = gettempvalue(number);
	condVal["tempVal"+number] = temp;
	
	var fan = getfanvalue(number);
	if (fan.includes("fanlow")){
		var fanvalue = "FANLOW";
	}
	else{
		var fanvalue = "FANHIGH";
	}
	condVal["fanVal"+number] = fanvalue;
	
	var ac = getairconvalue(number);
	var acsrc = "";
	if(ac.charAt(ac.length-1) == 1){
		acsrc = "COOL";
	}if(ac.charAt(ac.length-1) == 2){
		acsrc = "DRY";
	}else{
		acsrc = "FAN";
	}
	
	condVal["mode"+number] = acsrc;
	
	sendControl("Room"+number, "ON_"+condVal["mode"+number]+"_"+condVal["fanVal"+number]+"_"+condVal["tempVal"+number]);
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
	
	var aircon = document.getElementById(getairconvalue(number));
	var airconsrc = aircon.value;
	condVal["mode"+number] = airconsrc;
	sendControl("Room"+number, "ON_"+condVal["mode"+number]+"_"+condVal["fanVal"+number]+"_"+condVal["tempVal"+number]);
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
		for (let i = 1; i <= numRoom; i++){
			document.getElementById("room"+i+"settemp").value = gettempvalue(i);
			document.getElementById("fanspeedimageroom"+i).src = getfanvalue(i);
			document.getElementById(getairconvalue(i)).style.color="#0AFFEF";
			if(getairconvalue(i).charAt(getairconvalue(i).length-1) == 3){
				var temp = document.getElementById("settempwrapper"+i);
				temp.style.visibility = 'hidden';
				}
			};
	} catch (e) {
		console.log(`Room3 air con is off`);
	}
});
