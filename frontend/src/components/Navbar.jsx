import React from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import toast from 'react-hot-toast'

export default function Navbar() {
  const { user, logout } = useAuth()
  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
    toast.success('Signed out successfully')
    navigate('/login')
  }

  const initials = user?.name
    ? user.name.split(' ').map((n) => n[0]).join('').toUpperCase().slice(0, 2)
    : user?.email?.[0]?.toUpperCase() || 'U'

  return (
    <nav className="ca-navbar">
      <a href="/dashboard" className="ca-navbar-brand">
        <div className="ca-navbar-logo-icon">📋</div>
        <span className="ca-navbar-brand-text">ContractAI</span>
      </a>

      <div className="ca-navbar-right">
        {user && (
          <div className="ca-user-pill">
            <div className="ca-user-avatar">{initials}</div>
            <span className="ca-user-name">{user.name || user.email}</span>
          </div>
        )}
        <button className="btn ca-logout-btn" onClick={handleLogout}>
          Sign out
        </button>
      </div>
    </nav>
  )
}
