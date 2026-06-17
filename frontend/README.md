# ContractAI — Frontend

A professional AI-powered contract analysis chatbot built with React.js, Vite, Bootstrap 5, and more.

## Tech Stack

- **React 18** + Vite
- **React Router DOM v6** — client-side routing
- **Bootstrap 5** + React Bootstrap — UI components
- **Axios** — HTTP client with JWT interceptor
- **React Hook Form** — form validation
- **React Hot Toast** — notifications
- **React Markdown** — AI response rendering

## Quick Start

```bash
# 1. Install dependencies
npm install

# 2. Copy environment config
cp .env.example .env

# 3. Edit .env with your backend URL
# VITE_API_BASE_URL=http://localhost:8000

# 4. Run development server
npm run dev

# App runs at http://localhost:3000
```

## Build for Production

```bash
npm run build
# Output: dist/
```

## Project Structure

```
src/
├── api/
│   └── axios.js            # Axios instance + JWT interceptor
├── services/
│   ├── authService.js      # Login / Register API calls
│   ├── documentService.js  # File upload with progress
│   └── queryService.js     # Chat question API
├── context/
│   └── AuthContext.jsx     # Auth state, login, logout
├── routes/
│   └── ProtectedRoute.jsx  # Redirect unauthenticated users
├── pages/
│   ├── Login.jsx
│   ├── Register.jsx
│   └── Dashboard.jsx       # Main chatbot interface
├── components/
│   ├── Navbar.jsx          # Top nav with user pill + logout
│   ├── UploadBox.jsx       # Drag & drop upload with progress
│   ├── ChatMessage.jsx     # User/AI message bubbles
│   ├── ChatInput.jsx       # Textarea + send button
│   └── Loader.jsx          # Full-screen spinner
├── App.jsx
└── main.jsx
```

## API Endpoints Expected

| Method | Path | Auth |
|--------|------|------|
| POST | `/api/v1/user/register` | No |
| POST | `/api/v1/user/login` | No |
| POST | `/api/v1/documents/upload` | Bearer |
| POST | `/api/v1/query/query/` | Bearer |

## Features

- ✅ JWT Authentication with session persistence
- ✅ Protected routes (auto-redirect to /login)
- ✅ Drag & drop multi-file upload (PDF + TXT)
- ✅ Upload progress bar
- ✅ Chatbot with typing indicator + auto-scroll
- ✅ Markdown rendering in AI responses
- ✅ Copy AI response button
- ✅ Press Enter to send, Shift+Enter for new line
- ✅ Toast notifications for all actions
- ✅ Responsive mobile layout
