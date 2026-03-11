async function createHomestay(){

  const data = {

    name: document.getElementById("name").value,
    address: document.getElementById("address").value,
    city: document.getElementById("city").value,
    district: document.getElementById("district").value,
    ward: document.getElementById("ward").value,
    price_per_night: document.getElementById("price").value,
    max_guests: document.getElementById("guests").value,
    description: document.getElementById("description").value

  };

  try{

    await axiosClient.post("/host/homestays/", data, {
      headers:{
        "Content-Type":"application/json"
      }
    });

    alert("Tạo Homestay thành công");

    window.location.href = "my-homestay.html";

  }catch(error){

    console.log(error);

  }

}