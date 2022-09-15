function ValidateEmail(inputText) {
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    errorMessage = document.getElementById('erroremail');
    if (inputText.value.match(mailformat)) {
        errorMessage.innerText = '';
        return true;
    }
    else {
        // alert("You have entered an invalid email address!");
        errorMessage.innerText = 'This is an invalid email';
        document.form1.gmail.focus();
        return false;
    }
}

function CheckUsername(inputtxt) {
    // var decimal = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
    var decimal = /^(?=.*[A-Z])(?=.*[0-9])/;
    errorMessage = document.getElementById('errorname');
    if (inputtxt.value.match(decimal)) {
        errorMessage.innerText = '';
        return true;
    }
    else {
        errorMessage.innerText = 'This is an invalid name';
        console.log(inputtxt.value)
        document.form1.uname.focus();
        return false;
    }
} 

function UnameValidate(event){
    document.addEventListener('keypress', keyPressHandler);    
}

function ValidatePassword() {
 
    var pass = document.getElementById('pword').value;
    var confirm_pass = document.getElementById('cpword').value;
    if (pass != confirm_pass) {
        document.getElementById('wrong_pass_alert').style.color = 'red';
        document.getElementById('wrong_pass_alert').innerHTML
          = '☒ Use same password';
        document.getElementById('create').disabled = true;
        document.getElementById('create').style.opacity = (0.4);
    } else {
        document.getElementById('wrong_pass_alert').style.color = 'green';
        document.getElementById('wrong_pass_alert').innerHTML =
            '🗹 Password Matched';
        document.getElementById('create').disabled = false;
        document.getElementById('create').style.opacity = (1);
    }
}

function keyPressHandler(event){
    // console.log("Key pressed: ",event.key)
    CheckUsername(document.form1.uname);
}
function SubmitForm(){
    bool1 = ValidateEmail(document.form1.gmail);
    bool1 = CheckUsername(document.form1.uname);

    // if(bool1 && bool2){
    // }
    //alert("Name: "+document.getElementById('fname').value )

}
