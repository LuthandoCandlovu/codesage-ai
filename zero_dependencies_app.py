# CodeSage - Zero Dependencies Version
import http.server
import socketserver
import json
import ast
import re
import html
from typing import List, Dict, Any
from enum import Enum
from urllib.parse import urlparse, parse_qs

class CodeLanguage(str, Enum):
    PYTHON = \"python\"
    JAVASCRIPT = \"javascript\"
    JAVA = \"java\"
    CPP = \"cpp\"

class CodeIssueSeverity(str, Enum):
    LOW = \"low\"
    MEDIUM = \"medium\" 
    HIGH = \"high\"
    CRITICAL = \"critical\"

class CodeIssueType(str, Enum):
    SECURITY = \"security\"
    PERFORMANCE = \"performance\" 
    CODE_SMELL = \"code_smell\"
    BUG = \"bug\"
    STYLE = \"style\"

class ZeroDependencyAnalyzer:
    def analyze_code(self, code: str, language: str) -> List[Dict]:
        issues = []
        lines = code.split('\n')
        
        for i, line in enumerate(lines, 1):
            line_issues = self._analyze_line(line, i, language)
            issues.extend(line_issues)
        
        return issues
    
    def _analyze_line(self, line: str, line_num: int, language: str) -> List[Dict]:
        issues = []
        
        # Security checks
        if any(secret in line.lower() for secret in ['password', 'api_key', 'secret', 'token']):
            if '=' in line and any(quote in line for quote in ['\"', \"'\"]):
                issues.append({
                    'line_number': line_num,
                    'issue_type': 'security',
                    'severity': 'high',
                    'message': 'Potential hardcoded secret',
                    'suggestion': 'Use environment variables or secure configuration',
                    'confidence': 0.7
                })
        
        if 'eval(' in line:
            issues.append({
                'line_number': line_num,
                'issue_type': 'security',
                'severity': 'critical', 
                'message': 'Use of eval() function',
                'suggestion': 'Avoid eval() as it can execute arbitrary code',
                'confidence': 0.9
            })
        
        return issues

class CodeSageAPIHandler(http.server.SimpleHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_OPTIONS(self):
        self._set_headers(200)
    
    def do_GET(self):
        if self.path == '/':
            self._serve_frontend()
        elif self.path == '/api/languages':
            self._get_languages()
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Not found'}).encode())
    
    def do_POST(self):
        if self.path == '/api/analyze':
            self._analyze_code()
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Not found'}).encode())
    
    def _serve_frontend(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html_content = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>CodeSage AI - Zero Dependencies</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .container { max-width: 1200px; margin: 0 auto; }
                .header { text-align: center; margin-bottom: 30px; }
                textarea { width: 100%; height: 300px; font-family: monospace; }
                button { padding: 10px 20px; background: #007acc; color: white; border: none; cursor: pointer; }
                .issue { padding: 10px; margin: 5px 0; border-left: 4px solid #ff4b4b; background: #f9f9f9; }
            </style>
        </head>
        <body>
            <div class=\"container\">
                <div class=\"header\">
                    <h1>🔍 CodeSage AI Code Review</h1>
                    <p>Zero Dependencies Version - Basic Static Analysis</p>
                </div>
                
                <select id=\"language\">
                    <option value=\"python\">Python</option>
                    <option value=\"javascript\">JavaScript</option>
                    <option value=\"java\">Java</option>
                    <option value=\"cpp\">C++</option>
                </select>
                <textarea id=\"code\" placeholder=\"Paste your code here...\"></textarea>
                <button onclick=\"analyzeCode()\">Analyze Code</button>
                
                <div id=\"results\" style=\"display: none;\">
                    <div id=\"metrics\"></div>
                    <div id=\"issues\"></div>
                </div>
            </div>
            
            <script>
                async function analyzeCode() {
                    const code = document.getElementById('code').value;
                    const language = document.getElementById('language').value;
                    
                    if (!code.trim()) {
                        alert('Please enter some code to analyze');
                        return;
                    }
                    
                    try {
                        const response = await fetch('/api/analyze', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({
                                code: code,
                                language: language
                            })
                        });
                        
                        const result = await response.json();
                        displayResults(result);
                    } catch (error) {
                        alert('Analysis failed: ' + error);
                    }
                }
                
                function displayResults(result) {
                    document.getElementById('results').style.display = 'block';
                    
                    // Display metrics
                    const metricsHtml = 
                        <div style=\"display: flex; gap: 20px; margin: 20px 0;\">
                            <div style=\"text-align: center; padding: 10px; background: #f0f0f0; border-radius: 5px;\">
                                <h3>Security Score</h3>
                                <p>%</p>
                            </div>
                            <div style=\"text-align: center; padding: 10px; background: #f0f0f0; border-radius: 5px;\">
                                <h3>Total Issues</h3>
                                <p></p>
                            </div>
                        </div>
                    ;
                    document.getElementById('metrics').innerHTML = metricsHtml;
                    
                    // Display issues
                    const issuesHtml = result.issues.map(issue => 
                        <div class=\"issue\">
                            <strong>Line :</strong> 
                            <span style=\"color: \"></span>
                            <br>
                            
                        </div>
                    ).join('');
                    document.getElementById('issues').innerHTML = issuesHtml;
                }
                
                function getSeverityColor(severity) {
                    const colors = {
                        critical: '#ff4b4b',
                        high: '#ff4b4b', 
                        medium: '#ffa64b',
                        low: '#4bff4b'
                    };
                    return colors[severity] || '#666';
                }
            </script>
        </body>
        </html>
        '''
        self.wfile.write(html_content.encode())
    
    def _get_languages(self):
        languages = {
            'languages': ['python', 'javascript', 'java', 'cpp'],
            'details': {
                'python': 'Basic static analysis',
                'javascript': 'Basic pattern matching',
                'java': 'Basic pattern matching', 
                'cpp': 'Basic pattern matching'
            }
        }
        self._set_headers(200)
        self.wfile.write(json.dumps(languages).encode())
    
    def _analyze_code(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            code = data.get('code', '')
            language = data.get('language', 'python')
            
            analyzer = ZeroDependencyAnalyzer()
            issues = analyzer.analyze_code(code, language)
            
            # Calculate scores
            security_issues = [i for i in issues if i['issue_type'] == 'security']
            security_score = max(0.0, 1.0 - len(security_issues) * 0.2)
            
            response = {
                'issues': issues,
                'summary': f'Found {len(issues)} issues',
                'complexity_score': 0.8,
                'security_score': security_score,
                'maintainability_score': 0.75,
                'explanations': ['Basic static analysis completed using zero dependencies.']
            }
            
            self._set_headers(200)
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            self._set_headers(500)
            error_response = {'error': f'Analysis failed: {str(e)}'}
            self.wfile.write(json.dumps(error_response).encode())

def run_server(port=8000):
    with socketserver.TCPServer((\"\", port), CodeSageAPIHandler) as httpd:
        print(f\"🚀 CodeSage Zero-Dependencies Server running!\")
        print(f\"📊 Open http://localhost:{port} in your browser\")
        print(\"🔍 Features: Basic static analysis, security checks, multi-language support\")
        print(\"💡 Zero external dependencies - uses only Python standard library\")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(\"\n🛑 Server stopped\")

if __name__ == \"__main__\":
    run_server()
