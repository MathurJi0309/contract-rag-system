import React, { createContext, useContext, useState, useEffect, useCallback } from 'react'
import { authService } from '../services/authService'

const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null)
  const [token, setToken] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const savedToken = localStorage.getItem('ca_token')
    const savedUser = localStorage.getItem('ca_user')
    if (savedToken && savedUser) {
      setToken(savedToken)
      setUser(JSON.parse(savedUser))
    }
    setLoading(false)
  }, [])

  const login = useCallback(async (credentials) => {
    const data = await authService.login(credentials)
    const jwt = data.token || data.access_token || data.data?.token
    const userData = data.user || data.data?.user || { email: credentials.email, name: data.name }

    localStorage.setItem('ca_token', jwt)
    localStorage.setItem('ca_user', JSON.stringify(userData))
    setToken(jwt)
    setUser(userData)
    return data
  }, [])

  const register = useCallback(async (credentials) => {
    const data = await authService.register(credentials)
    return data
  }, [])

  const logout = useCallback(() => {
    localStorage.removeItem('ca_token')
    localStorage.removeItem('ca_user')
    setToken(null)
    setUser(null)
  }, [])

  const value = { user, token, loading, login, register, logout, isAuthenticated: !!token }

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

export function useAuth() {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth must be used within AuthProvider')
  return ctx
}
