import API from '../api/axios'

export const authService = {
  register: async (data) => {
    const res = await API.post('/api/v1/user/register', data)
    return res.data
  },

  login: async (data) => {
    const res = await API.post('/api/v1/user/login', data)
    return res.data
  },
}
