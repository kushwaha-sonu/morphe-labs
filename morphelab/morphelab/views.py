import os
import subprocess
from datetime import datetime, timedelta
from django.http import HttpResponse

def get_server_time_ist():
    ist_time = datetime.utcnow() + timedelta(hours=5, minutes=30)  # IST (UTC+5:30)
    return ist_time.strftime('%Y-%m-%d %H:%M:%S')

def get_top_output():
    try:
        result = subprocess.run(['top', '-bn1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except Exception as e:
        return f"Error running 'top' command: {str(e)}"

def htop(request):
    name = "Sonu Kumar"  # Replace with your actual name
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"
    server_time = get_server_time_ist()
    top_output = get_top_output()

    html_content = f"""
    <html>
        <head><title>System Info</title></head>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h2>TOP Output:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return HttpResponse(html_content)
