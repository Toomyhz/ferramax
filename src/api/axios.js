import axios from 'axios';

const api = axios.create({
    baseURL:  'http://localhost:5000'|| 'http://192.168.1.90:5000',
});

export default api;