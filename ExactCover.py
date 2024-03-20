from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from User import User
import help_class

app = Flask(__name__) #defult setting for the app
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)




users = {} #dictionary containing the users and their emails - key is the email and the value is the username
users_tokens = {} #dictionary containing the users by their email and their tokens - key is email and value is the tokens


@app.route('/')
def homepage():
        if not session.get("username"):         #check if the user is not logged in using session
            return redirect('/login')     
        name = session["username"]                      
        current_tokens = users_tokens[session["email"]]
        return render_template('target.html', name = name, current_tokens = current_tokens)     #if the user is logged in, render the target page which is the main page of the app
                                                                                                #also sending the username and the current tokens to the target page

        
@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":                #checks if the user sent a request to login, declared by the method type - post or get
        name = request.form.get("username")
        email = request.form.get("email")
        new_user = User(name,email)                 #create a new user object with the username and email entered

        if email not in users:              #check if the user is new or not
            if not email_check(email):      #if the user is new, check if the email is in the right format
                return render_template('login.html', message="ERROR: Invalid Email, email should be in this fomrat:'abc@abc.com'")
            
            users[new_user.Email] = new_user.Username
            session["username"] = request.form.get("username")              #if the user is new, add the user to the users dictionary and set the session username and email
            session["email"] = request.form.get("email")
            users_tokens[new_user.Email] = new_user.get_tokens()            #also add the user to the users_tokens dictionary and set the tokens to the default value (3)
            return  redirect('/')
   

        
        else:
            if users[email] == name:                            #if the user is not new, set the session and seding the the landing page that should render the target page 
                session["username"] = request.form.get("username")        
                session["email"] = request.form.get("email")
                # users_tokens[session["email"]] = new_user.get_tokens() #debug
                
                return redirect('/')
            else:
                return render_template('login.html', message="ERROR: not the correct username")    #if the username isnt as saved in the users dictionary, send an error message

    return render_template('login.html')    # if request method is get, render the login page
        


@app.route('/target',methods=['POST','GET'] )  #the route for the target page
def target():
    name = session["username"]              #get the username from the session and send it to the target page
    
    return render_template('target.html',name = name)  

def email_check(email):                                 #help function to check if the email is in the right format
    if email.count('@') == 1 and email.count('.') >= 1: 
        parts = email.split('.')
        if len(parts[-1])>1:         
            return True     
        else:
            return False

@app.route('/logout')               #route for the logout page
def logout():
    session["username"] = None      #set the session username to none
    return redirect('/')



@app.route('/result_page', methods=["POST","GET"])          #route for the result page
def result_page():
    if not session.get("username"):                     #check if the user is logged in using session
            return redirect('/login') 
   
   
    current_tokens = users_tokens[session["email"]]     #get the current tokens of the user from the users_tokens dictionary
    
    if request.method == "POST":                #check if the user sent a request to the result page, declared by the method type - post or get
        group = request.form.get("group")         
        sub_group = request.form.get("sub_group")         #get the group and sub_group from the form
        
        if check_integers(group) == False or help_class.is_valid_sublist(sub_group) == False:   #this if statement checks if the input for both group and subgroup is valid
                                                                                                #this uses functions from the help_class.py file
             return render_template('target.html', message = "ERROR: Invalid Input", current_tokens = current_tokens) 
      
        
        
        users_tokens[session["email"]] -=1                  #if the input is valid, reduce the tokens of the user by 1 because he used the app main feature.
        current_tokens = users_tokens[session["email"]]         #get the current tokens of the user from the users_tokens dictionary
        username = users[session["email"]]                      #get the username of the user from the users dictionary
     
        a = group
        b = sub_group 
        flag = False
        if  type(help_class.Exact_cover(a,b)) != type("a"): #using a flag to check if it is an exact cover, for futre use (if result is string it isnt exact cover)
            flag = True          
                                                 
        return render_template('result_page.html' ,flag=flag ,message2 = help_class.Exact_cover(a,b), current_tokens = current_tokens, username = username, a=a)    #send the result of the exact cover function to the result page

        
    

def check_integers(input_str): #help function to check if the input is a string of integers
    inputs = input_str.split(',')
    for item in inputs:
        if not item.strip().isdigit():
            return False
    return True
  




if __name__ == "__main__":
    app.run(debug=True)