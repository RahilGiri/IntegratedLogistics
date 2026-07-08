import glob

html_files = glob.glob('*.html')

old_str = 'style="height: 60px; filter: brightness(0) invert(1);"'
new_str = 'style="height: 60px; background-color: var(--paper); padding: 5px; border-radius: 4px;"'

for f in html_files:
    with open(f, 'r') as file:
        content = file.read()
    
    new_content = content.replace(old_str, new_str)
    
    if content != new_content:
        with open(f, 'w') as file:
            file.write(new_content)
        print(f"Updated {f}")

