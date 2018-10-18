
#include <iostream>
#include <stdlib.h>
#include <GL/glut.h>
#include <math.h>

using namespace std;


class Point {
public:
    float x, y;
    void setxy(float x2, float y2)
    {
        x = x2; y = y2;
    }
    const Point & operator=(const Point &rPoint)
    {
        x = rPoint.x;
        y = rPoint.y;
        return *this;
    }

};

int factorial(int n)
{
    if (n<=1)
        return(1);
    else
        n=n*factorial(n-1);
    return n;
}

float binomial_coff(float n,float k)
{
    float ans;
    ans = factorial(n) / (factorial(k)*factorial(n-k));
    return ans;
}




Point abc[20];
int SCREEN_HEIGHT = 500;
int points = 0;
int clicks = 4;
int first=0;

void myInit() {
    glClearColor(1.0,1.0,1.0,0.0);
    glColor3f(1.0,0.0,0.0);
    glClearDepth(1.0f);
    glPointSize(3);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluOrtho2D(0.0,640.0,0.0,500.0);
    //glOrtho(0.0,640.0,0.0,500.0,0.0,0.0);

}

void drawDot(int x, int y) {
    glBegin(GL_POINTS);
     glVertex3i(x,y,1);
    glEnd();
    glFlush();
}

void drawLine(Point p1, Point p2) {
    glBegin(GL_LINES);
      glVertex3f(p1.x, p1.y ,1);
      glVertex3f(p2.x, p2.y ,1);
    glEnd();
    glFlush();
}


//Calculate the bezier point


Point drawBezierGeneralized(Point PT[], double t) {
        Point P;
        P.x = 0; P.y = 0;
        for (int i = 0; i<clicks; i++)
        {
            P.x = P.x + binomial_coff((float)(clicks - 1), (float)i) * pow(t, (double)i) * pow((1 - t), (clicks - 1 - i)) * PT[i].x;
            P.y = P.y + binomial_coff((float)(clicks - 1), (float)i) * pow(t, (double)i) * pow((1 - t), (clicks - 1 - i)) * PT[i].y;
        }
        //cout<<P.x<<endl<<P.y;
        //cout<<endl<<endl;
        return P;
    }
float xrot = 0.0;
/*void draw()
{
    glColor3f(0.2,1.0,0.0);
    glTranslatef(abc[0].x,abc[0].y,1);
    glRotatef(xrot,1.0,0.0,0.0);
    glTranslatef(-abc[0].x,-abc[0].y,-1);
    for(int k=0;k<clicks-1;k++)
        drawLine(abc[0], abc[clicks-1]);

    Point p1 = abc[0];
    for(double t = 0.0;t <= 1.0; t += (1.0/15.0))
    {
        Point p2 = drawBezierGeneralized(abc,t);
        cout<<p1.x<<"  ,  "<<p1.y<<endl;
        cout<<p2.x<<"  ,  "<<p2.y<<endl;
        cout<<endl;
        drawLine(p1, p2);
        p1 = p2;
    }
    glColor3f(0.0,0.0,0.0);
}*/
void myMouse(int button, int state, int x, int y) {
  // If left button was clicked
  if(button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) 
  {
    // Store where mouse was clicked, Y is backwards.
    if(points==0 && first!=0){
        abc[0].setxy(abc[clicks-1].x,abc[clicks-1].y);
        first=1;
        points++;
        cout<<"asdsd";
        return;
    }
    if(first==0){
        first=1;
    }
    abc[points].setxy((float)x,(float)(SCREEN_HEIGHT - y));
    points++;

    // Draw the red  dot.
    //glTranslatef(1.5f, 0.0f, -7.0f);
    drawDot(x, SCREEN_HEIGHT - y);


    if(points == clicks)
    {
        /*for(;xrot<=360.0;xrot+=30.0)
            draw();*/
        glColor3f(1.0,0.0,0.0);
        // for(int k=0;k<clicks-1;k++)
        // drawLine(abc[k], abc[k+1]);
        // drawLine(abc[0], abc[clicks-1]);

		Point p1 = abc[0];
		for(double t = 0.0;t <= 1.0; t += (1.0/15.0))
		{
		    Point p2 = drawBezierGeneralized(abc,t);
		    cout<<p1.x<<"  ,  "<<p1.y<<endl;
		    cout<<p2.x<<"  ,  "<<p2.y<<endl;
		    cout<<endl;
		    drawLine(p1, p2);
		    p1 = p2;
		}
		glColor3f(1.0,0.0,0.0);
		points = 0;
    }
  }
}


void myDisplay() {
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
   glFlush();
}

int main(int argc, char *argv[]) {
    glutInit(&argc, argv);            // Initialize GLUT
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH); // Enable double buffered mode
    glutInitWindowSize(640, 500);   // Set the window's initial width & height
    glutInitWindowPosition(100,150);
    glutCreateWindow("Bezier Curve");
    glutMouseFunc(myMouse);
    glutDisplayFunc(myDisplay);
    myInit();
    glutMainLoop();

    return 0;
}

