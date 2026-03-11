async function loadMyHomestays(){

  try{

    const res = await axiosClient.get("/host/homestays/");

    const homestays = res.data;

    console.log(homestays);

    const list = document.getElementById("homestay-list");

    let html = "";

    homestays.forEach(h => {
      console.log(h);
      html += `
        <div class="col-md-4 mb-4">
        <div class="card shadow room-card"
          <div class="card">

            <div class="card-body">

                <img src="https://picsum.photos/400/200" class="card-img-top">
              <h5 class="card-title">${h.name}</h5>

              <p class="card-text">
                ${h.address || ""}
              </p>

              <a href="rooms-by_homestay.html?id=${h.HomestayID}" 
                 class="btn btn-primary">
                 xem phòng
              </a>

              <a href="create-room.html?id=${h.HomestayID}" 
                 class="btn btn-primary">
                 Thêm phòng
              </a>

              <a href="edit-homestay.html?id=${h.HomestayID}" 
                 class="btn btn-primary">
                 Sửa 
              </a>

              <button class="btn btn-primary" onclick="deleteHomestay(${h.HomestayID})">
                 Xóa 
              </button>

            </div>

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

function deleteHomestay(id){
  if(confirm("Bạn có chắc muốn xóa homestay này?")){
    axiosClient.delete(`/host/homestays/${id}/`)
      .then(res => {
        alert("Xóa thành công");
        loadMyHomestays();
      })
      .catch(error => {
        console.log(error);
        alert("Xóa thất bại");
      });
  }
}