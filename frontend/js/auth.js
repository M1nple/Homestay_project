
// hàm logout xóa toten trong localstorage 
function logout(){

  localStorage.removeItem("access");
  localStorage.removeItem("refresh");

  window.location.href = "login.html";

}


// kiểm tra login chưa 
function checkLogin(){

  const token = localStorage.getItem("access");

  if(!token){

    window.location.href = "home.html";

  }

}

async function renderNavbar(){

  const token = localStorage.getItem("access");

  const nav = document.getElementById("nav-auth");

  if(!token){

    nav.innerHTML = `
      <a href="login.html" class="btn btn-primary">
        Login
      </a>
    `;

    return;
  }

  try{

    const res = await axiosClient.get("/auth/me/");

    const user = res.data;

    nav.innerHTML = `
      <span class="text-white me-3">
        Welcome ${user.username}
      </span>

      <button class="btn btn-danger" onclick="logout()">
        Logout
      </button>
    `;

  }catch(error){

    console.log(error);

  }

}