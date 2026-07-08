import os
import glob

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r') as file:
        content = file.read()
    
    new_content = content.replace('images/logo.png', 'images/logointegrated.png')
    
    if content != new_content:
        with open(f, 'w') as file:
            file.write(new_content)
        print(f"Updated {f}")

