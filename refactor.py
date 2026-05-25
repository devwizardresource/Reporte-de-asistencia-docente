import re

def update_file():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Fonts
    content = re.sub(
        r'<link href="https://fonts.googleapis.com/css2\?family=Inter:.*?rel="stylesheet">',
        r'<link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@400;500;700&display=swap" rel="stylesheet">',
        content,
        flags=re.DOTALL
    )

    # 2. Update CSS Variables (Facebook style)
    new_vars = """
    :root {
      --primary: #1877F2;
      --primary-dark: #166FE5;
      --primary-deep: #0D4A9B;
      --primary-soft: #E7F3FF;
      --primary-glow: rgba(24, 119, 242, 0.2);
      --accent: #42B72A;
      --accent-soft: #E8FDF1;
      --lavender: #CCD0D5;
      --lavender-mist: #F0F2F5;
      --gold: #F5C33B;
      --gold-soft: #FFF9E6;
      --border: #CED0D4;
      --border-strong: #8A8D91;
      --text: #050505;
      --muted: #65676B;
      --muted-soft: #8A8D91;
      --ok: #42B72A;
      --warn: #F5C33B;
      --danger: #FA3E3E;
      --bg: #F0F2F5;
      --bg-deep: #E4E6EB;
      --surface: #FFFFFF;
      --white: #FFFFFF;
      --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.1);
      --shadow-md: 0 2px 4px rgba(0, 0, 0, 0.1), 0 8px 16px rgba(0, 0, 0, 0.1);
      --shadow-lg: 0 4px 8px rgba(0, 0, 0, 0.1), 0 12px 24px rgba(0, 0, 0, 0.1);
      --shadow-xl: 0 12px 28px rgba(0, 0, 0, 0.2);
      --radius-sm: 6px;
      --radius-md: 8px;
      --radius-lg: 12px;
      --radius-xl: 16px;
      --transition: 200ms ease;
    }

    * { box-sizing: border-box; }

    html, body { height: auto; min-height: 100%; }

    body {
      margin: 0;
      font-family: 'Century Gothic', 'Ubuntu', system-ui, -apple-system, sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    h1, h2, h3, h4 { font-family: 'Century Gothic', 'Ubuntu', sans-serif; font-weight: 700; }
"""
    content = re.sub(
        r':root\s*\{.*?}.*?h1, h2, h3, h4\s*\{.*?\}',
        new_vars.strip(),
        content,
        flags=re.DOTALL
    )

    # 3. Update top app bar colors
    content = re.sub(
        r'\.appbar \{[^}]*background:[^;]*;[^}]*color:[^;]*;',
        r'.appbar {\n      position: sticky;\n      top: 0;\n      z-index: 40;\n      background: var(--surface);\n      color: var(--text);',
        content
    )

    # Fix appbar styling and shadow
    content = re.sub(
        r'\.appbar::after\s*\{.*?\}',
        '',
        content,
        flags=re.DOTALL
    )

    # Fix appbar title color
    content = re.sub(
        r'\.appbar-title strong \{',
        r'.appbar-title strong {\n      color: var(--primary);\n',
        content
    )

    # 4. Fix dropdown to be hover-based
    hover_css = """
    .services-wrap:hover .services-menu {
      opacity: 1;
      visibility: visible;
      transform: translateY(0) scale(1);
    }
    .services-wrap:hover .services-trigger .chev {
      transform: rotate(-135deg) translate(-2px, -2px);
    }
    .services-trigger {
      background: var(--bg);
      color: var(--text);
      border: none;
      padding: 8px 12px;
      border-radius: 6px;
      font-weight: 600;
      cursor: pointer;
    }
    .services-trigger:hover {
      background: var(--bg-deep);
    }
"""
    content = re.sub(r'\.services-trigger\s*\{.*?\}\s*\.services-trigger:hover\s*\{.*?\}\s*\.services-trigger \.chev\s*\{.*?\}\s*\.services-trigger\.open \.chev\s*\{.*?\}', hover_css, content, flags=re.DOTALL)

    # Convert the appbar actions and move .service-actions inside the hover menu
    # The user wanted the rest of the buttons of the top bar in an option that deploys on hover.
    new_appbar_html = """
    <div class="appbar-actions">
      <div class="services-wrap">
        <button type="button" class="services-trigger" id="btnServices" aria-haspopup="true" aria-expanded="false">
          Menú Opciones
          <span class="chev"></span>
        </button>
        <div class="services-menu" id="servicesMenu" role="menu">
          <!-- Dropdown content: Servicios + Sesión -->
          <div style="padding: 8px 12px; border-bottom: 1px solid var(--border); margin-bottom: 8px;">
            <div style="font-weight: bold; font-size: 14px; margin-bottom: 4px;">Mi Cuenta</div>
            <div id="sessionName" style="font-size: 13px; color: var(--muted);">—</div>
            <div class="role-tag" id="sessionRole" style="display:inline-block; margin-top:4px; padding:2px 6px; border-radius:4px; background:var(--gold); color:#000; font-size:10px; font-weight:bold;">docente</div>
          </div>
          <div style="font-weight: bold; font-size: 12px; color: var(--muted); padding: 4px 12px;">Servicios</div>
          <button type="button" class="service-item active" data-service="serviceAttendance" role="menuitem">
            <span class="icon" style="background:var(--primary); color:#fff;">📋</span>
            <span class="meta">
              <b>Control de Asistencia Docente</b>
              <span>Registro y firma de asistencia por fecha de clase.</span>
            </span>
          </button>
          <button type="button" class="service-item" data-service="serviceNovedades" role="menuitem">
            <span class="icon" style="background:var(--primary); color:#fff;">📝</span>
            <span class="meta">
              <b>Reportes de Novedades</b>
              <span>Diligenciamiento del formato institucional.</span>
            </span>
          </button>
          <div style="border-top: 1px solid var(--border); margin-top: 8px; padding-top: 8px;">
            <button id="btnLogout" type="button" class="service-item" style="color: var(--danger);">
               <span class="icon" style="background:#fdecea; color:var(--danger);">🚪</span>
               <span class="meta"><b>Cerrar sesión</b></span>
            </button>
          </div>
        </div>
      </div>
    </div>
"""
    content = re.sub(r'<div class="appbar-actions">.*?</div>\s*</div>\s*</header>', new_appbar_html.strip() + '\n  </header>', content, flags=re.DOTALL)

    # 5. Fix Overflow issues
    content = re.sub(
        r'max-height:\s*calc\(100vh - 108px\);',
        r'/* max-height removed */',
        content
    )
    content = re.sub(
        r'\.panel \{[^}]*\}',
        r'.panel {\n      padding: 22px;\n      align-self: start;\n      position: sticky;\n      top: 88px;\n      overflow: visible;\n    }',
        content
    )
    
    # login wrap grid fix
    content = re.sub(
        r'\.login-wrap\s*\{[^}]*\}',
        r'.login-wrap {\n      width: 100%;\n      max-width: 1280px;\n      margin: auto;\n      display: grid;\n      grid-template-columns: 1.1fr 0.9fr;\n      gap: 40px;\n      padding: 40px 32px;\n      align-items: center;\n      overflow: visible;\n    }',
        content
    )

    # Overhaul buttons CSS
    button_css = """
    button {
      border: none;
      background: var(--surface);
      color: var(--text);
      padding: 10px 16px;
      border-radius: var(--radius-md);
      cursor: pointer;
      font-weight: 600;
      transition: all var(--transition);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }

    button:hover {
      background: var(--bg-deep);
    }

    .btn-primary {
      background: var(--primary);
      color: #fff;
    }
    .btn-primary:hover {
      background: var(--primary-dark);
      color: #fff;
    }

    .btn-ghost {
      background: transparent;
      color: var(--primary);
    }
    .btn-ghost:hover { background: var(--primary-soft); }

    .btn-soft {
      background: var(--primary-soft);
      color: var(--primary-dark);
    }
    .btn-soft:hover { background: #D8EAFC; }

    .btn-danger {
      background: #FA3E3E;
      color: #fff;
    }
    .btn-danger:hover { background: #E12D2D; }
"""
    content = re.sub(r'button\s*\{[^}]*\}[\s\S]*?\.btn-danger:hover\s*\{[^}]*\}', button_css.strip(), content)

    # Save
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_file()
