import API from '../api/axios'

export const documentService = {
  upload: async (files, onUploadProgress) => {
    const formData = new FormData()
    files.forEach((file) => formData.append('files', file))

    const res = await API.post('/api/v1/documents/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
      onUploadProgress,
    })
    return res.data
  },
}
