async function login(){

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try{

        const res = await axios.post(
            "http://127.0.0.1:8000/api/token/",
            {username, password}
        );

        localStorage.setItem("access", res.data.access);

        alert("Login success");

        window.location.href = "rooms.html";

    }catch(error){

        alert("Login failed");

    }

}