async function loadRooms(){

  try{

    const res = await axiosClient.get("/rooms/");

    const rooms = res.data;

    const container = document.getElementById("room-list");

    container.innerHTML = "";

    rooms.forEach(room => {

      const card = `
        <div class="col-md-4 mb-4">

        <div class="card shadow room-card"
             onclick="goToDetail(${room.id})"
             style="cursor:pointer">
             
            <img src="https://picsum.photos/400/200" class="card-img-top">

            <div class="card-body">

              <h5 class="card-title" >${room.room_name}</h5>

              <p class="card-text">
                Price: $${room.price_per_night}
              </p>

              <button class="btn btn-primary" onclick="bookRoom(${room.id})">
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