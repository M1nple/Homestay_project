function getHomestayId(){
    const params = new URLSearchParams(window.location.search);
    return params.get("id");
}

async function loadHomestay(){
     try{

    const homestayId = getHomestayId();

    const res = await axiosClient.get(`/host/homestays/${homestayId}/`);

    const r = res.data;

    document.getElementById("name").value = r.name;
    document.getElementById("address").value = r.address;
    document.getElementById("city").value = r.city;
    document.getElementById("district").value = r.district;
    document.getElementById("ward").value = r.ward;
    document.getElementById("price").value = r.price_per_night;
    document.getElementById("guests").value = r.max_guests;
    document.getElementById("description").value = r.description;
    document.getElementById("max_guests").value = r.max_guests;
    document.getElementById("price_per_night").value = r.price_per_night;

  }catch(error){

    console.log(error);

  }

}


async function updateHomestay(){

  const id = getHomestayId();

  const data = {
    name: document.getElementById("name").value,
    description: document.getElementById("description").value,
    address: document.getElementById("address").value,
    guests: document.getElementById("guests").value,
    price: document.getElementById("price").value
  };

  const city = document.getElementById("city").value;
  const district = document.getElementById("district").value;
  const ward = document.getElementById("ward").value;

  if(city) data.city = city;
  if(district) data.district = district;
  if(ward) data.ward = ward;

  console.log(data);

  try{

    await axiosClient.patch(`/host/homestays/${id}/`, data);

    alert("Update success");
    window.location.href = "my-homestay.html";

  }catch(error){

    console.log(error.response.data);

  }

}