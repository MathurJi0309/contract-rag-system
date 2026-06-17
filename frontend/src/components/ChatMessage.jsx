import React, { useState } from 'react'
import ReactMarkdown from 'react-markdown'
import toast from 'react-hot-toast'

function formatTime(date) {
  return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
}

export default function ChatMessage({ message }) {
  const { role, content, timestamp } = message
  const isUser = role === 'user'
  const [copied, setCopied] = useState(false)

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(content)
      setCopied(true)
      toast.success('Copied to clipboard')
      setTimeout(() => setCopied(false), 2000)
    } catch {
      toast.error('Could not copy text')
    }
  }

  return (
    <div className={`message-row ${isUser ? 'user' : 'ai'}`}>
      <div className={`message-avatar ${isUser ? 'user' : 'ai'}`}>
        {isUser ? '👤' : '🤖'}
      </div>

      <div className="message-content">
        <div className={`message-bubble ${isUser ? 'user' : 'ai'}`}>
          {isUser ? (
            content
          ) : (
            <div className="markdown-content">
              <ReactMarkdown>{content}</ReactMarkdown>
            </div>
          )}
        </div>

        <div className="message-meta">
          <span className="message-time">{formatTime(timestamp)}</span>
          {!isUser && (
            <button className="btn copy-btn" onClick={handleCopy}>
              {copied ? '✓ Copied' : '⎘ Copy'}
            </button>
          )}
        </div>
      </div>
    </div>
  )
}
