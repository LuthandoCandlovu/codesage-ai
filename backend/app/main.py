from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import code_review, github_webhook, metrics

app = FastAPI(
    title=\"CodeSage AI Code Review Assistant\",
    description=\"AI-powered code review system with multi-language support\",
    version=\"1.0.0\"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[\"*\"],
    allow_credentials=True,
    allow_methods=[\"*\"],
    allow_headers=[\"*\"],
)

# Include routers
app.include_router(code_review.router, prefix=\"/api/v1/code-review\", tags=[\"code-review\"])
app.include_router(github_webhook.router, prefix=\"/api/v1/webhook\", tags=[\"webhook\"])
app.include_router(metrics.router, prefix=\"/api/v1/metrics\", tags=[\"metrics\"])

@app.get(\"/\")
async def root():
    return {\"message\": \"CodeSage AI Code Review Assistant API\"}

@app.get(\"/health\")
async def health_check():
    return {\"status\": \"healthy\"}
