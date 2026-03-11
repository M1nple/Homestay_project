function loadNavbar(){

  document.getElementById("navbar").innerHTML = `

  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">

    <div class="container-fluid">

      <a class="navbar-brand" href="home.html">Homestay</a>

      <div class="collapse navbar-collapse">

        <ul class="navbar-nav me-auto" id="main-menu">

          <li class="nav-item">
            <a class="nav-link" href="home.html">Home</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="homestays.html">Homestays</a>
          </li>

        </ul>

        <!-- menu role -->
        <ul class="navbar-nav me-3" id="role-menu"></ul>

        <!-- login logout -->
        <div id="nav-auth"></div>

      </div>

    </div>

  </nav>

  `;

  renderNavbar();
}




async function renderNavbar(){

  const token = localStorage.getItem("access");

  const nav = document.getElementById("nav-auth");
  const roleMenu = document.getElementById("role-menu");

  if(!token){

    nav.innerHTML = `
      <a href="register.html" class="btn btn-secondary me-2">Register</a>
      <a href="login.html" class="btn btn-primary">Login</a>
    `;

    return;
  }

  try{

    const res = await axiosClient.get("/auth/me/");

    const user = res.data;

    console.log(user);  

    let menu = "";

    switch(user.role){

      case "ADMIN":
        menu = `
          <li class="nav-item">
            <a class="nav-link" href="dashboard.html">Dashboard</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="users.html">Manage Users</a>
          </li>
        `;
        break;

      case "HOST":
        menu = `
          <li class="nav-item">
            <a class="nav-link" onclick="goToMyHomestay(${user.id})">My Homestay</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" onclick="window.location.href='create-homestay.html'">Tạo homestay</a>
          </li>
        `;
        break;

      case "CUSTOMER":
        menu = `

            <li class="nav-item">
                <a class="nav-link" href="bookings.html">My Booking</a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="host.html">Become Host</a>
            </li>

        `;
        break;

    }

    roleMenu.innerHTML = menu;

    nav.innerHTML = `
      <span class="text-white me-3">Welcome ${user.username}</span>
      <button class="btn btn-danger" onclick="logout()">Logout</button>
    `;

  }catch(error){
      console.log(error);

      nav.innerHTML = `
        <a href="register.html" class="btn btn-secondary me-2">Register</a>
        <a href="login.html" class="btn btn-primary">Login</a>
      `;

  }

}



function logout(){

  localStorage.removeItem("access");

  window.location.href = "login.html";

}

function goToMyHomestay(userId){

  window.location.href = `my-homestay.html?user_id=${userId}`;
}

