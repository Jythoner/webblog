var theHeight = 320;
// Initailization
// ---------------------------------------------------
// canvas ready
var canvas = document.getElementsByTagName('canvas')[0];
var points = [], width = canvas.width, height = canvas.height;

if (canvas && canvas.getContext) {
	var context = canvas.getContext("2d");
	Initialize()
}
// Initialize
function Initialize() {
	canvas.addEventListener("mousemove", MouseMove, false);
	window.addEventListener("resize", ResizeCanvas, false);
	setInterval(Update, 10);
	ResizeCanvas()
}

// Do not forget about resizing
function ResizeCanvas(e) {
	canvas.width = window.innerWidth * 0.97;
	canvas.height = theHeight;
}

// Update canvas
function Update(e) {
	// reay to paint
	context.clearRect(0, 0, canvas.width, canvas.height);
	var t, n, r,
	i = new Array(points.length);
	for (n = 0; n < particles.length; n++) {
		i[n] = new Array(particles.length);
		for (r = 0; r < particles.length; r++) {
			i[n][r] = 0
		}
	}
	// Paint and paint
	for (var n = 0; n < particles.length; n++) {
		particles[n].x += particles[n].vx;
		particles[n].y += particles[n].vy;

		reflush(n);

		context.strokeStyle = particles[n].color;
		context.beginPath();
		var o = DistanceBetween(mouse, particles[n]);
		o = Math.max(Math.min(6 - o / 10, 5), 1);
		context.beginPath();
		context.arc(particles[n].x, particles[n].y, particles[n].size * o, 0, Math.PI * 2, true);
		context.fillStyle = particles[n].color;
		context.closePath();
		context.fill()
	}
}

// Deposition
// ---------------------------------------------------
var particles = [];

// Create
var dots = Math.floor(window.innerWidth * 0.97 / 10);
for (var i = 0; i < dots; i++) {
	particles.push({
		// randomize postition
		x : Math.random() * window.innerWidth * 0.97,
		y : Math.random() * theHeight,
		// velocity
		vx : (Math.random() - 0.5) * 1.2,
		vy : (Math.random() - 0.5) * 1.2,
		// size & color
		size : (Math.random() + 0.5) * 2.5,
		color : randomColor()
	})
}

// Reflush
var reflush = function (index) {
	var x = particles[index].x, y = particles[index].y;
	
	var inBoundary = (x >= 0 && y >=0) && (x <= canvas.width && y <= canvas.height);
	if (inBoundary) return;

	// infinite x range
	if (x > canvas.width) particles[index].x = 0;
		else if (x < 0) particles[index].x = canvas.width;
 
	// infinite y range
  if (y > canvas.height) particles[index].y = 0;
  else if (y < 0) particles[index].y = canvas.height;

  // disguise
	particles[index].color = randomColor();
	particles[index].size = (Math.random() + 0.5) * 2.5;

	return;
}

// Mouse move
// ---------------------------------------------------
var mouse = {
	x : canvas.width * 0.5,
	y : canvas.height * 0.5
};
function MouseMove(e) {
	mouse.x = e.layerX;
	mouse.y = e.layerY
}

function DistanceBetween(e, t) {
	var n = t.x - e.x;
	var r = t.y - e.y;
	return Math.sqrt(n * n + r * r);
}

// Color Related
// ---------------------------------------------------
// Randomize color
function randomColor() {
	var rr = Math.ceil((Math.random()) * 255),
		rg = Math.ceil((Math.random()) * 255),
		rb = Math.ceil((Math.random()) * 255);
	return convertRGB(rr, rg, rb);
}
// Color conversion from RGB to HEX
function convertRGB(r, g, b) {
	var colorRef = function (num) {
		var res = num.toString(16).toUpperCase();
		return (res.length == 1) ? (res + res) : res;
	}
	var output = "#" + colorRef(r) + colorRef(g) + colorRef(b);
	return output;
}