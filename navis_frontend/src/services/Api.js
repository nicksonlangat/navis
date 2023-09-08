import axios from 'axios'

export default () => {
    const token = JSON.parse(localStorage.getItem("navis"))
    
    const Api = axios.create({
        baseURL: 'http://localhost:8000/',
        withCredentials: false,
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token.access}`
        },
    })
    return Api
}
