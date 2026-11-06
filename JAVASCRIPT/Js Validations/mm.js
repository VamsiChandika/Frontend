 export let validateform=() =>{
            var name = document.getElementById('t1').value
            if (name === "") {
                alert("Name can't be blank");
                return false;
            } else if (name.length < 6 || name.length > 15) {
                alert("Name must be at least 6 characters long and msut not exceeds 15 character");
                return false;
            } else {
                return true
            }
        }