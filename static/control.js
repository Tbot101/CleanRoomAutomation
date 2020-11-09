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


.on1 {
	color:#0AFFEF;
}
.on0{
	color:#8A959D;
}

.off1{
	color:#8A959D;
}
.0ff0{
	color:#E32626;
}
*/
