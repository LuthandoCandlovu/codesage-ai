# CodeSage AI - AI-Powered Code Review Assistant

![CodeSage](https://img.shields.io/badge/CodeSage-AI%20Code%20Review-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-lightblue)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)

A comprehensive AI-powered code review system that analyzes code for security vulnerabilities, performance issues, and best practices across multiple programming languages.

## 🚀 Features

- **Multi-Language Support**: Python, JavaScript, Java, C++
- **AI-Powered Analysis**: Uses OpenAI GPT for intelligent code review
- **Security Vulnerability Detection**: Identifies security risks and hardcoded secrets
- **Static Code Analysis**: Built-in AST parsing for deep code analysis
- **Real-time Web Interface**: Streamlit-based dashboard
- **Zero-Dependencies Mode**: Fallback version using only Python standard library
- **GitHub Integration**: Ready for GitHub Actions and webhooks

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python
- **Frontend**: Streamlit, Plotly
- **AI**: OpenAI API, Custom analysis engines
- **Code Analysis**: AST parsing, Pattern matching
- **Deployment**: Docker-ready, GitHub Actions

## 📦 Installation

### Option 1: Full Version (Recommended)
\\\ash
git clone https://github.com/LuthandoCandlovu/codesage-ai.git
cd codesage-ai
pip install -r requirements.txt
\\\

### Option 2: Zero-Dependencies Version
\\\ash
git clone https://github.com/LuthandoCandlovu/codesage-ai.git
cd codesage-ai
python zero_dependencies_app.py
\\\

## 🎯 Quick Start

1. **Start Backend**:
   \\\ash
   cd backend
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   \\\

2. **Start Frontend**:
   \\\ash
   cd frontend
   streamlit run src/main.py
   \\\

3. **Open Browser**: http://localhost:8501

## 🔧 Configuration

Add your API keys to \.env\:
\\\env
OPENAI_API_KEY=your_openai_key_here
GITHUB_WEBHOOK_SECRET=your_webhook_secret
\\\

## 📚 Usage

### Web Interface
1. Visit http://localhost:8501
2. Paste your code
3. Select programming language
4. Click \"Analyze Code\"
5. View security issues and suggestions

### API Usage
\\\python
import requests

response = requests.post(
    \"http://localhost:8000/api/analyze\",
    json={
        \"code\": \"def example():\\n    password = 'secret'\\n    return True\",
        \"language\": \"python\"
    }
)
print(response.json())
\\\

## 🏗️ Project Structure

\\\
codesage-ai/
├── backend/                 # FastAPI backend
│   ├── app/                # Application layer
│   ├── core/               # Configuration and settings
│   ├── models/             # Pydantic models
│   ├── services/           # Business logic
│   └── utils/              # Utility functions
├── frontend/               # Streamlit frontend
│   └── src/main.py         # Main frontend application
├── scripts/                # Utility scripts
├── zero_dependencies_app.py # Fallback version
└── requirements.txt        # Python dependencies
\\\

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues and pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**CodeSage AI** - Making code review smarter, faster, and more secure. 🔍
