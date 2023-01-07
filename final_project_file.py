from OpenGL.GL import *#gl lib
from OpenGL.GLUT import *#gl lib
from OpenGL.GLU import *
import OpenGL


"""Clock"""

"""Clock Hands and Animation"""

from datetime import datetime
import time
i=0.0
j=0.0
k=0.0
def initGL():
  global i
  global j
  global k
  glClearColor(0.0, 0.1, 0.0, 0.1)
  now = datetime.now()
  sec = int(now.strftime("%S"))
  min = int(now.strftime("%M"))
  hr = int(now.strftime("%H"))
  i = -6 * sec
  j = -6 * min
  k = -30 * hr


def disp(id=0):
    global i
    global j
    global k
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(5.0)
    
    #clock hands

    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    #12
    glVertex2f(0.0,.9)
    glVertex2f(0.0,.75)

    #3
    glVertex2f(0.9,0.0)
    glVertex2f(0.75,0.0)
    #6
    glVertex2f(0.0,-0.9)
    glVertex2f(0.0,-0.75)
    #9
    glVertex2f(-0.9,0.0)
    glVertex2f(-0.75,0.0)
    #1
    glVertex2f(0.45,0.8)
    glVertex2f(0.399,0.7)
    #2
    glVertex2f(0.8,0.4)
    glVertex2f(0.7,0.34)
    #4
    glVertex2f(0.8,-0.4)
    glVertex2f(0.7,-0.34)
    #5
    glVertex2f(.45,-.8)
    glVertex2f(.399,-.7)
    #7
    glVertex2f(-.45,-.8)
    glVertex2f(-.399,-.7)
    #8
    glVertex2f(-.8,-.4)
    glVertex2f(-.7,-.34)
    #10
    glVertex2f(-.8,.4)
    glVertex2f(-.7,.34)
    #11
    glVertex2f(-.45,.8)
    glVertex2f(-.399,.7)
    
    #clock hand digit show 
    #12 digit show
    #1
    glVertex2f(-0.1,0.6)
    glVertex2f(-0.1,0.4)
    glVertex2f(-0.2,0.4)
    glVertex2f(0.0,0.4)
    glVertex2f(-0.1,0.6)
    glVertex2f(-0.15,0.55)
    #2
    glVertex2f(.1,.53)
    glVertex2f(.1,.6)
    glVertex2f(.1,.6)
    glVertex2f(.25,.6)
    glVertex2f(.25,.6)
    glVertex2f(.25,.5)
    glVertex2f(.25,.5)
    glVertex2f(.1,.5)
    glVertex2f(.1,.5)
    glVertex2f(.1,.4)
    glVertex2f(.1,.4)
    glVertex2f(.25,.4)

    #3 digit draw
    glVertex2f(.4,.1)
    glVertex2f(.4,.2)
    glVertex2f(.4,.2)
    glVertex2f(.6,.2)
    glVertex2f(.6,.2)
    glVertex2f(.6,-.2)
    glVertex2f(.6,-.2)
    glVertex2f(.4,-.2)
    glVertex2f(.4,-.2)
    glVertex2f(.4,-.1)
    glVertex2f(.6,0.0)
    glVertex2f(.4,0.0)

    #9 draw
    glVertex2f(-.6,0.0)
    glVertex2f(-.6,.2)
    glVertex2f(-.6,.2)
    glVertex2f(-.4,.2)
    glVertex2f(-.4,.2)
    glVertex2f(-.4,-.2)
    glVertex2f(-.4,-.2)
    glVertex2f(-.6,-.2)
    glVertex2f(-.6,0.0)
    glVertex2f(-.4,0.0)

    #6 draw
    glVertex2f(.1,-.4)
    glVertex2f(-.1,-.4)
    glVertex2f(-.1,-.4)
    glVertex2f(-.1,-.6)
    glVertex2f(-.1,-.6)
    glVertex2f(.1,-.6)
    glVertex2f(.1,-.6)
    glVertex2f(.1,-.47)
    glVertex2f(.1,-.47)
    glVertex2f(-.1,-.47)

    glEnd()

    glPushMatrix()
    glRotatef(i, 0.0,0.0,0.1)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)    #Second
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 0.6)
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glRotatef(j, 0.0, 0.0, 0.1)
    glLineWidth(3.0)
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)    #Minute
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 0.5)
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glRotatef(k, 0.0, 0.0, 0.1)
    glLineWidth(6.0)
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 0.0)    #Hour
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 0.3)
    glEnd()
    glPopMatrix()

    i -= 6
    if i <= -360:
        if j <= -360:
            k -= 5.0
            i = 0.0
            j = 0.0
        else:
            j -= 6.0
            i = 0.0


    glLoadIdentity()
    glColor3f(1, 1, 0)
    glPointSize(2)


    def circle(x,y,r):
      glPointSize(3.5)
      glBegin(GL_POINTS)
      glColor3f(1, 1, 1)
      x=x/1000
      y=y/1000
      a=0
      b=r
      d=1-r
      while a<=b:
        p=a
        q=b
        p=p/1000
        q=q/1000


        glVertex2f(q+x,p+y)
        glVertex2f(p+x,q+y)
        glVertex2f(-p+x,q+y)
        glVertex2f(-q+x,p+y)
        glVertex2f(-q+x,-p+y)
        glVertex2f(-p+x,-q+y)
        glVertex2f(p+x,-q+y)
        glVertex2f(q+x,-p+y)
        if d>0:
          d=d+2*a-2*b+5
          a+=1
          b-=1
        else:
          d=d+2*a+3
          a+=1
      glEnd()

    circle(0,0,90)

    glutTimerFunc(1000, disp, 0)
    glutSwapBuffers()



if __name__ == '__main__':
  glutInit()
  glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
  glutInitWindowSize(1000, 1000)
  glutCreateWindow("Our Clock")
  initGL()
  glutDisplayFunc(disp)
  glutMainLoop()


