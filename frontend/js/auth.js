
// hàm logout xóa toten trong localstorage 
function logout(){

  localStorage.removeItem("access");
  localStorage.removeItem("refresh");

  window.location.href = "home.html";

}


// kiểm tra login chưa 
function checkLogin(){

  const token = localStorage.getItem("access");

  if(!token){

    window.location.href = "home.html";

  }

}


