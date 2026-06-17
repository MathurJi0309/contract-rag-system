import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useForm } from 'react-hook-form'
import toast from 'react-hot-toast'
import { useAuth } from '../context/AuthContext'

export default function Login() {
  const { login } = useAuth()
  const navigate = useNavigate()
  const [loading, setLoading] = useState(false)

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm()

  const onSubmit = async (data) => {
    setLoading(true)
    try {
      await login(data)
      toast.success('Welcome back!')
      navigate('/dashboard')
    } catch (err) {
      toast.error(err?.response?.data?.message || 'Invalid credentials. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="auth-wrapper">
      <div className="auth-card">
        <div className="auth-logo">
          <div className="auth-logo-icon">📋</div>
          <span className="auth-logo-text">ContractAI</span>
        </div>

        <h1 className="auth-title">Sign in to your account</h1>
        <p className="auth-subtitle">Analyze contracts with the power of AI</p>

        <form onSubmit={handleSubmit(onSubmit)} noValidate>
          <div className="mb-3">
            <label className="auth-label">Email address</label>
            <input
              type="email"
              className="form-control auth-input"
              placeholder="you@company.com"
              {...register('email', {
                required: 'Email is required',
                pattern: { value: /^\S+@\S+\.\S+$/, message: 'Enter a valid email' },
              })}
            />
            {errors.email && <p className="field-error">{errors.email.message}</p>}
          </div>

          <div className="mb-4">
            <label className="auth-label">Password</label>
            <input
              type="password"
              className="form-control auth-input"
              placeholder="Your password"
              {...register('password', {
                required: 'Password is required',
                minLength: { value: 6, message: 'Password must be at least 6 characters' },
              })}
            />
            {errors.password && <p className="field-error">{errors.password.message}</p>}
          </div>

          <button type="submit" className="btn btn-primary auth-btn w-100" disabled={loading}>
            {loading ? (
              <>
                <span className="spinner-border spinner-border-sm me-2" />
                Signing in…
              </>
            ) : (
              'Sign in'
            )}
          </button>
        </form>

        <div className="auth-divider mt-4">
          Don't have an account?{' '}
          <Link to="/register" className="auth-link">
            Create one free
          </Link>
        </div>
      </div>
    </div>
  )
}
