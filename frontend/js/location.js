let locations = [];

async function loadLocations(){

  try{

    const res = await axiosClient.get("/locations/");
    console.log(res.data);
    locations = res.data;
    

    const citySelect = document.getElementById("city");

    citySelect.innerHTML = "<option value=''>Select city</option>";

    locations.forEach(city => {

      citySelect.innerHTML += `
        <option value="${city.id}">
          ${city.name}
        </option>
      `;

    });

  }catch(error){

    console.log(error);

  }

}
function loadDistricts(cityId){

  const city = locations.find(c => c.id == cityId);

  const districtSelect = document.getElementById("district");

  districtSelect.innerHTML = "<option value=''>Select district</option>";

  if(!city) return;

  city.districts.forEach(district => {

    districtSelect.innerHTML += `
      <option value="${district.id}">
        ${district.name}
      </option>
    `;

  });

}
function loadWards(cityId, districtId){

  const city = locations.find(c => c.id == cityId);

  if(!city) return;

  const district = city.districts.find(d => d.id == districtId);

  const wardSelect = document.getElementById("ward");

  wardSelect.innerHTML = "<option value=''>Select ward</option>";

  if(!district) return;

  district.wards.forEach(ward => {

    wardSelect.innerHTML += `
      <option value="${ward.id}">
        ${ward.name}
      </option>
    `;

  });

}
document.getElementById("city").addEventListener("change", function(){

  loadDistricts(this.value);

});


document.getElementById("district").addEventListener("change", function(){

  const cityId = document.getElementById("city").value;

  loadWards(cityId, this.value);

});
loadLocations();