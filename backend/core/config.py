import os
from typing import Optional

class Settings:
    # API Settings
    app_name: str = \"CodeSage AI Code Review\"
    debug: bool = False
    
    # AI Model Settings
    openai_api_key: Optional[str] = os.getenv(\"OPENAI_API_KEY\")
    anthropic_api_key: Optional[str] = os.getenv(\"ANTHROPIC_API_KEY\")
    
    # GitHub Integration
    github_webhook_secret: Optional[str] = os.getenv(\"GITHUB_WEBHOOK_SECRET\")
    
    # Security
    secret_key: str = \"your-secret-key-here\"

settings = Settings()
