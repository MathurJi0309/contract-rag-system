import React, { useRef, useEffect } from 'react'

export default function ChatInput({ onSend, disabled, loading }) {
  const textareaRef = useRef()

  const handleSubmit = () => {
    const val = textareaRef.current?.value.trim()
    if (!val || disabled || loading) return
    onSend(val)
    textareaRef.current.value = ''
    textareaRef.current.style.height = 'auto'
  }

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSubmit()
    }
  }

  const handleInput = (e) => {
    e.target.style.height = 'auto'
    e.target.style.height = `${Math.min(e.target.scrollHeight, 120)}px`
  }

  return (
    <div className="chat-input-bar">
      <div className="chat-input-inner">
        <textarea
          ref={textareaRef}
          className="form-control chat-textarea"
          placeholder={disabled ? 'Upload documents to start asking questions…' : 'Ask a question about your contracts…'}
          onKeyDown={handleKeyDown}
          onInput={handleInput}
          disabled={disabled || loading}
          rows={1}
        />
        <button
          className="btn ask-btn"
          onClick={handleSubmit}
          disabled={disabled || loading}
          title="Send (Enter)"
        >
          {loading ? (
            <span className="spinner-border spinner-border-sm text-white" />
          ) : (
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
              <line x1="22" y1="2" x2="11" y2="13" />
              <polygon points="22 2 15 22 11 13 2 9 22 2" />
            </svg>
          )}
        </button>
      </div>
      <p className="chat-hint">Press Enter to send · Shift+Enter for new line</p>
    </div>
  )
}
