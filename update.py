import os

files = ['index.html', 'about.html', 'services.html', 'network.html', 'gallery.html', 'contact.html']

logo_main_old = """            <a href="index.html" class="logo">
                <svg viewBox="0 0 100 100" aria-label="Integrated Logistics Logo">
                    <path d="M20 20 L40 20 L40 80 L80 80 L80 90 L20 90 Z" fill="var(--maroon)" />
                    <path d="M40 20 L55 20 L55 90 L40 90 Z" fill="var(--maroon)" opacity="0.8"/>
                </svg>
                <div class="logo-text">
                    <span class="logo-title">Integrated Logistics</span>
                    <span class="logo-subtitle">On Schedule</span>
                </div>
            </a>"""

logo_main_new = """            <a href="index.html" class="logo">
                <img src="images/logo.png" alt="Integrated Logistics" style="height: 60px;">
            </a>"""

logo_mob_old = """                <div class="navbar-top">
                    <div class="logo-text">
                        <span class="logo-title">Integrated Logistics</span>
                        <span class="logo-subtitle">On Schedule</span>
                    </div>
                    <button class="nav-close-btn" aria-label="Close menu"><ion-icon name="close-outline"></ion-icon></button>
                </div>"""

logo_mob_new = """                <div class="navbar-top">
                    <img src="images/logo.png" alt="Integrated Logistics" style="height: 50px;">
                    <button class="nav-close-btn" aria-label="Close menu"><ion-icon name="close-outline"></ion-icon></button>
                </div>"""

logo_foot_old = """                    <div class="logo">
                        <svg viewBox="0 0 100 100" style="height: 40px;">
                            <path d="M20 20 L40 20 L40 80 L80 80 L80 90 L20 90 Z" fill="var(--gold)" />
                            <path d="M40 20 L55 20 L55 90 L40 90 Z" fill="var(--gold)" opacity="0.8"/>
                        </svg>
                        <div class="logo-text">
                            <span class="logo-title" style="color:var(--paper);">Integrated Logistics</span>
                            <span class="logo-subtitle" style="color:var(--gold);">On Schedule</span>
                        </div>
                    </div>"""

logo_foot_new = """                    <div class="logo">
                        <img src="images/logo.png" alt="Integrated Logistics" style="height: 60px; filter: brightness(0) invert(1);">
                    </div>"""

for f in files:
    if os.path.exists(f):
        with open(f, 'r') as file:
            content = file.read()
        
        content = content.replace(logo_main_old, logo_main_new)
        content = content.replace(logo_mob_old, logo_mob_new)
        content = content.replace(logo_foot_old, logo_foot_new)
        
        content = content.replace('                    <li><a href="track.html" class="navbar-link">Track <ion-icon name="chevron-forward"></ion-icon></a></li>\n', '')
        content = content.replace('                        <li><a href="track.html" class="footer-link"><ion-icon name="chevron-forward"></ion-icon> Track Shipment</a></li>\n', '')
        content = content.replace('                        <a href="track.html" class="btn">Track Shipment</a>\n', '')
        
        with open(f, 'w') as file:
            file.write(content)
print("Updated successfully")
