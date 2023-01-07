def circle(x,y,r):
#   glPointSize(1)
#   glBegin(GL_POINTS)
#   glColor3f(.5,.3,.7)
#   x=x/100
#   y=y/100
#   a=0
#   b=r
#   d=1-r
#   while a<=b:
#     p=a
#     q=b
#     p=p/100
#     q=q/100


#     glVertex2f(q+x,p+y)
#     glVertex2f(p+x,q+y)
#     glVertex2f(-p+x,q+y)
#     glVertex2f(-q+x,p+y)
#     glVertex2f(-q+x,-p+y)
#     glVertex2f(-p+x,-q+y)
#     glVertex2f(p+x,-q+y)
#     glVertex2f(q+x,-p+y)
#     if d>0:
#       d=d+2*a-2*b+5
#       a+=1
#       b-=1
#     else:
#       d=d+2*a+3
#       a+=1
#   glEnd()
 
# circle(0,0,90)