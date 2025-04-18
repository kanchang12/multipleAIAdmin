import os
from flask import Flask, render_template_string, request, jsonify, render_template
import openai

# Use environment variables for secrets
openai.api_key = os.getenv('OPENAI_API_KEY', '')

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/agent-creator.html')
def agent_creator():
    return render_template('agent-creator.html')

@app.route('/phone-integration.html')
def phone_integration():
    return render_template('phone-integration.html')

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Voice Assistant Prompt Generator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f4f6f9; }
        textarea {
            min-height: 300px;
            resize: vertical;
        }
        #prompt-output {
            background-color: #f8f9fa;
            font-family: monospace;
        }
    </style>
</head>
<body>
<div class="container mt-5 position-relative">
    <a href="/dashboard" class="btn btn-secondary position-absolute top-0 end-0">Return to Dashboard</a>
    <h2 class="mb-4">🎙️ Voice Assistant Prompt Generator</h2>
    <div class="row">
        <div class="col-md-6">
            <label for="user-context" class="form-label">📝 Your Voice Assistant Context</label>
            <textarea id="user-context" class="form-control" placeholder="Describe your assistant's use case, role, and behavior..."></textarea>
            <button id="generate-btn" class="btn btn-primary mt-3">Generate Prompt</button>
        </div>

        <div class="col-md-6">
            <label for="prompt-output" class="form-label">📤 Generated Prompt</label>
            <textarea id="prompt-output" class="form-control" readonly placeholder="Your custom prompt will appear here..."></textarea>
            <div class="mt-3 d-flex justify-content-between">
                <button id="copy-btn" class="btn btn-secondary">Copy</button>
                <button id="clear-btn" class="btn btn-outline-secondary">Clear</button>
            </div>
        </div>
    </div>
</div>

<script>
    document.getElementById('generate-btn').addEventListener('click', function () {
        const context = document.getElementById('user-context').value.trim();
        const outputEl = document.getElementById('prompt-output');

        if (!context) {
            alert("Please enter context to generate a prompt.");
            return;
        }

        outputEl.value = "Generating precise prompt...";

        fetch('/generate_prompt', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ context: context })
        })
        .then(response => response.json())
        .then(data => {
            if (data.prompt) {
                outputEl.value = data.prompt;
            } else {
                outputEl.value = "Error: " + data.error;
            }
        })
        .catch(error => {
            outputEl.value = "Request failed: " + error.message;
        });
    });

    document.getElementById('copy-btn').addEventListener('click', function () {
        const output = document.getElementById('prompt-output');
        output.select();
        document.execCommand('copy');
        this.textContent = "Copied!";
        setTimeout(() => { this.textContent = "Copy"; }, 2000);
    });

    document.getElementById('clear-btn').addEventListener('click', function () {
        document.getElementById('user-context').value = '';
        document.getElementById('prompt-output').value = '';
    });
</script>
</body>
</html>
"""

@app.route('/')
def index():
    provided_token = request.args.get('token')
    expected_token = os.getenv('ACCESS_TOKEN')
    
    if not provided_token or provided_token != expected_token:
        return 'Unauthorized Access', 401
    
    return render_template_string(HTML_TEMPLATE)

@app.route('/generate_prompt', methods=['POST'])
def generate_prompt():
    data = request.json
    user_context = data.get("context", "")

    try:
        system_prompt = """You are an advanced prompt engineering AI specializing in creating highly precise, context-aware voice assistant prompts. Your goal is to:
        - Deeply understand the user's specific requirements
        - Translate abstract needs into a concrete, actionable prompt
        - Generate a prompt that feels custom-built for the exact use case
        - Ensure the prompt captures both the letter and spirit of the user's intent
        - Create a prompt that is immediately implementable by a voice assistant"""

        response = openai.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"User context:\n{user_context}"}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        generated_prompt = response.choices[0].message.content.strip()
        return jsonify(prompt=generated_prompt)

    except Exception as e:
        return jsonify(error=str(e)), 500

# Koyeb requires using the host 0.0.0.0 and a port from the PORT environment variable
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
