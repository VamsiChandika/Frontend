 function validateform() {
            var firstPassword = document.getElementById('t1').value
            var secondPassword = document.getElementById('t2').value
            
            if (firstPassword == secondPassword) {
                return true;
            }
            else {
                alert("Password and Confirm Password must be same");
                return false;
            }
        } 