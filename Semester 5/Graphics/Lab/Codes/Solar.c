#include <cmath>
#ifdef __SUN__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif
#include <stdlib.h>
#include <cstdio>
#include <string>


/* GLUT callback Handlers */
static void resize(int width, int height)
{
	const float ar = (float) width / (float) height;

	glViewport(0, 0, width, height);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glFrustum(-ar, ar, -1.0, 1.0, 2.0, 100.0);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity() ;
}

// Planet class that will hold all our planetary data
class Planet {
public:
	std::string name = "";
	double x = 0;
	double y = 0;
	double c1 = 0;
	double c2 = 0;
	double c3 = 0;
	double f = 0;
	double a = 0;
	double s1 = 0;

	Planet(std::string,double,double,double,double,double,double);
	void glStuff(double t, double closeness);
	void printPlanet();
};

// Simple planet constructor
Planet::Planet(std::string name="",double c1=0,double c2=0,double c3=0,double f=0,double a=0,double s1=0) {
	this->name = name;
	this->x = 0;
	this->y = 0;
	this->c1 = c1;
	this->c2 = c2;
	this->c3 = c3;
	this->f = f;
	this->a = a;
	this->s1 = s1;
}

// Function will compute new planet position
void Planet::glStuff(double t, double closeness) {
	x = sin(t*f)*a*1.5;
	y = cos(t*f)*a;

	glColor3d(c1,c2,c3);
	glPushMatrix();
	glTranslated(x,y,closeness);
	glRotated(50.0*t,0,0,1);
	glutSolidSphere(s1,20,20);
	glPopMatrix();
}

static double closeness = -15.0;
Planet** planets;
double moon_x; // moon x position
double moon_y; // moon y position
static double t; // time

static void display(void) // void
{
    t = glutGet(GLUT_ELAPSED_TIME) / 1000.0;
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	for(int i = 0; i < 2; i++) {
		(*planets[i]).glStuff(t, closeness);
	}

	// moon orbit calculation
	moon_x = -sin(t)*0.5+ planets[1]->x;
	moon_y = cos(t)*0.5+ planets[1]->y;

    // "Moon"
	glColor3d(0.7,0.7,0.7);
	glPushMatrix();
	glTranslated(moon_x , moon_y , closeness);
	glRotated(60,1,0,0);
	glRotated(50.0*t,0,0,1);
	glutSolidSphere(0.1,20,20);
	glPopMatrix();

	glutSwapBuffers();
}

static void key(unsigned char key, int x, int y)
{
	switch (key)
	{
		case 27 :
		case 'q':
			exit(0);
			break;
		case '+':
			if (closeness < -4.0) {
				closeness += 0.5;
			}
			break;
		case '-':
			closeness -= 0.5;
			break;
	}
	glutPostRedisplay();
}

static void idle(void)
{
	glutPostRedisplay();
}

const GLfloat light_ambient[]  = { 0.0f, 0.0f, 0.0f, 1.0f };
const GLfloat light_diffuse[]  = { 1.0f, 1.0f, 1.0f, 1.0f };
const GLfloat light_specular[] = { 1.0f, 1.0f, 1.0f, 1.0f };
const GLfloat light_position[] = { -20.0f, 10.0f, 0.0f, 0.0f };

const GLfloat mat_ambient[]    = { 0.7f, 0.7f, 0.7f, 1.0f };
const GLfloat mat_diffuse[]    = { 0.8f, 0.8f, 0.8f, 1.0f };
const GLfloat mat_specular[]   = { 1.0f, 1.0f, 1.0f, 1.0f };
const GLfloat high_shininess[] = { 50.0f };

int main(int argc, char *argv[])
{
	// Although the sun is not a planet it is
	// convenient to keep in our array of planets
	planets = new Planet*[2];
	Planet q("sun", 1.0, 0.6, 0.0, 0.0, 0.0, 1.5);        planets[0] = &q;
	Planet d("earth", 0.0, 0.0, 0.7, 0.2, 4.0, 0.2);      planets[1] = &d;
	
	glutInit(&argc, argv);
	glutInitWindowSize(1100,600);
	glutInitWindowPosition(100,20);
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH);

	glutCreateWindow("Solar System");

	glutReshapeFunc(resize);
	glutDisplayFunc(display);
	glutKeyboardFunc(key);
	glutIdleFunc(idle);

	glClearColor(0,0,0,0);
	glEnable(GL_CULL_FACE);
	glCullFace(GL_BACK);
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LESS);

	glEnable(GL_LIGHT0);
	glEnable(GL_NORMALIZE);
	glEnable(GL_COLOR_MATERIAL);
	glEnable(GL_LIGHTING);

	glLightfv(GL_LIGHT0, GL_AMBIENT,  light_ambient);
	glLightfv(GL_LIGHT0, GL_DIFFUSE,  light_diffuse);
	glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular);
	glLightfv(GL_LIGHT0, GL_POSITION, light_position);

	glMaterialfv(GL_FRONT, GL_AMBIENT,   mat_ambient);
	glMaterialfv(GL_FRONT, GL_DIFFUSE,   mat_diffuse);
	glMaterialfv(GL_FRONT, GL_SPECULAR,  mat_specular);
	glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess);

	glutMainLoop();

	return EXIT_SUCCESS;
}
