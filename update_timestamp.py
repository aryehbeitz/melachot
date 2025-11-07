#!/usr/bin/env python3
from datetime import datetime
import pytz

# Get current time in Israel timezone
israel_tz = pytz.timezone('Asia/Jerusalem')
now = datetime.now(israel_tz)

# Format the timestamp
timestamp = now.strftime('%B %d, %Y at %H:%M:%S')

# Read the JavaScript file
with open('js/main.js', 'r') as f:
    js_content = f.read()

# Replace the timestamp in the code
# Look for the line with DEPLOYMENT_TIME constant
if 'const DEPLOYMENT_TIME =' in js_content:
    # Update existing timestamp
    import re
    js_content = re.sub(
        r"const DEPLOYMENT_TIME = '[^']*';",
        f"const DEPLOYMENT_TIME = '{timestamp} (Israel Time)';",
        js_content
    )
else:
    # Add the timestamp constant at the beginning of the file
    js_content = f"// Deployment timestamp\nconst DEPLOYMENT_TIME = '{timestamp} (Israel Time)';\n\n" + js_content

# Write back
with open('js/main.js', 'w') as f:
    f.write(js_content)

print(f"✓ Updated deployment timestamp to: {timestamp} (Israel Time)")
