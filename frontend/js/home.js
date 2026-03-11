async function loadRooms(){

  try{

    const res = await axiosClient.get("/homestays/");

    const homestays = res.data;

    const container = document.getElementById("homestay-list");

    container.innerHTML = "";

    homestays.forEach(homestay => {

      const card = `
        <div class="col-md-4 mb-4">

        <div class="card shadow room-card"
             onclick="goToDetail(${homestay.HomestayID})"
             style="cursor:pointer">
             
            <img src="https://picsum.photos/400/200" class="card-img-top">

            <div class="card-body">

              <h5 class="card-title" >${homestay.name}</h5>

              <p class="card-text">
                address: ${homestay.address}
                ward: ${homestay.ward_name}
                district: ${homestay.district_name}
                city: ${homestay.city_name}
              </p>

              <button class="btn btn-primary" onclick="bookRoom(${homestay.HomestayID})">
                Book
              </button>

            </div>

          </div>

        </div>
      `;

      container.innerHTML += card;

    });

  }catch(error){

    console.log(error);

  }

}

async function bookRoom(roomId){

  try{

    await axiosClient.post("/bookings/",{
      room: roomId
    });

    alert("Booking successful");

  }catch(error){

    console.log(error);

    alert("Booking failed");

  }

}

function goToDetail(roomId){

  window.location.href = `room-detail.html?id=${roomId}`;

}

loadRooms();