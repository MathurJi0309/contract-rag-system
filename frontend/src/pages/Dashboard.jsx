import React, { useState, useRef, useEffect, useCallback } from "react";
import Navbar from "../components/Navbar";
import UploadBox from "../components/UploadBox";
import ChatMessage from "../components/ChatMessage";
import ChatInput from "../components/ChatInput";
import { queryService } from "../services/queryService";
import toast from "react-hot-toast";

function TypingIndicator() {
  return (
    <div className="message-row ai">
      <div className="message-avatar ai">🤖</div>
      <div className="typing-dots">
        <div className="typing-dot" />
        <div className="typing-dot" />
        <div className="typing-dot" />
      </div>
    </div>
  );
}

export default function Dashboard() {
  const [docsReady, setDocsReady] = useState(false);
  const [docs_count,set_docs_count]=useState(0)
  const [messages, setMessages] = useState([]);
  const [aiLoading, setAiLoading] = useState(false);
  const bottomRef = useRef();

  // Auto-scroll to latest message
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, aiLoading]);
  const check_docs = async () => {
    const present = await queryService.docs_present();
    setDocsReady(present.has_documents);
    console.log("present.docs_count",present)
    set_docs_count(()=>present.docs_count)
    if(present.has_documents){
       setMessages([
      {
        id: Date.now(),
        role: "ai",
        content:
          "Your documents have been uploaded and indexed. I'm ready to answer questions about your contracts. What would you like to know?",
        timestamp: new Date(),
      },
    ]);
    }
  };
  useEffect(() => {
    check_docs();
  }, []);

  const handleUploadSuccess = useCallback(() => {
    check_docs();
   
  }, []);

  const handleSend = useCallback(
    async (question) => {
      if (!question.trim() || aiLoading) return;

      const userMsg = {
        id: Date.now(),
        role: "user",
        content: question,
        timestamp: new Date(),
      };

      setMessages((prev) => [...prev, userMsg]);
      setAiLoading(true);

      try {
        const data = await queryService.ask(question);
        const aiMsg = {
          id: Date.now() + 1,
          role: "ai",
          content:
            data.answer ||
            "I could not find an answer in the uploaded documents.",
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, aiMsg]);
      } catch (err) {
        toast.error(
          err?.response?.data?.message ||
            "Failed to get a response. Please try again.",
        );
        setMessages((prev) => [
          ...prev,
          {
            id: Date.now() + 1,
            role: "ai",
            content:
              "Sorry, I encountered an error processing your question. Please try again.",
            timestamp: new Date(),
          },
        ]);
      } finally {
        setAiLoading(false);
      }
    },
    [aiLoading],
  );

  return (
    <div className="dashboard-wrapper">
      <Navbar />

      <div className="dashboard-main">
        {/* Left panel — upload */}
        <aside className="upload-panel">
          <UploadBox onUploadSuccess={handleUploadSuccess} docs_count={docs_count} />
        </aside>

        {/* Right panel — chat */}
        <section className="chat-panel">
          {/* Messages area */}
          <div className="chat-messages">
            {!docsReady ? (
              <div className="chat-empty">
                <div className="chat-empty-icon">📋</div>
                <h2 className="chat-empty-title">Ready to analyze contracts</h2>
                <p className="chat-empty-subtitle">
                  Upload PDF or TXT contract documents on the left to start
                  asking questions.
                </p>
              </div>
            ) : (
              <>
                {messages.map((msg) => (
                  <ChatMessage key={msg.id} message={msg} />
                ))}
                {aiLoading && <TypingIndicator />}
                <div ref={bottomRef} />
              </>
            )}
          </div>

          {/* Input bar */}
          <ChatInput
            onSend={handleSend}
            disabled={!docsReady}
            loading={aiLoading}
          />
        </section>
      </div>
    </div>
  );
}
