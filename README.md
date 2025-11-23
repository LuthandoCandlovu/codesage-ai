<div align="center">
  <img width="300" height="168" alt="CodeSage AI Logo" src="https://github.com/user-attachments/assets/36ca9d1f-010f-48b6-a599-1bcae5016597" />
  
  # CodeSage AI
  ### 🤖 AI-Powered Code Review Assistant
  
  [![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
  [![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
  [![OpenAI](https://img.shields.io/badge/OpenAI-GPT-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
  
  **Transform your code quality with intelligent AI-powered reviews**
  
  [Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-usage) • [Contributing](#-contributing)
  
  ---
</div>

## 🎯 Overview

**CodeSage AI** is a comprehensive, intelligent code review system that leverages artificial intelligence to analyze your code for security vulnerabilities, performance bottlenecks, and best practice violations. Supporting multiple programming languages with zero-configuration deployment options, CodeSage makes professional-grade code review accessible to developers of all levels.

### Why CodeSage AI?

- 🔍 **Deep Analysis**: AST-based parsing combined with AI provides insights beyond surface-level linting
- 🛡️ **Security First**: Automatically detects vulnerabilities, hardcoded secrets, and security anti-patterns
- ⚡ **Real-Time Feedback**: Get instant code review results through an intuitive web interface
- 🌐 **Multi-Language**: Native support for Python, JavaScript, Java, and C++
- 🚀 **Production Ready**: Docker support, GitHub Actions integration, and enterprise-grade API

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔐 Security Analysis
- SQL injection detection
- XSS vulnerability scanning
- Hardcoded credential detection
- Insecure function identification
- OWASP compliance checking

</td>
<td width="50%">

### 🎨 Code Quality
- Best practices enforcement
- Performance optimization tips
- Code complexity analysis
- Design pattern suggestions
- Refactoring recommendations

</td>
</tr>
<tr>
<td width="50%">

### 🤖 AI-Powered Insights
- GPT-4 integration for context-aware reviews
- Natural language explanations
- Custom rule learning
- Intelligent code suggestions
- Historical pattern recognition

</td>
<td width="50%">

### 🛠️ Developer Experience
- Beautiful web dashboard
- REST API for CI/CD integration
- GitHub webhook support
- Zero-dependency fallback mode
- Comprehensive reporting

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8+
Node.js 16+ (optional, for advanced features)
OpenAI API key
```

### Installation

#### 🎯 Option 1: Full Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/LuthandoCandlovu/codesage-ai.git
cd codesage-ai

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

#### 🔧 Option 2: Zero-Dependencies Mode

Perfect for quick testing or environments with restricted dependencies:

```bash
git clone https://github.com/LuthandoCandlovu/codesage-ai.git
cd codesage-ai
python zero_dependencies_app.py
```

### Launch Application

```bash
# Terminal 1 - Start Backend API
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2 - Start Frontend Dashboard
cd frontend
streamlit run src/main.py
```

🎉 **Access the dashboard at** `http://localhost:8501`

---

## 📖 Usage

### Web Interface

1. **Navigate** to `http://localhost:8501`
2. **Paste** your code into the editor
3. **Select** your programming language
4. **Click** "Analyze Code"
5. **Review** security findings, suggestions, and metrics

### API Integration

```python
import requests

# Analyze code via REST API
response = requests.post(
    "http://localhost:8000/api/analyze",
    json={
        "code": """
        def authenticate(username, password):
            if password == 'admin123':  # Security issue!
                return True
            return False
        """,
        "language": "python",
        "options": {
            "include_ai_review": True,
            "severity_threshold": "medium"
        }
    }
)

result = response.json()
print(f"Issues found: {len(result['issues'])}")
print(f"Security score: {result['metrics']['security_score']}")
```

### CI/CD Integration

```yaml
# .github/workflows/code-review.yml
name: CodeSage Review
on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run CodeSage AI
        run: |
          curl -X POST http://your-codesage-instance/api/analyze \
            -H "Content-Type: application/json" \
            -d @code_payload.json
```

---

---

## 📸 See It In Action

<div align="center">
  <img width="100%" alt="CodeSage AI Dashboard" src="https://github.com/user-attachments/assets/a88c3138-05a6-4527-97be-c04c391f1046" />
  <p><em>Real-time code analysis with detailed security findings and AI-powered suggestions</em></p>
</div>

---

## 🏗️ Architecture

```
codesage-ai/
├── 📁 backend/                 # FastAPI backend service
│   ├── app/                   # Application core
│   │   ├── api/              # REST API endpoints
│   │   ├── core/             # Configuration & settings
│   │   ├── models/           # Pydantic data models
│   │   └── services/         # Business logic layer
│   ├── analysis/             # Code analysis engines
│   └── tests/                # Backend test suite
├── 📁 frontend/               # Streamlit web interface
│   ├── src/                  # Frontend source code
│   ├── components/           # Reusable UI components
│   └── utils/                # Helper functions
├── 📁 scripts/                # Automation & utility scripts
├── 📁 docs/                   # Documentation
├── 🐳 Dockerfile             # Container configuration
├── 📄 zero_dependencies_app.py # Standalone version
└── 📋 requirements.txt        # Python dependencies
```

---

## 🔧 Configuration

Create a `.env` file in the root directory:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4

# Application Settings
APP_ENV=development
LOG_LEVEL=INFO

# GitHub Integration (Optional)
GITHUB_WEBHOOK_SECRET=your_webhook_secret
GITHUB_TOKEN=your_github_token

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
FRONTEND_PORT=8501
```

---

## 🌟 Key Highlights

### Supported Languages

| Language | Analysis Depth | Security Checks | Performance Analysis |
|----------|---------------|-----------------|---------------------|
| 🐍 Python | ⭐⭐⭐⭐⭐ | ✅ Full | ✅ Full |
| 📜 JavaScript | ⭐⭐⭐⭐⭐ | ✅ Full | ✅ Full |
| ☕ Java | ⭐⭐⭐⭐ | ✅ Full | ✅ Partial |
| ⚡ C++ | ⭐⭐⭐⭐ | ✅ Partial | ✅ Full |

### Security Vulnerability Detection

- **SQL Injection**: Detects unsafe database query construction
- **XSS Vulnerabilities**: Identifies unescaped user input
- **Hardcoded Secrets**: Finds API keys, passwords, and tokens
- **Insecure Dependencies**: Flags known vulnerable libraries
- **Authentication Issues**: Weak password policies and session management
- **Path Traversal**: Directory traversal vulnerability detection

---

## 🤝 Contributing

We love contributions! Here's how you can help make CodeSage AI even better:

### Getting Started

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Write clear, documented code
- Add tests for new features
- Follow existing code style
- Update documentation as needed
- Be respectful and collaborative

### Areas We Need Help

- 🌐 Additional language support (Go, Rust, TypeScript)
- 🧪 Expanding test coverage
- 📚 Documentation improvements
- 🎨 UI/UX enhancements
- 🔌 New integrations (GitLab, Bitbucket)

---

## 📊 Roadmap

- [ ] **Q1 2024**: TypeScript and Go support
- [ ] **Q2 2024**: IDE plugins (VSCode, IntelliJ)
- [ ] **Q3 2024**: Team collaboration features
- [ ] **Q4 2024**: Custom rule engine builder
- [ ] **2025**: Machine learning model training on user feedback

---

## 📚 Documentation

- [📖 Full Documentation](https://github.com/LuthandoCandlovu/codesage-ai/wiki)
- [🚀 API Reference](https://github.com/LuthandoCandlovu/codesage-ai/wiki/API)
- [🔧 Configuration Guide](https://github.com/LuthandoCandlovu/codesage-ai/wiki/Configuration)
- [🐛 Troubleshooting](https://github.com/LuthandoCandlovu/codesage-ai/wiki/Troubleshooting)

---

## 💡 Use Cases

- **Code Reviews**: Automated PR reviews for teams
- **Security Audits**: Regular security scanning
- **Learning Tool**: Educational feedback for students
- **CI/CD Pipeline**: Continuous code quality monitoring
- **Legacy Code**: Understanding and improving old codebases

---

## 🙏 Acknowledgments

- OpenAI for GPT API
- FastAPI and Streamlit communities
- All our amazing contributors
- Open source security research community

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support & Community

- 🐛 [Report Issues](https://github.com/LuthandoCandlovu/codesage-ai/issues)
- 💬 [Discussions](https://github.com/LuthandoCandlovu/codesage-ai/discussions)
- 📧 Email: support@codesage-ai.com
- 🐦 Twitter: [@CodeSageAI](https://twitter.com/codesageai)

---

<div align="center">
  
  ### ⭐ Star this repo if you find it helpful!
  
  **Made with ❤️ by developers, for developers**
  
  [⬆ Back to Top](#codesage-ai)
  
</div>
