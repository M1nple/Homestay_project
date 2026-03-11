function getHomestayId(){

  const params = new URLSearchParams(window.location.search);
  return params.get("id");

}

console.log("Homestay ID:", getHomestayId());

async function loadMyrooms(){

  try{

    const res = await axiosClient.get(`/homestays/${getHomestayId()}/rooms/`);

    const rooms = res.data.rooms;   // sửa ở đây

    console.log(rooms);

    const list = document.getElementById("room-list");

    let html = "";

    rooms.forEach(r => {

      html += `
        <div class="col-md-4 mb-4">

          <div class="card shadow">

            <img src="https://picsum.photos/400/200" class="card-img-top">

            <div class="card-body">

              <h5 class="card-title">${r.room_name}</h5>

              <p class="card-text">
                ${r.description}
              </p>

              <p>
                Guests: ${r.max_guests}
              </p>

              <p>
                Price: ${r.price_per_night} / night
              </p>

              <span class="badge bg-success">
                ${r.status}
              </span>

            </div>

          </div>

        </div>
      `;

    });

    list.innerHTML = html;

  }catch(error){

    console.log(error);

  }

}