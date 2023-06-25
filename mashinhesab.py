from tkinter import *
from tkinter import ttk

def add(x):
    global a
    a.append(x)


def text_button(name,b):
    b.config( command= lambda:add_entry(name) )
    
    
def button_making():
    global b
    global a
    for i in range(0,18):
        if a[i]=='0':
            b[i] = ttk.Button( w , text=a[i] , width=32 )

        else:
            b[i] = ttk.Button( w , text=a[i] , width=5 )
        text_button(a[i],b[i])
            

def grid():
    global a
    global b
    i=0
    for r in range(1,6):
        for c in range(1,5):
            if a[i]=='0':
                b[i].grid( row=r , column=c , ipadx=15 , ipady=1 , pady=5 , padx=5 , columnspan=3 )
                i=i+1
            
            elif a[i]=='=':
                b[i].grid( row=r , column=c+2 , ipadx=15 , ipady=1 , pady=5 , padx=5 )
                break
            
            else:
                b[i].grid( row=r , column=c , ipadx=15 , ipady=1 , pady=5 , padx=5 )
                i+=1


def add_entry(txt):
    st_e = str(e.get())
    l = len(st_e)
        
    if txt=='=':
##        if st_e=='*' or st_e=='/' or st_e=='+' or st_e=='-':
##            e.delete(l-1 , l)
##            st_e = str(e.get())
        answer = eval(st_e)
        e.delete(0 , END)
        e.insert(0 , answer)

    elif txt=='c':
        e.delete(0 , END)

    elif txt=='del':
        e.delete(l-1 , l)
        
    else :
        e.insert(END , txt)

########
w = Tk()
w.title("calculator")

###### Entry
s = StringVar()
e = Entry( w , textvariable=s , width=40 , borderwidth=5 )
e.grid( row=0 , column=0 , columnspan=5 )
##e.place( x=0 , y=0 , relx=0.9 , rely=0.9 )


###### Button
a=[]
b=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
add('c')
add('del')
add('.')
add('/')

add('7')
add('8')
add('9')
add('*')

add('4')
add('5')
add('6')
add('-')

add('1')
add('2')
add('3')
add('+')

add('0')
add('=')

button_making()
grid()
w.mainloop()
    














































