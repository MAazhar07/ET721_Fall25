# Lab 19: Simple Django Blog App

This is a basic blog application built with Django. Users can:
- View a list of all blog posts.
- View details of a single post.
- Create new blog posts.
- Edit existing blog posts.

Built using Django models, views (class-based), templates, forms, and URL routing. Includes basic CSS styling.

## Features
- **Models**: `BlogPost` with title, content, created_at, updated_at.
- **Views**: List, Detail, Create, Update.
- **Templates**: Base layout + post_list.html, post_detail.html, post_form.html.
- **Forms**: ModelForm for creating/editing posts.
- **Styling**: Simple CSS in `static/blog/styles.css`.
- **Database**: SQLite (default).

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd lab19