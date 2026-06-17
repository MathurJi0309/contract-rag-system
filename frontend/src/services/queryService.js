import API from '../api/axios'

export const queryService = {
  ask: async (question) => {
    const res = await API.post('/api/v1/query/query/', { question })
    return res.data
  },
  docs_present:async()=>{
     const res = await API.get('/api/v1/documents/status')
    return res.data
  }
}


