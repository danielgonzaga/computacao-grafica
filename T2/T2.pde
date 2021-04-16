float pl_x = 100;
float pl_y = 600;
float p2_x = 300;
float p2_y = 200;
float p3_x = 500;
float p3_y = 600;
float p4_x = 700;
float p4_y = 200;
boolean p2_clicked = false;
boolean p3_clicked = false;

void setup()
{
  size(750, 700);
}

void draw() {
  background(200);
  
  if(p2_clicked)
  {
    p2_x = mouseX;
    p2_y = mouseY;
  }
  else if(p3_clicked)
  {
    p3_x = mouseX;
    p3_y = mouseY;
  }
  
  noFill();
  beginShape();
  for(float i = 0; i <= 1; i += 0.01) {
    float ax = pl_x + i*(p2_x-pl_x);
    float ay = pl_y + i*(p2_y-pl_y);
    float bx = p2_x + i*(p3_x-p2_x);
    float by = p2_y + i*(p3_y-p2_y);
    float cx = p3_x + i*(p4_x-p3_x);
    float cy = p3_y + i*(p4_y-p3_y);
    float dx = ax + i*(bx-ax);
    float dy = ay + i*(by-ay);
    float ex = bx + i*(cx-bx);
    float ey = by + i*(cy-by);
    float fx = dx + i*(ex-dx);
    float fy = dy + i*(ey-dy);
    vertex(fx, fy);
  }
  endShape();
  
  fill(0, 0, 0);
  
  circle(pl_x, pl_y, 5);
  circle(p2_x, p2_y, 5);
  circle(p3_x, p3_y, 5);
  circle(p4_x, p4_y, 5);
}

void mousePressed()
{
    if(dist(p2_x, p2_y, mouseX, mouseY) < 10)
    {
      p2_clicked = true;
    }
    if(dist(p3_x, p3_y, mouseX, mouseY) < 10)
    {
      p3_clicked = true;
    }
  
}

void mouseReleased()
{
  p2_clicked = false;
  p3_clicked = false;
}
