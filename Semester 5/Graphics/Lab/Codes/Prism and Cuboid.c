#include <stdio.h>
#include <stdarg.h>
#include <math.h>
#define GL_GLEXT_PROTOTYPES
#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif
// ----------------------------------------------------------
// Function Prototypes
// ----------------------------------------------------------
void display();
void specialKeys();
 
// ----------------------------------------------------------
// Global Variables
// ----------------------------------------------------------
double rotate_y=0; 
double rotate_x=0;
double scale_up=1;
double scale_down=1;
int cubeSelected=1;
int triangleSelected=1;
// ----------------------------------------------------------
// display() Callback function
// ----------------------------------------------------------
void display(){
 
  //  Clear screen and Z-buffer
  glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
 
  // Reset transformations
  glMatrixMode(GL_PROJECTION);
  if(cubeSelected){
  glLoadIdentity();
 gluOrtho2D(-8, 8, -8, 8);
 glTranslatef(5.0f, 0.0f, 0.0f);
  // Other Transformations
  // glTranslatef( 0.1, 0.0, 0.0 );      // Not included
  // glRotatef( 180, 0.0, 1.0, 0.0 );    // Not included
 
  // Rotate when user changes rotate_x and rotate_y
  glPointSize(1.0);
  glScaled(scale_up,scale_up,scale_up);
  glRotatef( rotate_x, 1.0, 0.0, 0.0 );
  glRotatef( rotate_y, 0.0, 1.0, 0.0 );
 
  // Other Transformations
  // glScalef( 2.0, 2.0, 0.0 );          // Not included
 
  //Multi-colored side - FRONT
  glBegin(GL_POLYGON);
 
  glColor3f( 1.0, 1.0, 0.0 );     
  glVertex3f(  0.5, -0.5, -0.5 );          
  glVertex3f(  0.5,  0.5, -0.5 );           
  glVertex3f( -0.5,  0.5, -0.5 );          
  glVertex3f( -0.5, -0.5, -0.5 );      
 
  glEnd();
 
  // White side - BACK
  glBegin(GL_POLYGON);
  glColor3f(   1.0,  1.0, 1.0 );
  glVertex3f(  0.5, -0.5, 0.5 );
  glVertex3f(  0.5,  0.5, 0.5 );
  glVertex3f( -0.5,  0.5, 0.5 );
  glVertex3f( -0.5, -0.5, 0.5 );
  glEnd();
 
  // Purple side - RIGHT
  glBegin(GL_POLYGON);
  glColor3f(  1.0,  0.0,  1.0 );
  glVertex3f( 0.5, -0.5, -0.5 );
  glVertex3f( 0.5,  0.5, -0.5 );
  glVertex3f( 0.5,  0.5,  0.5 );
  glVertex3f( 0.5, -0.5,  0.5 );
  glEnd();
 
  // Green side - LEFT
  glBegin(GL_POLYGON);
  glColor3f(   0.0,  1.0,  0.0 );
  glVertex3f( -0.5, -0.5,  0.5 );
  glVertex3f( -0.5,  0.5,  0.5 );
  glVertex3f( -0.5,  0.5, -0.5 );
  glVertex3f( -0.5, -0.5, -0.5 );
  glEnd();
 
  // Blue side - TOP
  glBegin(GL_POLYGON);
  glColor3f(   0.0,  0.0,  1.0 );
  glVertex3f(  0.5,  0.5,  0.5 );
  glVertex3f(  0.5,  0.5, -0.5 );
  glVertex3f( -0.5,  0.5, -0.5 );
  glVertex3f( -0.5,  0.5,  0.5 );
  glEnd();
 
  // Red side - BOTTOM
  glBegin(GL_POLYGON);
  glColor3f(   1.0,  0.0,  0.0 );
  glVertex3f(  0.5, -0.5, -0.5 );
  glVertex3f(  0.5, -0.5,  0.5 );
  glVertex3f( -0.5, -0.5,  0.5 );
  glVertex3f( -0.5, -0.5, -0.5 );
  glEnd();
}
if(triangleSelected){
glLoadIdentity();
 gluOrtho2D(-8, 8, -8, 8);
 glTranslatef(-5.0f, 0.0f, 0.0f);
  // Other Transformations
  // glTranslatef( 0.1, 0.0, 0.0 );      // Not included
  // glRotatef( 180, 0.0, 1.0, 0.0 );    // Not included
 
  // Rotate when user changes rotate_x and rotate_y
  glPointSize(1.0);
  glScaled(scale_up,scale_up,scale_up);
  glRotatef( rotate_x, 1.0, 0.0, 0.0 );
  glRotatef( rotate_y, 0.0, 1.0, 0.0 );
 glBegin( GL_TRIANGLES );
glColor3f( 0.5, 0.0, 0.0 );
 glVertex3f( 0.0, 0.5, 0.0 );
 glVertex3f( -0.5, -0.5, 0.5 );
 glVertex3f( 0.5, -0.5, 0.5);
glEnd();
 glBegin( GL_TRIANGLES );
 glColor3f( 0.0, 0.5, 0.0 );
 glVertex3f( 0.0, 0.5, 0.0);
 glVertex3f( -0.5, -0.5, 0.5);
 glVertex3f( 0.0, -0.5, -0.5);
glEnd();
 glBegin( GL_TRIANGLES );
 glColor3f( 0.0, 0.0, 0.5 );
glVertex3f( 0.0, 0.5, 0.0);
 glVertex3f( 0.0, -0.5, -0.5);
 glVertex3f( 0.5, -0.5, 0.5);
glEnd();
 glBegin( GL_TRIANGLES );
 glColor3f( 0.5, 0.0, 0.5 );
 glVertex3f( -0.5, -0.5, 0.5);
 glVertex3f( 0.0, -0.5, -0.5);
 glVertex3f( 0.5, -0.5, 0.5);
glEnd();
}
  glFlush();
  glutSwapBuffers();
 
}
 
