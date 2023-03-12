import axios from "axios";

const api = axios.create({
  baseURL: "http://10.0.0.191:5000",
});

export default api;
