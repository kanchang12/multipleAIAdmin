import os

# Function to update app.py to fix dashboard routes
def update_app_py():
    # Check if app.py exists
    if not os.path.exists('app.py'):
        print("Error: app.py not found. Please make sure you're in the correct directory.")
        return False
    
    # Read the current app.py
    try:
        with open('app.py', 'r', encoding='utf-8') as f:
            app_content = f.read()
    except UnicodeDecodeError:
        # Try with default encoding if UTF-8 fails
        with open('app.py', 'r') as f:
            app_content = f.read()
    
    # Add dashboard as a separate route (not overriding the index route)
    dashboard_route = """
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

    # Check if routes are already added
    if '@app.route(\'/dashboard\')' in app_content:
        print("Dashboard routes already exist in app.py")
    else:
        # Find a good insertion point - after the imports but before the routes
        import_section_end = app_content.find('app = Flask')
        if import_section_end == -1:
            # If we can't find Flask initialization, look for import section
            import_section_end = max(app_content.rfind('import'), app_content.rfind('from'))
            if import_section_end == -1:
                # If we can't even find imports, just insert at the beginning
                insertion_point = 0
            else:
                # Find the end of the line where the last import statement is
                insertion_point = app_content.find('\n', import_section_end) + 1
        else:
            # Find the end of the line where app is initialized
            insertion_point = app_content.find('\n', import_section_end) + 1
        
        # Insert the dashboard routes
        updated_content = app_content[:insertion_point] + dashboard_route + app_content[insertion_point:]
        
        # Write back to app.py
        try:
            with open('app.py', 'w', encoding='utf-8') as f:
                f.write(updated_content)
        except UnicodeEncodeError:
            # Try with default encoding if UTF-8 fails
            with open('app.py', 'w') as f:
                f.write(updated_content)
        
        print("Added dashboard routes to app.py")
    
    return True

# Update batch file to open correct URL
def create_batch_file():
    with open('open_dashboard.bat', 'w') as f:
        f.write("""@echo off
echo Opening ElevenLabs Integration Dashboard...
echo.

REM Start the Flask application in the background
start cmd /c "python app.py"

REM Wait a moment for the app to start
timeout /t 2 > nul

REM Open the dashboard URL
start http://127.0.0.1:5000/dashboard

echo Dashboard opened in your browser.
echo The Flask application is running in a separate window.
echo Do not close that window until you're done using the dashboard.
echo.
pause
""")
    print("Created open_dashboard.bat")
    return True

if __name__ == "__main__":
    print("Setting up ElevenLabs Dashboard access...")
    
    if update_app_py():
        create_batch_file()
        print("\nSetup complete!")
        print("To access the dashboard, double-click 'open_dashboard.bat'")