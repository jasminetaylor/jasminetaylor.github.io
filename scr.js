function Loader(circles) {
  this.circles = circles;
}

function Circle(pos, radius, angle) {
  this.pos = pos;
  this.radius = radius;
  this.point = {
    x: 0, y: 0,
    speed: 0.04,
    radius: 10,
    angle: angle
  };
}

Circle.prototype.update = function(ctx, circles) {	
  this.updatePoint(circles);

  ctx.save();
  ctx.translate(this.point.x, this.point.y);
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.arc(0, 0, this.point.radius, 0, Math.PI * 2, true);
  ctx.closePath();
  //ctx.fill();
  ctx.restore();
  this.render(ctx);
};

Circle.prototype.updatePoint = function(circles) {
  var self = this;
  this.point.x = this.pos.x + Math.sin(this.point.angle) * this.radius;
  this.point.y = this.pos.y + Math.cos(this.point.angle) * this.radius;
  circles.forEach(function(next) {
    ctx.save();
    ctx.lineWidth = 0.25;
    ctx.strokeStyle = '#fff';
    ctx.beginPath();
    ctx.moveTo(self.point.x, self.point.y);
    ctx.lineTo(next.point.x, next.point.y);
    ctx.closePath();
    ctx.stroke();
    ctx.restore();
  });
  this.point.angle += this.point.speed;
};

Circle.prototype.render = function(ctx) {
  ctx.save();
  ctx.lineWidth = 0.8;
  ctx.strokeStyle = '#555';
  ctx.translate(this.pos.x, this.pos.y);
  ctx.beginPath();
  ctx.arc(0, 0, this.radius, 0, Math.PI * 2, true);
  ctx.closePath();
  ctx.stroke();
  ctx.restore();
}

var canvas = document.createElement('canvas'),
    ctx = canvas.getContext('2d'),

    width = window.innerWidth,
    height = window.innerHeight,

    circles;

function init() {
  setUpCanvas();
  circles = generateCircles(12, height / 4);
  render();
}

function setUpCanvas() {
  document.body.appendChild(canvas);
  canvas.width = width;
  canvas.height = height;
  ctx.fillStyle = '#111';
}

function generateCircles(num, range) {
  circles = [];
  var i = 0;
  for (var angle = 0; angle < Math.PI * 2; angle += (Math.PI * 2) / num) {
    var circle = new Circle(
      { x: width / 2 + Math.sin(angle) * range, y: height / 2 + Math.cos(angle) * range },
      height / 20, angle + i
    );
    i += 2;
    circles.push(circle);
  }
  return circles;
}

function render() {
  window.requestAnimationFrame(render);
  ctx.fillRect(0, 0, width, height);
  circles.forEach(renderCircle);
}

function renderCircle(circle) {
  circle.update(ctx, circles);
}

window.onload = init;