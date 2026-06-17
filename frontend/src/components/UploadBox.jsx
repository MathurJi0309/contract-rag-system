import React, { useState, useRef, useCallback } from 'react'
import { ProgressBar } from 'react-bootstrap'
import toast from 'react-hot-toast'
import { documentService } from '../services/documentService'

const ACCEPTED = ['application/pdf', 'text/plain']
const ACCEPT_EXT = '.pdf,.txt'

function getFileIcon(type) {
  if (type === 'application/pdf') return '📄'
  if (type === 'text/plain') return '📝'
  return '📎'
}

function formatSize(bytes) {
  if (bytes < 1024) return `${bytes} B`
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`
}

export default function UploadBox({ onUploadSuccess,docs_count }) {
  const [files, setFiles] = useState([])
  const [dragging, setDragging] = useState(false)
  const [uploading, setUploading] = useState(false)
  const [progress, setProgress] = useState(0)
  const [uploaded, setUploaded] = useState(false)
  const inputRef = useRef()

  const addFiles = useCallback((incoming) => {
    const valid = Array.from(incoming).filter((f) => {
      if (!ACCEPTED.includes(f.type)) {
        toast.error(`${f.name}: only PDF and TXT files are supported`)
        return false
      }
      return true
    })
    setFiles((prev) => {
      const names = new Set(prev.map((f) => f.name))
      return [...prev, ...valid.filter((f) => !names.has(f.name))]
    })
  }, [])

  const removeFile = (idx) => setFiles((prev) => prev.filter((_, i) => i !== idx))

  const handleDrop = (e) => {
    e.preventDefault()
    setDragging(false)
    addFiles(e.dataTransfer.files)
  }

  const handleUpload = async () => {
    if (!files.length) {
      toast.error('Select at least one file to upload')
      return
    }
    setUploading(true)
    setProgress(0)
    try {
      await documentService.upload(files, (evt) => {
        if (evt.total) setProgress(Math.round((evt.loaded / evt.total) * 100))
      })
      setProgress(100)
      setUploaded(true)
      toast.success('Documents uploaded — you can now ask questions!')
      onUploadSuccess()
      setFiles([])
    } catch (err) {
      toast.error(err?.response?.data?.message || 'Upload failed. Please try again.')
    } finally {
      setUploading(false)
    }
  }

  return (
    <div>
      <p className="panel-title">Upload Documents</p>
      <p className="panel-title">({docs_count} present )</p>
      <p className="panel-subtitle">PDF or TXT — multiple files supported</p>

      {/* Drop Zone */}
      <div
        className={`drop-zone${dragging ? ' dragging' : ''}`}
        onDragOver={(e) => { e.preventDefault(); setDragging(true) }}
        onDragLeave={() => setDragging(false)}
        onDrop={handleDrop}
        onClick={() => inputRef.current?.click()}
      >
        <input
          ref={inputRef}
          type="file"
          accept={ACCEPT_EXT}
          multiple
          onChange={(e) => addFiles(e.target.files)}
          onClick={(e) => e.stopPropagation()}
          style={{ display: 'none' }}
        />
        <span className="drop-icon">📂</span>
        <p className="drop-label">
          {dragging ? 'Drop files here' : 'Drag & drop files here'}
        </p>
        <p className="drop-hint">or click to browse — PDF & TXT accepted</p>
      </div>

      {/* File List */}
      {files.length > 0 && (
        <div className="file-list">
          {files.map((f, i) => (
            <div key={`${f.name}-${i}`} className="file-item">
              <span className="file-icon">{getFileIcon(f.type)}</span>
              <div className="file-meta">
                <div className="file-name">{f.name}</div>
                <div className="file-size">{formatSize(f.size)}</div>
              </div>
              {!uploading && !uploaded && (
                <button className="file-remove" onClick={() => removeFile(i)} title="Remove">
                  ✕
                </button>
              )}
            </div>
          ))}
        </div>
      )}

      {/* Progress */}
      {uploading && (
        <div className="upload-progress-wrap">
          <div className="upload-progress-label">
            <span>Uploading…</span>
            <span>{progress}%</span>
          </div>
          <ProgressBar
            now={progress}
            striped
            animated
            style={{ height: '6px', borderRadius: '3px' }}
          />
        </div>
      )}

      {/* Upload Button */}
      {!uploaded && (
        <button
          className="btn btn-primary upload-btn"
          onClick={handleUpload}
          disabled={uploading || files.length === 0}
        >
          {uploading ? (
            <>
              <span className="spinner-border spinner-border-sm me-2" />
              Uploading…
            </>
          ) : (
            `Upload ${files.length > 0 ? `(${files.length} file${files.length > 1 ? 's' : ''})` : ''}`
          )}
        </button>
      )}

      {/* Success Banner */}
      {uploaded && (
        <div className="upload-success-banner">
          <span>✅</span>
          <div>
            <strong>Documents uploaded successfully.</strong>
            <br />
            You can now ask questions about your contracts.
          </div>
        </div>
      )}
    </div>
  )
}
