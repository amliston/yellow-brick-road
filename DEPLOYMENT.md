# Deployment Guide

## Static Site Ready ✓

This website is now a **static site** compatible with GitHub Pages and other static hosting platforms. No backend server needed.

## Removed Components

- **ybr.py** (Flask backend) - No longer needed
- **forms/contact.php** - Handled via external service
- **Jinja2 templating** - Converted to plain HTML
  - `base.html` - Merged into each page
  - `index.html` - Standalone with full HTML structure
  - `therapist-bio-*.html` - Standalone pages

## Path Changes

All asset paths updated from absolute to relative:
- ❌ `/static/css/main.css` → ✓ `./static/css/main.css`
- ❌ `/bio/Holly` → ✓ `./therapist-bio-holly.html`
- ❌ `/forms/contact` → ✓ External form service URLs

This allows the site to work:
- Locally (file://)
- On GitHub Pages
- Any domain without URL rewriting

## External Service Setup

### 1. Contact Form (Required)

Pick one and update `index.html` form action:

**Option A: Formspree (Recommended)**
1. Go to https://formspree.io
2. Create new form, get form ID
3. Update in `index.html` line ~460:
```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```

**Option B: EmailJS (JavaScript-based)**
- Requires JavaScript setup
- More control, but clientside

**Option C: Basin (Simple endpoint)**
1. Go to https://basinapp.com
2. Create form, get endpoint URL
3. Update form action

### 2. Appointment Scheduling (Recommended)

**Calendly Option:**
1. Create account at https://calendly.com
2. Set up availability
3. Embed widget or link from website

Add to `index.html` footer or contact section:
```html
<a href="https://calendly.com/your-link" target="_blank">Book Appointment</a>
```

Or embed with:
```html
<div class="calendly-inline-widget" data-url="https://calendly.com/your-url?hide_event_type=1" style="height:630px;"></div>
<script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
```

## GitHub Pages Deployment

1. **Initial Setup:**
   ```bash
   cd yellow-brick-road
   git add .
   git commit -m "Convert to static site for GitHub Pages"
   git push origin main
   ```

2. **Configure Repository:**
   - Go to repo → Settings → Pages
   - Source: `main` branch, `/root` directory
   - Save

3. **Site Live:**
   - Available at: `https://amliston.github.io/yellow-brick-road/`
   - (May take 5-10 minutes to deploy)

## Alternative Hosting

### Netlify
1. Connect GitHub repo
2. Build settings: Leave blank (static)
3. Deploy automatically on push

### Vercel
1. Import project
2. Framework: None
3. Deploy

### Traditional Hosting (cPanel, etc.)
1. Download as ZIP
2. Upload all files via FTP/cPanel file manager
3. Point domain to hosting

## Testing Locally

**Python 3:**
```bash
python -m http.server 8000
# Visit http://localhost:8000
```

**Python 2:**
```bash
python -m SimpleHTTPServer 8000
```

**Node.js:**
```bash
npx http-server
```

**VS Code:**
- Install "Live Server" extension
- Right-click `index.html` → "Open with Live Server"

## SEO & Meta Tags

Update these in HTML files:
- `<title>` - Page title (important for SEO)
- `<meta name="description">` - Google snippet preview
- `<meta name="keywords">` - Keywords (less important now)
- `<meta name="viewport">` - Already set for mobile ✓

Example for bio pages:
```html
<meta name="description" content="Meet Holly Merrick-Liston, LPC-MH therapist specializing in trauma and EMDR therapy in Sioux Falls.">
```

## Performance Notes

Current setup includes:
- Bootstrap for responsive layout ✓
- No database queries ✓
- Minimal JavaScript ✓
- Fast load times ✓
- Mobile optimized ✓

## Troubleshooting

**Forms not submitting:**
- Verify form action URL (Formspree/other service)
- Check browser console for errors
- Test independently on service website

**Images not loading:**
- Verify relative paths: `./static/img/...`
- Check file exists in that location
- File names are case-sensitive

**Navigation links broken:**
- All links should use relative paths: `./index.html`, `./therapist-bio-*.html`
- No leading `/` on file links

**GitHub Pages showing old content:**
- Hard refresh: Ctrl+Shift+R (or Cmd+Shift+R)
- Clear cache or use incognito window
- Verify deployment completed

## Next Steps

1. Set up contact form service
2. Set up appointment scheduler
3. Update contact info (phone, email)
4. Add social media links (footer)
5. Deploy to GitHub Pages
6. Configure custom domain (optional)
