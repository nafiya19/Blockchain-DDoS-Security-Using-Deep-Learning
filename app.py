import streamlit as st
import csv
import os
import pandas as pd
import subprocess
import base64
import streamlit as st

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:background/background.avif;base64,%s");
    background-position: center;
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown('<style>h1 { color: Black; }</style>', unsafe_allow_html=True)

    st.markdown('<style>p { color: Black; font-weight: bold; }</style>', unsafe_allow_html=True)
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('background/4.jpg')
st.title("An AI Driven VM threat Prediction Model for Multirsiks Analysis based Cloud Cyber security")

typee = st.selectbox( 'CHOOSE HERE ',('HOME','Admin', 'User'))

if typee=="HOME":
    # st.text("Welcome to our page !!!")

    st.markdown(f'<h1 style="color:#000000;font-size:24px;">{" Welcome to Home Page !!! "}</h1>', unsafe_allow_html=True)
    

if typee=="Admin":
    # st.text("Welcome to our page !!!")

    st.markdown(f'<h1 style="color:#000000;font-size:24px;">{" Welcome to Admin Page !!! "}</h1>', unsafe_allow_html=True)
    
    reg=st.button('View Register Details')
    
    st.success("Welcome Admin!!!")
    
    
    adname=st.text_input("Enter Name","Name")
    passs=st.text_input("Enter Password","Password",type="password")
    aa=st.button("Submit")
    
    # if aa:
        
    if adname=="admin" and passs=="123":
        st.success("Admin Login Successfully !!!")
        subprocess.run(["streamlit", "run", "app1.py"]) 

        
        
if typee=="User":
    # st.text("Welcome to our page !!!")

    st.markdown(f'<h1 style="color:#000000;font-size:24px;">{" Welcome to User Page !!! "}</h1>', unsafe_allow_html=True)


    st.success("Welcome User!!!")    
    

    import pandas as pd
    
    # Store the initial value of widgets in session state
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False
    
    col1, col2 = st.columns(2)
    
    
        
    with col2:
    
        UR1 = st.text_input("Login User Name",key="username")
        psslog = st.text_input("Password",key="password",type="password")
        agree = st.checkbox('LOGIN')
        
        if agree:
            import pandas as pd
            try:
                
                df = pd.read_csv(UR1+'.csv')
                U_P1 = df['User'][0]
                
                import pickle
                with open('name.pickle', 'wb') as f:
                    pickle.dump(U_P1, f)
                    
                    
                U_P2 = df['Password'][0]
                if str(UR1) == str(U_P1) and str(psslog) == str(U_P2):
                    st.write('Successfully Login !!!')
                    subprocess.run(["streamlit", "run", "app1.py"]) 
                    
                else:
                    st.write('Login Failed!!!')
            except:
                st.write('Login Failed!!!')
                
                
          
    with col1:
        UR = st.text_input("Register User Name",key="username1")
        pss1 = st.text_input("First Password",key="password1",type="password")
        pss2 = st.text_input("Confirm Password",key="password2",type="password")
        
        
        
        if pss1 == pss2 and len(str(pss1)) > 2:
            import pandas as pd
            
    
                
            import csv 
            
            # field names 
            fields = ['User', 'Password'] 
            
            # data rows of csv file
            # a1 = df['User']
            # a2 = df['Password']
            # new_row = [a1,a2]
            old_row = [[UR,pss1]]
            # new_row.append(old_row)
            # name of csv file 
            
            # writing to csv file 
            with open(UR+'.csv', 'w') as csvfile: 
                # creating a csv writer object 
                csvwriter = csv.writer(csvfile) 
                    
                # writing the fields 
                csvwriter.writerow(fields) 
                    
                # writing the data rows 
                csvwriter.writerows(old_row)
                
                
            with open('All Data/'+UR+'.csv', 'w', newline='') as csvfile: 
         
            
        # creating a csv writer object 
                csvwriter = csv.writer(csvfile) 
            
            # writing the fields 
                csvwriter.writerow(fields) 
                
            # writing the data rows 
                csvwriter.writerows(old_row)
                
            
            st.write('Successfully Registered !!!')
        else:
            
            st.write('Registeration Failed !!!')

       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        