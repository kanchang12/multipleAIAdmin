import os
import webbrowser
import threading
import time
import subprocess

def open_browser():
    """Open browser after a short delay"""
    time.sleep(2)  # Wait for Flask to start
    webbrowser.open('http://127.0.0.1:5000/')

def create_index_template():
    """Create the index.html template file if it doesn't exist"""
    os.makedirs('templates', exist_ok=True)
    
    # Only create if file doesn't exist to avoid overwriting customizations
    if not os.path.exists('templates/index.html'):
        with open('templates/index.html', 'w', encoding='utf-8') as f:
            f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ElevenLabs Integration Dashboard</title>
    <style>
        :root {
            --primary-color: #4361ee;
            --secondary-color: #3a0ca3;
            --accent-color: #7209b7;
            --light-color: #f8f9fa;
            --dark-color: #212529;
        }
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--dark-color);
            background-color: #f5f7fa;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        header {
            text-align: center;
            margin-bottom: 2rem;
        }
        
        h1 {
            color: var(--primary-color);
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            color: #6c757d;
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }
        
        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }
        
        .card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 1.5rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
        }
        
        .card-header {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
        }
        
        .card-icon {
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: var(--primary-color);
            color: white;
            border-radius: 50%;
            margin-right: 1rem;
            font-size: 1.2rem;
        }
        
        .card h2 {
            color: var(--secondary-color);
            font-size: 1.4rem;
            margin-bottom: 0.5rem;
        }
        
        .card p {
            color: #6c757d;
            margin-bottom: 1.5rem;
            min-height: 3rem;
        }
        
        .card-actions {
            display: flex;
            gap: 0.5rem;
        }
        
        .btn {
            display: inline-block;
            padding: 0.6rem 1.2rem;
            background-color: var(--primary-color);
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: 500;
            transition: background-color 0.3s ease;
            border: none;
            cursor: pointer;
            font-size: 1rem;
            text-align: center;
        }
        
        .btn:hover {
            background-color: var(--secondary-color);
        }
        
        .btn-secondary {
            background-color: #6c757d;
        }
        
        .btn-secondary:hover {
            background-color: #5a6268;
        }
        
        .btn-full {
            width: 100%;
        }
        
        footer {
            text-align: center;
            margin-top: 3rem;
            padding: 1rem;
            color: #6c757d;
            font-size: 0.9rem;
        }
        
        /* Modal styles */
        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            overflow: auto;
        }
        
        .modal-content {
            background-color: white;
            margin: 10% auto;
            padding: 2rem;
            border-radius: 10px;
            max-width: 600px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            position: relative;
        }
        
        .close {
            position: absolute;
            top: 1rem;
            right: 1.5rem;
            font-size: 1.5rem;
            font-weight: bold;
            color: #6c757d;
            cursor: pointer;
        }
        
        .close:hover {
            color: var(--dark-color);
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }
        
        input, textarea, select {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ced4da;
            border-radius: 5px;
            font-size: 1rem;
        }
        
        textarea {
            min-height: 100px;
            resize: vertical;
        }
        
        @media (max-width: 768px) {
            .dashboard {
                grid-template-columns: 1fr;
            }
            
            .container {
                padding: 1rem;
            }
            
            .modal-content {
                margin: 20% auto;
                width: 90%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>ElevenLabs Integration Dashboard</h1>
            <p class="subtitle">Access all your voice assistant configuration tools in one place</p>
        </header>
        
        <div class="dashboard">
            <div class="card">
                <div class="card-header">
                    <div class="card-icon">2</div>
                    <h2>Agent Creator</h2>
                </div>
                <p>Create a new ElevenLabs AI agent with custom prompt, actions, and platform tools.</p>
                <div class="card-actions">
                    <a href="agent-creator.html" class="btn btn-full" target="_blank">Open Tool</a>
                </div>
            </div>
            
            <div class="card">
                <div class="card-header">
                    <div class="card-icon">3</div>
                    <h2>Phone Number Integration</h2>
                </div>
                <p>Complete setup for phone number creation, agent connection, and talk-to link generation.</p>
                <div class="card-actions">
                    <a href="phone-integration.html" class="btn btn-full" target="_blank">Open Tool</a>
                </div>
            </div>
            
            <div class="card">
                <div class="card-header">
                    <div class="card-icon">1</div>
                    <h2>Voice Assistant Prompt Generator</h2>
                </div>
                <p>Create customized prompts for industry-specific voice assistants.</p>
                <div class="card-actions">
                    <a href="/" class="btn btn-full">Open Tool</a>
                </div>
            </div>
            
            <div class="card">
                <div class="card-header">
                    <div class="card-icon">4</div>
                    <h2>Appointment Availability Tool</h2>
                </div>
                <p>Configure the appointment availability checking tool for your voice assistant.</p>
                <div class="card-actions">
                    <button class="btn btn-full" onclick="openConfigModal()">Configure Tool</button>
                </div>
            </div>
        </div>
        
        <!-- Appointment Config Modal -->
        <div id="configModal" class="modal">
            <div class="modal-content">
                <span class="close" onclick="closeConfigModal()">&times;</span>
                <h2>Appointment Availability Tool Configuration</h2>
                <p style="margin-bottom: 1.5rem;">Configure the API parameters for checking appointment availability.</p>
                
                <form id="configForm">
                    <div class="form-group">
                        <label for="toolName">Tool Name:</label>
                        <input type="text" id="toolName" value="check_appointment_availability" readonly>
                    </div>
                    
                    <div class="form-group">
                        <label for="toolDescription">Description:</label>
                        <textarea id="toolDescription" readonly>Checks if a requested appointment time is available and suggests alternatives if not</textarea>
                    </div>
                    
                    <div class="form-group">
                        <label for="apiUrl">API URL:</label>
                        <input type="text" id="apiUrl" value="https://multipleaisolutions.com.au/callmanager/admin/appointment_check.php">
                    </div>
                    
                    <div class="form-group">
                        <label for="apiFormat">Request Format:</label>
                        <textarea id="apiFormat" readonly>{
  "requested_date": "YYYY-MM-DD",
  "requested_time": "HH:MM",
  "client_id": 123
}</textarea>
                    </div>
                    
                    <div class="form-group">
                        <label for="actionExample">Example Action JSON:</label>
                        <textarea id="actionExample" rows="25">{
  "name": "check_appointment_availability",
  "description": "Checks if a requested appointment time is available and suggests alternatives if not",
  "parameters": [
    {
      "name": "requested_date",
      "description": "The date for the requested appointment (YYYY-MM-DD)",
      "type": "string",
      "required": true
    },
    {
      "name": "requested_time",
      "description": "The time for the requested appointment (HH:MM)",
      "type": "string",
      "required": true
    },
    {
      "name": "client_id",
      "description": "The ID of the client (optional)",
      "type": "number",
      "required": false
    }
  ],
  "return": {
    "description": "Available status and alternative time slots",
    "type": "object",
    "properties": {
      "status": {
        "type": "string",
        "description": "Response status"
      },
      "is_available": {
        "type": "boolean",
        "description": "Whether the requested time is available"
      },
      "requested_datetime": {
        "type": "string",
        "description": "The requested date and time"
      },
      "alternative_slots": {
        "type": "array",
        "description": "Alternative available time slots"
      }
    }
  }
}</textarea>
                    </div>
                    
                    <button type="button" class="btn" onclick="copyActionJson()">Copy Action JSON</button>
                </form>
            </div>
        </div>
        
        <footer>
            <p>ElevenLabs Integration Tools &copy; 2025</p>
        </footer>
    </div>
    
    <script>
        function openConfigModal() {
            document.getElementById('configModal').style.display = 'block';
        }
        
        function closeConfigModal() {
            document.getElementById('configModal').style.display = 'none';
        }
        
        function copyActionJson() {
            const actionJson = document.getElementById('actionExample');
            actionJson.select();
            document.execCommand('copy');
            
            // Show temporary success message
            const button = document.querySelector('#configModal .btn');
            const originalText = button.textContent;
            button.textContent = 'Copied!';
            setTimeout(() => {
                button.textContent = originalText;
            }, 2000);
        }
        
        // Close modal if user clicks outside of it
        window.onclick = function(event) {
            const modal = document.getElementById('configModal');
            if (event.target == modal) {
                closeConfigModal();
            }
        }
    </script>
</body>
</html>""")

def create_html_files():
    """Create the HTML files for the tools if they don't exist"""
    os.makedirs('templates', exist_ok=True)
    
    # Create agent-creator.html
    if not os.path.exists('templates/agent-creator.html'):
        with open('templates/agent-creator.html', 'w', encoding='utf-8') as f:
            f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ElevenLabs Agent Creator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"], textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            height: 120px;
            font-family: monospace;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        #response {
            margin-top: 20px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: #f9f9f9;
            white-space: pre-wrap;
            display: none;
        }
        .code-block {
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 4px;
            margin-top: 20px;
            font-family: monospace;
            white-space: pre-wrap;
        }
    </style>
</head>
<body>
    <h1>ElevenLabs Agent Creator</h1>
    
    <div class="form-group">
        <label for="apiKey">ElevenLabs API Key:</label>
        
    </div>
    
    <div class="form-group">
        <label for="agentName">Agent Name:</label>
        <input type="text" id="agentName" value="My Custom Agent">
    </div>
    
    <div class="form-group">
        <label for="firstMessage">First Message:</label>
        <input type="text" id="firstMessage" value="Hello! How can I assist you today?">
    </div>
    
    <div class="form-group">
        <label for="prompt">Custom Prompt:</label>
        <textarea id="prompt">You are a helpful assistant powered by ElevenLabs and Gemini.</textarea>
    </div>
    
    <div class="form-group">
        <label for="actions">Actions (JSON format):</label>
        <textarea id="actions">[
  {
    "name": "example_action",
    "description": "An example action",
    "parameters": [
      {
        "name": "param1",
        "description": "First parameter",
        "type": "string",
        "required": true
      }
    ],
    "return": {
      "description": "Example return value",
      "type": "string"
    }
  }
]</textarea>
    </div>
    
    <div class="form-group">
        <label for="platformTools">Platform Tools (JSON format):</label>
        <textarea id="platformTools">[
  {
    "type": "browser",
    "tool_config": {
      "search_when_no_system_prompt_tool_enabled": true
    }
  }
]</textarea>
    </div>
    
    <button id="submitBtn">Create Agent</button>
    
    <div id="response"></div>
    
    <div class="code-block">
        <h3>Equivalent curl command:</h3>
        <pre id="curlCommand"></pre>
    </div>
    
    <script>
        document.getElementById('submitBtn').addEventListener('click', function() {
            const apiKey = "sk_a25b9c0aeb6381cc728ac97f54113fae13a52a4f72d88b2b";
            const firstMessage = document.getElementById('firstMessage').value;
            const prompt = document.getElementById('prompt').value;
            
            if (!apiKey) {
                alert('Please enter your ElevenLabs API key');
                return;
            }
            
            // Parse actions from the JSON input
            let actions = [];
            try {
                actions = JSON.parse(document.getElementById('actions').value);
            } catch (e) {
                alert('Invalid JSON in actions field. Please check the format.');
                return;
            }
            
            // Parse platform tools from the JSON input
            let platformTools = [];
            try {
                platformTools = JSON.parse(document.getElementById('platformTools').value);
            } catch (e) {
                alert('Invalid JSON in platform tools field. Please check the format.');
                return;
            }
            
            // Get agent name
            const agentName = document.getElementById('agentName').value;
            
            // Build the request payload
            const payload = {
                agent_name: agentName,
                conversation_config: {
                    agent: {
                        first_message: firstMessage,
                        prompt: {
                            prompt: prompt,
                            llm: "gemini-1.0-pro"
                        },
                        actions: actions
                    }
                },
                platform_settings: {
                    overrides: {
                        enable_conversation_initiation_client_data_from_webhook: true
                    }
                },
                platform_tools: platformTools
            };
            
            // Show curl command
            const curlCmd = `curl -X POST https://api.elevenlabs.io/v1/convai/agents/create \\
     -H "xi-api-key: ${apiKey}" \\
     -H "Content-Type: application/json" \\
     -d '${JSON.stringify(payload, null, 2)}'`;
            
            document.getElementById('curlCommand').textContent = curlCmd;
            
            // Make the API request
            fetch('https://api.elevenlabs.io/v1/convai/agents/create', {
                method: 'POST',
                headers: {
                    'xi-api-key': apiKey,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                const responseElement = document.getElementById('response');
                responseElement.textContent = JSON.stringify(data, null, 2);
                responseElement.style.display = 'block';
            })
            .catch(error => {
                const responseElement = document.getElementById('response');
                responseElement.textContent = `Error: ${error.message}`;
                responseElement.style.display = 'block';
            });
        });
    </script>
</body>
</html>""")
    
    # Create phone-integration.html
    if not os.path.exists('templates/phone-integration.html'):
        with open('phone-integration.html', 'w', encoding='utf-8') as f:
            f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ElevenLabs Phone Integration</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f7fa;
        }
        .container {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 25px;
            margin-bottom: 20px;
        }
        h1 {
            color: #2d3748;
            text-align: center;
            margin-bottom: 30px;
        }
        h2 {
            color: #4a5568;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 10px;
            margin-top: 0;
        }
        .step {
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            font-weight: 600;
            margin-bottom: 8px;
            color: #4a5568;
        }
        input[type="text"], textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #cbd5e0;
            border-radius: 4px;
            font-size: 14px;
            box-sizing: border-box;
        }
        textarea {
            height: 120px;
            font-family: monospace;
        }
        button {
            background-color: #4c51bf;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #434190;
        }
        .response {
            margin-top: 15px;
            padding: 15px;
            background-color: #f7fafc;
            border: 1px solid #e2e8f0;
            border-radius: 4px;
            white-space: pre-wrap;
            font-family: monospace;
            max-height: 200px;
            overflow-y: auto;
            display: none;
        }
        .code-block {
            background-color: #f1f5f9;
            padding: 15px;
            border-radius: 4px;
            margin-top: 15px;
            font-family: monospace;
            white-space: pre-wrap;
        }
        .navigation {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }
        .tabs {
            display: flex;
            border-bottom: 1px solid #e2e8f0;
            margin-bottom: 20px;
        }
        .tab {
            padding: 10px 20px;
            cursor: pointer;
            border-bottom: 3px solid transparent;
        }
        .tab.active {
            border-bottom: 3px solid #4c51bf;
            color: #4c51bf;
            font-weight: 600;
        }
        .step-content {
            display: none;
        }
        .step-content.active {
            display: block;
        }
        .status {
            display: inline-block;
            margin-left: 10px;
            font-size: 14px;
            font-weight: 500;
        }
        .success {
            color: #48bb78;
        }
        .error {
            color: #e53e3e;
        }
        .link-button {
            display: inline-block;
            margin-top: 10px;
            padding: 8px 16px;
            background-color: #48bb78;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            font-size: 14px;
        }
        #copyPythonBtn, #copyAgentLinkBtn, #copyCurlUpdateBtn, #copyWidgetBtn {
            background-color: #718096;
            padding: 8px 12px;
            font-size: 14px;
            margin-left: 10px;
        }
    </style>
</head>
<body>
    <h1>ElevenLabs Phone Integration</h1>

    <div class="tabs">
        <div class="tab active" data-step="1">Step 1: Create Phone Number</div>
        <div class="tab" data-step="2">Step 2: Update Phone Number</div>
        <div class="tab" data-step="3">Step 3: Generate Talk-to Link</div>
    </div>

    <div class="container">
        <!-- Step 1: Create Phone Number -->
        <div class="step-content active" id="step1">
            <h2>Step 2: Create Phone Number</h2>
            <div class="form-group">
                <label for="apiKey1">ElevenLabs API Key:</label>
                <input type="text" id="apiKey1" placeholder="sk_...">
            </div>
            
            <div class="form-group">
                <label for="phoneNumber">Phone Number:</label>
                <input type="text" id="phoneNumber" placeholder="+1234567890">
            </div>
            
            <div class="form-group">
                <label for="label">Label:</label>
                <input type="text" id="label" placeholder="My Phone Number">
            </div>
            
            <div class="form-group">
                <label for="sid">SID:</label>
                <input type="text" id="sid" placeholder="Enter SID">
            </div>
            
            <div class="form-group">
                <label for="token">Token:</label>
                <input type="text" id="token" placeholder="Enter token">
            </div>
            
            <button id="createPhoneBtn">Create Phone Number</button>
            <div id="phoneResponse" class="response"></div>

            <div class="code-block">
                <h3>Equivalent curl command:</h3>
                <pre id="phoneCurlCommand"></pre>
            </div>

            <div class="navigation">
                <div></div>
                <button id="nextToStep2" disabled>Next Step &rarr;</button>
            </div>
        </div>

        <!-- Step 3: Update Phone Number -->
        <div class="step-content" id="step2">
            <h2>Step 2: Update Phone Number with Agent ID</h2>
            <p class="info-text">This step allows you to connect your phone number to an agent using either Python code or a curl command.</p>
            <div class="form-group">
                <label for="apiKey2">ElevenLabs API Key:</label>
                <input type="text" id="apiKey2" placeholder="sk_...">
            </div>
            
            <div class="form-group">
                <label for="phoneNumberId">Phone Number ID:</label>
                <input type="text" id="phoneNumberId" placeholder="TeaqRRdTcIfIu2i7BYfT">
            </div>
            
            <div class="form-group">
                <label for="agentId">Agent ID:</label>
                <input type="text" id="agentId" placeholder="Enter agent ID">
            </div>
            
            <button id="updatePhoneBtn">Update Phone Number</button>
            <div id="updateResponse" class="response"></div>

            <div class="form-group">
                <label for="pythonCode">Python Code:</label>
                <textarea id="pythonCode" readonly></textarea>
                <button id="copyPythonBtn">Copy Code</button>
            </div>
            
            <div class="form-group">
                <label for="pythonCode">Python Code:</label>
                <textarea id="pythonCode" readonly></textarea>
                <button id="copyPythonBtn">Copy Code</button>
            </div>
            
            <div class="form-group">
                <label for="curlUpdateCommand">Curl Command (Alternative to Python):</label>
                <textarea id="curlUpdateCommand" readonly></textarea>
                <button id="copyCurlUpdateBtn">Copy Curl</button>
            </div>
            
            <div class="form-group">
                <label for="widgetCommand">Get Agent Widget Curl Command:</label>
                <textarea id="widgetCommand" readonly></textarea>
                <button id="copyWidgetBtn">Copy Curl</button>
            </div>

            <div class="navigation">
                <button id="backToStep1">&larr; Previous Step</button>
                <button id="nextToStep3" disabled>Next Step &rarr;</button>
            </div>
        </div>

        <!-- Step 4: Generate Talk-to Link -->
        <div class="step-content" id="step3">
            <h2>Step 3: Generate Talk-to Link</h2>
            <div class="form-group">
                <label for="agentIdForLink">Agent ID:</label>
                <input type="text" id="agentIdForLink" placeholder="Enter agent ID">
            </div>
            
            <button id="generateLinkBtn">Generate Link</button>
            
            <div class="form-group" style="margin-top: 20px;">
                <label for="talkToLink">Talk-to Link:</label>
                <input type="text" id="talkToLink" readonly>
                <button id="copyAgentLinkBtn">Copy Link</button>
            </div>
            
            <div id="linkPreview" style="margin-top: 20px;">
                <a id="talkToLinkBtn" class="link-button" target="_blank">Open Link in New Tab</a>
            </div>

            <div class="navigation">
                <button id="backToStep2">&larr; Previous Step</button>
                <div></div>
            </div>
        </div>
    </div>

    <script>
        // Global variables to store response data
        let phoneNumberIdFromResponse = "";
        let agentIdFromStep2 = "";
        
        // Initialize tab navigation
        document.querySelectorAll('.tab').forEach(tab => {
            tab.addEventListener('click', () => {
                const stepNumber = tab.getAttribute('data-step');
                activateTab(stepNumber);
            });
        });
        
        function activateTab(stepNumber) {
            // Update tabs
            document.querySelectorAll('.tab').forEach(t => {
                t.classList.remove('active');
            });
            document.querySelector(`.tab[data-step="${stepNumber}"]`).classList.add('active');
            
            // Update content
            document.querySelectorAll('.step-content').forEach(content => {
                content.classList.remove('active');
            });
            document.getElementById(`step${stepNumber}`).classList.add('active');
        }
        
        // Copy API key between steps
        document.getElementById('apiKey1').addEventListener('input', function() {
            document.getElementById('apiKey2').value = this.value;
        });
        
        // Step 1: Create Phone Number
        document.getElementById('createPhoneBtn').addEventListener('click', function() {
            const apiKey = document.getElementById('apiKey1').value;
            const phoneNumber = document.getElementById('phoneNumber').value;
            const label = document.getElementById('label').value;
            const sid = document.getElementById('sid').value;
            const token = document.getElementById('token').value;
            
            if (!apiKey) {
                alert('Please enter your ElevenLabs API key');
                return;
            }
            
            // Build request payload
            const payload = {
                phone_number: phoneNumber,
                label: label,
                sid: sid,
                token: token
            };
            
            // Update curl command display
            const curlCmd = `curl -X POST https://api.elevenlabs.io/v1/convai/phone-numbers/create \\
     -H "xi-api-key: ${apiKey}" \\
     -H "Content-Type: application/json" \\
     -d '${JSON.stringify(payload, null, 2)}'`;
            
            document.getElementById('phoneCurlCommand').textContent = curlCmd;
            
            // Make API request
            fetch('https://api.elevenlabs.io/v1/convai/phone-numbers/create', {
                method: 'POST',
                headers: {
                    'xi-api-key': apiKey,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                const responseElement = document.getElementById('phoneResponse');
                responseElement.textContent = JSON.stringify(data, null, 2);
                responseElement.style.display = 'block';
                
                // Store phone number ID for next step if available
                if (data.phone_number_id) {
                    phoneNumberIdFromResponse = data.phone_number_id;
                    document.getElementById('phoneNumberId').value = phoneNumberIdFromResponse;
                    
                    // Enable next button
                    document.getElementById('nextToStep2').disabled = false;
                }
            })
            .catch(error => {
                const responseElement = document.getElementById('phoneResponse');
                responseElement.textContent = `Error: ${error.message}`;
                responseElement.style.display = 'block';
            });
        });
        
        // Step 2: Update Phone Number
        document.getElementById('updatePhoneBtn').addEventListener('click', function() {
            const apiKey = document.getElementById('apiKey2').value;
            const phoneNumberId = document.getElementById('phoneNumberId').value;
            const agentId = document.getElementById('agentId').value;
            
            if (!apiKey) {
                alert('Please enter your ElevenLabs API key');
                return;
            }
            
            if (!phoneNumberId) {
                alert('Please enter the Phone Number ID');
                return;
            }
            
            if (!agentId) {
                alert('Please enter the Agent ID');
                return;
            }
            
            // Store agent ID for step 3
            agentIdFromStep2 = agentId;
            document.getElementById('agentIdForLink').value = agentIdFromStep2;
            
            // Generate and display Python code
            const pythonCode = `from elevenlabs import ElevenLabs
client = ElevenLabs(api_key="${apiKey}")        
client.conversational_ai.update_phone_number(
    phone_number_id="${phoneNumberId}",
    agent_id="${agentId}"
)`;
            
            document.getElementById('pythonCode').value = pythonCode;
            
            // Generate curl update command
            const curlUpdateCmd = `curl -X PATCH https://api.elevenlabs.io/v1/convai/phone-numbers/${phoneNumberId} \\
     -H "xi-api-key: ${apiKey}" \\
     -H "Content-Type: application/json" \\
     -d '{
  "agent_id": "${agentId}"
}'`;
            
            document.getElementById('curlUpdateCommand').value = curlUpdateCmd;
            
            // Generate widget curl command
            const widgetCmd = `curl https://api.elevenlabs.io/v1/convai/agents/${agentId}/widget \\
     -H "xi-api-key: ${apiKey}"`;
            
            document.getElementById('widgetCommand').value = widgetCmd;
            
            // Make API request (this is pseudo-code as we don't actually call this from browser)
            document.getElementById('updateResponse').textContent = "To execute the Python code, please copy it and run in your Python environment.\n\nThe code will update your phone number to use the specified agent.";
            document.getElementById('updateResponse').style.display = 'block';
            
            // Enable next button
            document.getElementById('nextToStep3').disabled = false;
        });
        
        // Step 3: Generate Talk-to Link
        document.getElementById('generateLinkBtn').addEventListener('click', function() {
            const agentId = document.getElementById('agentIdForLink').value;
            
            if (!agentId) {
                alert('Please enter the Agent ID');
                return;
            }
            
            const talkToLink = `https://elevenlabs.io/app/talk-to?agent_id=${agentId}`;
            
            document.getElementById('talkToLink').value = talkToLink;
            
            // Update link button
            const linkButton = document.getElementById('talkToLinkBtn');
            linkButton.href = talkToLink;
            linkButton.style.display = 'inline-block';
        });
        
        // Navigation buttons
        document.getElementById('nextToStep2').addEventListener('click', function() {
            activateTab('2');
        });
        
        document.getElementById('nextToStep3').addEventListener('click', function() {
            activateTab('3');
        });
        
        document.getElementById('backToStep1').addEventListener('click', function() {
            activateTab('1');
        });
        
        document.getElementById('backToStep2').addEventListener('click', function() {
            activateTab('2');
        });
        
        // Copy buttons
        document.getElementById('copyPythonBtn').addEventListener('click', function() {
            const pythonCode = document.getElementById('pythonCode');
            pythonCode.select();
            document.execCommand('copy');
            this.textContent = "Copied!";
            setTimeout(() => {
                this.textContent = "Copy Code";
            }, 2000);
        });
        
        document.getElementById('copyCurlUpdateBtn').addEventListener('click', function() {
            const curlCmd = document.getElementById('curlUpdateCommand');
            curlCmd.select();
            document.execCommand('copy');
            this.textContent = "Copied!";
            setTimeout(() => {
                this.textContent = "Copy Curl";
            }, 2000);
        });
        
        document.getElementById('copyWidgetBtn').addEventListener('click', function() {
            const widgetCmd = document.getElementById('widgetCommand');
            widgetCmd.select();
            document.execCommand('copy');
            this.textContent = "Copied!";
            setTimeout(() => {
                this.textContent = "Copy Curl";
            }, 2000);
        });
        
        document.getElementById('copyAgentLinkBtn').addEventListener('click', function() {
            const linkInput = document.getElementById('talkToLink');
            linkInput.select();
            document.execCommand('copy');
            this.textContent = "Copied!";
            setTimeout(() => {
                this.textContent = "Copy Link";
            }, 2000);
        });
    </script>
</body>
</html>""")

def update_app_py():
    """Modify app.py to add routes for our dashboard"""
    # Check if app.py exists
    if not os.path.exists('app.py'):
        print("Error: app.py not found. Please make sure you're in the correct directory.")
        return False
    
    # Read the current app.py
    with open('app.py', 'r', encoding='utf-8') as f:
        app_content = f.read()
    
    # Check if we need to add routes
    routes_needed = True
    if '@app.route(\'/dashboard\')' in app_content:
        routes_needed = False
    
    if routes_needed:
        # Find the point where routes are defined
        route_insert_point = app_content.find('@app.route')
        if route_insert_point == -1:
            print("Warning: Could not find a good place to add routes in app.py")
            return False
        
        # New routes to add
        new_routes = """
@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/agent-creator.html')
def agent_creator():
    return render_template('agent-creator.html')

@app.route('/phone-integration.html')
def phone_integration():
    return render_template('phone-integration.html')

"""
        # Insert new routes
        updated_content = app_content[:route_insert_point] + new_routes + app_content[route_insert_point:]
        
        # Write back to app.py
        with open('app.py', 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print("Updated app.py with new routes")
    
    return True

if __name__ == "__main__":
    print("Setting up ElevenLabs Integration Dashboard...")
    
    # Create necessary files
    create_index_template()
    create_html_files()
    
    # Update app.py
    if update_app_py():
        print("Successfully set up the dashboard!")
        
        # Start the Flask app
        print("\nStarting the Flask application...")
        
        # Open browser
        threading.Thread(target=open_browser).start()
        
        # Run the app.py file
        subprocess.run(["python", "app.py"])
    else:
        print("There was an issue updating app.py. Please check the file structure.")