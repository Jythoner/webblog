// Bind polyfill
// --------------------------------------------
if (!Function.prototype.bind) {
  Function.prototype.bind = function (oThis) {
    if (typeof this !== "function") {
      // closest thing possible to the ECMAScript 5 internal IsCallable function
      throw new TypeError("Function.prototype.bind - what is trying to be bound is not callable");
    }

    var aArgs = Array.prototype.slice.call(arguments, 1), 
        fToBind = this, 
        fNOP = function () {},
        fBound = function () {
          return fToBind.apply(this instanceof fNOP && oThis
                                 ? this
                                 : oThis || window,
                               aArgs.concat(Array.prototype.slice.call(arguments)));
        };

    fNOP.prototype = this.prototype;
    fBound.prototype = new fNOP();

    return fBound;
  };
}
// --------------------------------------------

var Floater = function (config) {
	// Initialize param defaults
	var config = config || {};
	this.element = config.element || document.getElementById('header-title');
	this.freq = config.freq || 10;
	this.range = config.range || 3;
	this.unit = config.unit || "px";
	this.iPos = config.iPos || 0;
	this.step = config.step || 0.5;
	this.pointer = 0;
}

Floater.prototype = {
	constructor: Floater,
	
	init: function () {
		setInterval(this.tween.bind(this), this.freq);
		// requestAnimationFrame(this.tween.bind(this))
	},

	tween: function () {
		this.pointer = (this.pointer > Math.PI * 2) ? 0 : (this.pointer + this.step);
		// console.log(this.pointer)
		var range = Math.sin(this.pointer) * this.range;
		this.element.style.top = (this.iPos + range) + this.unit;
	}
}

new Floater({
	element: document.getElementById('logo-wrap'),
	freq: 60,
	range: 10,
	unit: null,
	iPos: null,
	step: 0.1
}).init()
new Floater({
	element: document.getElementById('subtitle-wrap'),
	freq: 60,
	range: 8,
	unit: null,
	iPos: null,
	step: 0.1
}).init()