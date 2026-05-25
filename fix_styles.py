import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix .services-menu bounds (El menu de opciones aun no se ve dentro de los limites...)
# Find .services-menu block and update to make it responsive
content = re.sub(
    r'\.services-menu \{[^}]*min-width: 320px;[^}]*\}',
    r'.services-menu {\n      position: absolute;\n      right: -10px;\n      top: calc(100% + 10px);\n      min-width: 260px;\n      max-width: 90vw;\n      background: var(--surface);\n      color: var(--text);\n      border-radius: var(--radius-lg);\n      box-shadow: var(--shadow-xl);\n      border: 1px solid var(--border);\n      padding: 8px;\n      opacity: 0;\n      visibility: hidden;\n      transform: translateY(-6px) scale(.98);\n      transition: opacity var(--transition), transform var(--transition), visibility var(--transition);\n      z-index: 60;\n    }',
    content
)

# Also fix the inline styles on the inner service menus to prevent overflow on mobile
content = content.replace(
    'style="left: 0; right: auto;"',
    'style="left: 0; right: auto; min-width: 250px; max-width: calc(100vw - 40px);"'
)


# 2. Fix the login logo (en el login quitale el backgraund que tiene el logo agrandalo un poco)
login_logo_css = """
    .login-brand .brand-logo {
      background: transparent;
      border-radius: 0;
      padding: 0;
      box-shadow: none;
      max-width: 100%;
    }

    .login-brand .brand-logo img {
      display: block;
      max-width: 380px;
      max-height: 180px;
      object-fit: contain;
    }
"""
content = re.sub(
    r'\.login-brand \.brand-logo\s*\{[^}]*\}[\s\S]*?\.login-brand \.brand-logo img\s*\{[^}]*\}',
    login_logo_css.strip(),
    content
)

# 3. Fix the system logo (el logo dentr del sistema el backgirund debe ser blanco y ajustarlo de manera que se vea)
# Report logo:
report_logo_css = """
    .logo {
      border: none;
      border-radius: var(--radius-lg);
      min-height: 110px;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      color: var(--muted);
      font-size: 12px;
      padding: 12px 16px;
      background: #ffffff;
    }

    .logo img {
      max-width: 100%;
      max-height: 100px;
      object-fit: contain;
      display: block;
    }
"""
content = re.sub(
    r'\.logo\s*\{[^}]*\}[\s\S]*?\.logo img\s*\{[^}]*\}',
    report_logo_css.strip(),
    content
)

# Topbar logo
topbar_logo_css = """
    .appbar-logo {
      width: 50px;
      height: 50px;
      border-radius: 8px;
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 4px;
      box-shadow: var(--shadow-sm);
    }
    .appbar-logo img { width: 100%; height: 100%; object-fit: contain; display: block; }
"""
content = re.sub(
    r'\.appbar-logo\s*\{[^}]*\}[\s\S]*?\.appbar-logo img\s*\{[^}]*\}',
    topbar_logo_css.strip(),
    content
)

# Fix inner header logos for Novedades as well
nc_logo_css = """
    .nc-header .nc-logo {
      width: 100%; height: 92px;
      border-radius: var(--radius-md);
      background: #ffffff;
      border: none;
      display: flex; align-items: center; justify-content: center;
      padding: 6px;
    }
"""
content = re.sub(
    r'\.nc-header \.nc-logo\s*\{[^}]*\}',
    nc_logo_css.strip(),
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

