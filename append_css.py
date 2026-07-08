css_append = """
/* Logo Sizing & Alignment */
.header-logo-img {
  height: 75px; 
  width: auto;
  object-fit: contain;
}

.mobile-logo-img {
  height: 60px; 
  width: auto;
  object-fit: contain;
}

@media (max-width: 900px) {
  .header-logo-img {
    height: 65px;
    margin-left: 15px; 
  }
}

@media (max-width: 600px) {
  .header-logo-img {
    height: 55px;
    margin-left: 10px; 
  }
}
"""

with open('css/style.css', 'a') as f:
    f.write(css_append)

