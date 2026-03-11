async function register(){
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const first_name = document.getElementById("first_name").value;
    const last_name = document.getElementById("last_name").value;
    const phone = document.getElementById("phone").value;
    const email = document.getElementById("email").value;


    try{
        const res = await axios.post(
            "http://127.0.0.1:8000/api/auth/register/",
            {
                username: username,
                email: email,
                first_name: first_name,
                last_name: last_name,
                phone: phone,
                password: password
            }
        );
        alert("Register success");

        window.location.href = "login.html";

    }catch(error){

        console.log(error.response.data);

        alert("Register failed");

    }

}