// ----------------------------------------------------------
// specialKeys() Callback Function
// ----------------------------------------------------------
void specialKeys( int key, int x, int y ) {
 
 	char alpha='s';
 	int ascii=alpha;
  //  Right arrow - increase rotation by 5 degree
  if (key == GLUT_KEY_RIGHT)
    rotate_y += 5;
 
  //  Left arrow - decrease rotation by 5 degree
  else if (key == GLUT_KEY_LEFT)
    rotate_y -= 5;
 
  else if (key == GLUT_KEY_UP)
    rotate_x += 5;
 
  else if (key == GLUT_KEY_DOWN)
    rotate_x -= 5;
  else if (key == GLUT_KEY_PAGE_UP)
  	scale_up +=0.25;
  else if (key == GLUT_KEY_PAGE_DOWN)
  	scale_up -=0.25;
  //  Request display update
  glutPostRedisplay();
 
}
void mousePressed(int button, int state, int x, int y) {
if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
	if(cubeSelected==1){
		cubeSelected=0;
	}else{
		cubeSelected=1;
	}
	
}
if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
if(triangleSelected==1){
		triangleSelected=0;
	}else{
		triangleSelected=1;
	}
}
}
// ----------------------------------------------------------
// main() function
// ----------------------------------------------------------
int main(int argc, char* argv[]){
 
  glutInit(&argc,argv);
 
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
 
  glutInitWindowSize (1000, 1000);                  
  
  glutCreateWindow("Cuboid");
 
  //  Enable Z-buffer depth test
  glEnable(GL_DEPTH_TEST);
 
  // Callback functions
  glutDisplayFunc(display);
  glutSpecialFunc(specialKeys);
 
  //  Pass control to GLUT for events
  glutMainLoop();
 
  //  Return to OS
  return 0;
 
}