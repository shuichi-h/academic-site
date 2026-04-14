# AI Agent Instructions for Academic Pages Codebase

## Project Overview
This is an **Academic Pages** Jekyll-based personal portfolio website for researchers. The site dynamically generates academic content (publications, talks, teaching materials) from structured data. It's a heavily customized fork of the Minimal Mistakes theme, deployed to GitHub Pages at `https://shuichi-h.github.io/academic-site`.

## Architecture & Key Concepts

### Content Collections (Jekyll-specific)
The site uses **four primary Jekyll collections** that auto-generate pages:
- `_publications/` → individual publication pages with citations
- `_talks/` → conference talks and presentations  
- `_teaching/` → teaching materials
- `_posts/` → blog-style research notes

**Pattern**: Each collection has a front matter with metadata + content. Collections are rendered by `_layouts/` templates and filtered/listed by `_includes/` partials.

### Data-Driven Generation Workflow
`markdown_generator/` Python scripts convert tabular source data (TSV files) into Jekyll collection files:
- **Input**: `publications.tsv`, `talks.tsv` (tab-separated structured data)
- **Process**: Python scripts parse TSV, escape HTML/YAML special chars, generate markdown with YAML front matter
- **Output**: Individual `.md` files in `_publications/`, `_talks/` directories
- **Tools**: Jupyter notebooks (`.ipynb`) + pure Python equivalents (`.py`)

**Critical convention**: Use this workflow when bulk-adding content; don't manually create individual files for dozens of publications.

### Theme & Styling
- **Theme**: Minimal Mistakes (customized) with theme selection in `_config.yml` (`site_theme: "default"`)
- **Customizable themes**: "default", "air", "sunrise", "mint", "dirt", "contrast"
- **Styles**: `_sass/` organized as:
  - `_syntax.scss` - code highlighting
  - `_themes.scss` - theme variables
  - `vendor/` - third-party assets
  - `layout/`, `theme/`, `include/` - component styling

### Configuration Hierarchy
1. **Primary**: `_config.yml` (base config, auto-reload not supported—restart Jekyll after changes)
2. **Docker**: `_config_docker.yml` (container-specific overrides)
3. **Author metadata**: `_data/authors.yml` (multi-author support)
4. **Site metadata**: `_data/navigation.yml`, `_data/ui-text.yml`

## Local Development Workflow

### Quick Start (macOS)
```bash
brew install ruby node
gem install bundler
bundle install
bundle exec jekyll serve -l -H localhost
```
Site runs at `localhost:4000`. Changes to `.md` files auto-rebuild; changes to `_config.yml` require Jekyll restart.

### Using Docker (Recommended for consistency)
```bash
chmod -R 777 .
docker compose up
```
Access at `localhost:4000`. Eliminates Ruby/gem version issues.

### Using VS Code Dev Container
Press **F1** → "DevContainer: Reopen in Container" for automatic setup + local hosting.

### Troubleshooting
- **Permission errors**: `bundle config set --local path 'vendor/bundle'` then `bundle install`
- **Build failures**: Delete `Gemfile.lock` and retry `bundle install`
- **Dependency missing on Linux**: `sudo apt install build-essential gcc make`

## Content Conventions

### YAML Front Matter Standards
**Publications** (`_publications/YYYY-MM-DD-slug.md`):
```yaml
---
title: "Paper Title"
collection: publications
category: conferences  # books, manuscripts, conferences
permalink: /publication/YYYY-MM-DD-slug
venue: "Conference Name"
date: YYYY-MM-DD
paperurl: "https://..."
citation: 'Author. "Title." Journal. Year.'
---
```

**Talks** (`_talks/YYYY-MM-DD-slug.md`):
```yaml
---
title: "Talk Title"
collection: talks
type: "Talk"  # or "Tutorial"
permalink: /talks/YYYY-MM-DD-slug
venue: "Institution"
date: YYYY-MM-DD
location: "City, Country"
---
```

**Posts** (`_posts/YYYY-MM-DD-slug.md`):
```yaml
---
title: "Post Title"
date: YYYY-MM-DD
tags: [tag1, tag2]
author_profile: true
---
```

### URL Structure
- Publications: `/publication/YYYY-MM-DD-slug`
- Talks: `/talks/YYYY-MM-DD-slug`
- Teaching: `/teaching/YYYY-MM-DD-slug`
- Posts: `/posts/YYYY-MM-DD-slug`
- Custom pages: Use `permalink:` in `_pages/` front matter

### Asset Handling
- **Downloadable files**: Place in `files/` directory; link as `{{ site.baseurl }}/files/filename.pdf`
- **Images**: Place in `images/` directory
- **Profile avatar**: `profile.png` in `images/`

## Build & Deployment

### Local Build
```bash
bundle exec jekyll build
# Output: _site/ directory
```

### GitHub Pages Deployment
- Pushes to `main` branch automatically trigger GitHub Actions workflow (`pages-build-deployment`)
- Workflow file: `.github/workflows/`
- Site builds on GitHub's servers; no manual deployment needed

### Environment Variables
- `baseurl: /academic-site` in `_config.yml` (relative path for GitHub Pages)
- `url: https://shuichi-h.github.io` (full domain)

## Dependencies & Tech Stack
- **Jekyll** 4.x (Ruby static site generator)
- **Gems**: jekyll-feed, jekyll-sitemap, jekyll-redirect-from, jemoji (emoji support), webrick
- **Node packages**: jQuery, Plotly.js, fitvids, smooth-scroll (for JS minification)
- **Python**: pandas (markdown_generator scripts use this for TSV parsing)

## Key Files to Know
- `_config.yml` - Site configuration, author metadata
- `_layouts/default.html` - Base template structure
- `_includes/masthead.html` - Navigation bar
- `_includes/author-profile.html` - Sidebar author card
- `assets/js/_main.js` - Main JavaScript logic
- `markdown_generator/publications.py` - Publication TSV converter

## Common Tasks

### Add a Publication
**Option A (Bulk)**: Update `markdown_generator/publications.tsv`, run `markdown_generator/publications.py`
**Option B (Single)**: Create `_publications/YYYY-MM-DD-slug.md` with front matter + excerpt

### Add a Talk
**Option A (Bulk)**: Update `markdown_generator/talks.tsv`, run `markdown_generator/talks.py`
**Option B (Single)**: Create `_talks/YYYY-MM-DD-slug.md` with YAML front matter

### Add a Custom Page
Create in `_pages/page-name.md` with:
```yaml
---
title: "Page Title"
permalink: /page-name/
layout: single
---
```

### Change Site Theme
Edit `_config.yml`: `site_theme: "air"` and restart Jekyll

### Update Author Profile
Edit `_config.yml` `author:` section or `_data/authors.yml`

## Code Style & Patterns

- **Liquid templating**: Jekyll uses Liquid syntax; `{% %}` for logic, `{{ }}` for variables
- **Collections iteration**: Use `site.[collection]` to loop (e.g., `site.publications`, `site.talks`)
- **YAML special chars**: Always escape quotes in metadata with HTML entities (`&quot;`, `&apos;`)
- **Links**: Use `{{ site.baseurl }}` prefix for internal links to respect GitHub Pages subdirectory

## Testing & Validation
- **Local preview**: Always test with `jekyll serve` before pushing
- **HTML validation**: Check generated `_site/` HTML for broken links
- **CI/CD**: GitHub Actions validates build on every push to `main`
