#include <stdio.h>
#include <GL/gl.h>
#include <GL/glut.h>
#include <GL/glu.h>
#include <math.h>
/* Make point structure  */
struct point{
	float x,y;
};

int X1=0,Y1=0,X2=0,Y2=100,X3=200,Y3=0;
int rx=0,ry=0,angle=117; //rotation
float xscale=1,yscale=1.788; //scaling

void plot(int x, int y)
{
	glBegin(GL_POINTS);
	glVertex2i(x,y);
	glEnd();
}

void myInit(void)
{
	glClearColor(1.0, 1.0, 1.0, 0.0);
	// glColor3f(0.0f, 0.0f, 0.0f);
	// glPointSize(4.0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-320, 320, -320, 320);
}

void rotateAndScale(){
	glColor3f (0.196078, 0.6, 0.8);
	glPointSize(1.0);
	int i;
	float theta,xNew,yNew,c,s,xtemp;
	struct point p[3];
	p[0].x = (float)X1;
	p[0].y = (float)Y1;
	p[1].x = (float)X2;
	p[1].y = (float)Y2;
	p[2].x = (float)X3;
	p[2].y = (float)Y3;
	theta = (float)((angle * 3.14)/180);
	c = cos(theta);
	s = sin(theta);
	for(i=0;i<3;i++){
		xtemp = p[i].x;
		p[i].x = c*(p[i].x - rx) - s*(p[i].y - ry) + rx;
		p[i].y = s*(xtemp - rx) + c*(p[i].y - ry) + ry;
	}
    for(i=1;i<3;i++){
		p[i].x = (p[i].x - p[0].x)*xscale + p[0].x;
		p[i].y = (p[i].y - p[0].y)*yscale + p[0].y;
	}
    glBegin(GL_TRIANGLES);
	for(i=0;i<3;i++){
		glVertex2f(p[i].x,p[i].y);
	}
	glEnd();
}

void myDisplay(void)
{
	glClear (GL_COLOR_BUFFER_BIT);
	// glColor3f (0.80, 0.80, 0.80);
	glPointSize(1.0);
    glBegin(GL_TRIANGLES);
    glColor3f (1.0, 0.0, 0.0);
    glVertex2f(0.0,0.0);
    glVertex2f(0.0,100.0);
    glVertex2f(200.0,0.0);
    glEnd();
    
    rotateAndScale();

    glFlush();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);                          //initialize the GLUT library
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize (640, 640);                  
	glutInitWindowPosition (100, 150);
	glutCreateWindow ("Algo");
	glutDisplayFunc(myDisplay);
	myInit();
	glutMainLoop();
    return 0;
}