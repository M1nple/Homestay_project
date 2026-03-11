function getHomestayId(){
    const params = new URLSearchParams(window.location.search);
    return params.get("id");
}

function getHomestayId(){
    const params = new URLSearchParams(window.location.search);
    return params.get("id");
}

async function createRoom() {

    const data = {
        room_name: document.getElementById("name").value,
        description: document.getElementById("description").value,
        max_guests: document.getElementById("guests").value,
        price_per_night: document.getElementById("price").value,
        status: document.getElementById("status").value
    };

    console.log('dâta', data);
    try {

        await axiosClient.post(`/host/homestays/${getHomestayId()}/rooms/`, data, {
            headers: {
                "Content-Type": "application/json"
            }
        });

        alert("Tạo phòng thành công");

        window.location.href = `my-homestay.html?id=${getHomestayId()}`;

    } catch (error) {

        console.error("Lỗi khi tạo phòng:", error.response?.data);
        alert("Có lỗi xảy ra khi tạo phòng");

    }
}