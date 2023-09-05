import axios from 'axios'

export default () => {
    const Api = axios.create({
        baseURL: 'http://localhost:8000/',
        withCredentials: false,
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
    })
    return Api
}