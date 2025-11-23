import streamlit as st
import requests
import json

st.set_page_config(
    page_title=\"CodeSage AI Code Review\", 
    page_icon=\"🔍\",
    layout=\"wide\"
)

st.markdown(\"\"\"
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
\"\"\", unsafe_allow_html=True)

st.markdown('<h1 class=\"main-header\">🔍 CodeSage AI Code Review</h1>', unsafe_allow_html=True)

# Configuration
api_url = \"http://localhost:8000\"

# Sidebar
st.sidebar.title(\"Configuration\")
selected_language = st.sidebar.selectbox(
    \"Programming Language\",
    [\"python\", \"javascript\", \"java\", \"cpp\"]
)

# Main content
code_input = st.text_area(
    \"Enter your code to analyze:\",
    height=300,
    placeholder=\"Paste your code here...\",
    help=\"The code will be analyzed for security vulnerabilities and best practices\"
)

if st.button(\"Analyze Code\", type=\"primary\"):
    if code_input.strip():
        with st.spinner(\"Analyzing code...\"):
            try:
                # Call the API
                response = requests.post(
                    f\"{api_url}/api/analyze\",
                    json={
                        \"code\": code_input,
                        \"language\": selected_language
                    },
                    timeout=30
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # Display metrics
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        st.metric(\"Security Score\", f\"{result['security_score']:.2%}\")
                    
                    with col2:
                        st.metric(\"Complexity Score\", f\"{result['complexity_score']:.2%}\")
                    
                    with col3:
                        st.metric(\"Maintainability\", f\"{result['maintainability_score']:.2%}\")
                    
                    with col4:
                        st.metric(\"Total Issues\", len(result['issues']))
                    
                    # Display issues
                    st.subheader(\"Issues Found\")
                    
                    for issue in result['issues']:
                        with st.container():
                            st.write(f\"**Line {issue['line_number']}** - *{issue['severity'].upper()}*\"\)
                            st.write(f\"**{issue['message']}**\"\)
                            if issue.get('suggestion'):
                                st.write(f\"💡 {issue['suggestion']}\"\) 
                
                else:
                    st.error(f\"Analysis failed: {response.text}\")
                    
            except requests.exceptions.ConnectionError:
                st.error(\"❌ Cannot connect to backend server.\")
                st.info(\"Run: python zero_dependencies_app.py\"\)
            except Exception as e:
                st.error(f\"Failed to connect to API: {e}\")
    else:
        st.warning(\"Please enter some code to analyze\")

# Footer
st.markdown(\"---\")
st.markdown(\"### 🔍 CodeSage AI Code Review Assistant\")
