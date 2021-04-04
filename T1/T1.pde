void setup(){
 size(500,500); 
}

void draw(){
  background(200);
  int margin = 20;
  float x = 0;
  float y = 0;
  float n = round(map(mouseX, 0,   width, 3, 12));
  float a = TWO_PI/n;
  
  float raio_externo = (width/2) - margin;
  float raio_interno = raio_externo * map(mouseY, 0, width, 0.3, 0.8);
  
  translate(width/2, height/2);
  
  beginShape();
  for(float i=0; i< TWO_PI;i+=a){
    float sx = x + raio_interno * cos(i);
    float sy = y + raio_interno * sin(i);
    
    vertex(sx,sy);
    
    sx = x + cos(i+(a/2)) * raio_externo;
    sy = y+ sin(i+(a/2)) * raio_externo;
    
    vertex(sx,sy);
  }
  endShape();
}
