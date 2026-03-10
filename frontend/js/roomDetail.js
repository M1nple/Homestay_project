function getRoomId(){

  const params = new URLSearchParams(window.location.search);

  return params.get("id");

}

async function loadRoomDetail(){

  const roomId = getRoomId();

  try{

    const res = await axiosClient.get(`/rooms/${roomId}/`);

    const room = res.data;

    document.getElementById("room-name").innerText = room.room_name;

    document.getElementById("room-description").innerText = room.description;

    document.getElementById("room-guests").innerText = room.max_guests;

    const price = Number(room.price_per_night).toLocaleString();

    document.getElementById("room-price").innerText = price;

    document.getElementById("room-status").innerText = room.status;

  }catch(error){

    console.log(error);

  }

}

async function bookRoom(){

  const roomId = getRoomId();

  try{

    await axiosClient.post("/bookings/",{
      room: roomId
    });

    alert("Booking success");

  }catch(error){

    alert("Booking failed");

  }

}

loadRoomDetail();