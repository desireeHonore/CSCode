//declaring additional variables
let x = 300;
let y = 350;
let xSpeed = 2, ySpeed = -1;
let size = 90;
let isGrowing = true;
let redVal = 0, greenVal = 0;
const sunR = 30;

function setup() {
  createCanvas(600, 400);
  noStroke();
}

function draw() {
  redVal = min(redVal + 0.8, 220);
  greenVal = min(greenVal + 0.15, 60);

  background(redVal, greenVal, 0);

//sun
  fill(255, 135, 5, 60);
  circle(x, y, size * 2);
  fill(255, 100, 0, 100);
  circle(x, y, size * 1.56);

//mountain drawing
  fill(110, 50, 18);
  triangle(200, 400, 520, 253, 800, 400);
  fill(110, 95, 20);
  triangle(200, 400, 520, 253, 350, 400);

  fill(150, 75, 0);
  triangle(-100, 400, 150, 200, 400, 400);
  fill(100, 50, 12);
  triangle(-100, 400, 150, 200, 0, 400);

  fill(150, 100, 0);
  triangle(200, 400, 450, 250, 800, 400);
  fill(120, 80, 50);
  triangle(200, 400, 450, 250, 300, 400);

//speed/movement of sun
  x += xSpeed;
  y += ySpeed;

  if (x >= width - sunR || x <= sunR) xSpeed *= -1;
  if (y >= height - sunR || y <= sunR) ySpeed *= -1;

//sun pulsating
  if (isGrowing) size++;
  else size--;
  if (size < 40) isGrowing = true;
  if (size > 110) isGrowing = false;
}

function mousePressed() {
  isGrowing = !isGrowing;
  xSpeed = (mouseX - x) * 0.05;
  ySpeed = (mouseY - y) * 0.05;
}
