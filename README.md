# Yellow Brick Road Counseling & Therapy Website

A static website for Yellow Brick Road Counseling & Therapy built with HTML, CSS, and JavaScript for easy deployment to GitHub Pages.

## Project Structure

```
├── index.html                      # Main homepage
├── therapist-bio-brittani.html     # Brittani's bio page
├── therapist-bio-holly.html        # Holly's bio page
├── static/
│   ├── css/                        # Stylesheets
│   ├── js/                         # JavaScript files
│   ├── img/                        # Images and icons
│   ├── scss/                       # SCSS source files (for development)
│   └── vendor/                     # Third-party libraries (Bootstrap, AOS, etc.)
└── data/
    └── bio.json                    # Therapist information (reference)
```

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/amliston/yellow-brick-road.git
   cd yellow-brick-road
   ```

2. **Open locally:**
   - Open `index.html` in a web browser
   - Or use a local server (Python, Node.js, etc.)

## Deployment

### GitHub Pages

This is a static website ready for GitHub Pages:

1. Go to your repository settings
2. Navigate to **Pages** section
3. Set source to `main` branch
4. Your site will be available at `https://amliston.github.io/yellow-brick-road/`

### Other Hosting

Works with any static hosting:
- Netlify
- Vercel
- Traditional web hosting (FTP/SFTP)

## External Services Integration

### Contact Forms

The contact form currently points to a placeholder. Update it to use:
- **Formspree** (free tier available): Replace the form action URL in `index.html`
- **EmailJS** (serverless)
- **Basin** (simple form endpoint)

Update line in `index.html`:
```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```

### Appointment Scheduling

Recommended services:
- **Calendly** - Embed widget in footer or dedicated page
- **Acuity Scheduling** - More features, similar setup
- **Simple Calendar** - Lightweight alternative

## Development

### Editing Content

All pages are plain HTML files. Edit directly:
- `index.html` - Home page with sections
- `therapist-bio-brittani.html` - Brittani's profile
- `therapist-bio-holly.html` - Holly's profile

### Styling

- Main CSS: `static/css/main.css`
- SCSS sources in `static/scss/` (for development only)

To compile SCSS → CSS, use a tool like VS Code's Live Sass Compiler or command line:
```bash
sass static/scss/main.scss static/css/main.css
```

### JavaScript

Main JS file: `static/js/main.js` handles:
- Navigation
- Animations (AOS)
- Scroll behavior
- Gallery lightbox

## Key Dependencies

All third-party libraries included in `static/vendor/`:
- **Bootstrap 5.x** - Responsive layout framework
- **Bootstrap Icons** - Icon library
- **AOS** (Animate On Scroll) - Scroll animations
- **GLightbox** - Image gallery lightbox
- **Swiper** - Carousel/slider

## Notes

- All paths are relative (`./static/...`) for GitHub Pages compatibility
- The original Flask backend (`ybr.py`) is no longer needed for this static version
- Forms and appointments are handled via external services

## Contact

For questions about the website, contact the YBR team.
