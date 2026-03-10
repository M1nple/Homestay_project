const axiosClient = axios.create({
    baseURL: "http://127.0.0.1:8000/api"
});

axiosClient.interceptors.request.use(function (config) {

    const token = localStorage.getItem("access");

    if (token) {
        config.headers.Authorization = "Bearer " + token;
    }

    return config;
});


// tất cả API request đi qua đây
// tự động gắn JWT token