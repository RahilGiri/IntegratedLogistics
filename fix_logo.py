import glob

files = glob.glob('*.html')

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    content = content.replace('style="height: 60px;"', 'class="header-logo-img"')
    content = content.replace('style="height: 50px;"', 'class="mobile-logo-img"')
    
    with open(f, 'w') as file:
        file.write(content)

