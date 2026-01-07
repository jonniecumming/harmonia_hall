# Django Project Guidelines

## Core Rule: Always Use Django Best Conventions

**CRITICAL:** Every update to this project MUST follow Django best practices and conventions. Before implementing any feature, always ask: "Does this follow Django conventions?" Apply Django conventions to:

- **Paths & File Locations** - Use standard Django directory structure
- **Naming Conventions** - Follow Django naming standards for models, views, URLs, templates
- **User Authentication** - Use Django's built-in `django.contrib.auth` system
- **Security** - Implement Django's security features (CSRF, password hashing, SQL injection prevention)
- **Logic & Structure** - Use Django patterns for business logic, views, and data models
- **Database Design** - Use Django ORM and migrations properly
- **Testing** - Use Django's TestCase framework
- **Configuration** - Use environment variables for settings

### File Structure & Organization
- Follow Django's standard project layout: `project/` → `manage.py`, apps as subdirectories
- Use `apps.py` for app configuration
- Organize code in standard Django directories: `models/`, `views/`, `templates/`, `static/`, `migrations/`
- Name apps descriptively in lowercase with underscores (e.g., `user_auth`, `blog_posts`)
- Store templates in `app_name/templates/app_name/` directory structure
- Store static files in `app_name/static/app_name/` directory structure

### Naming Conventions
- Model names: `PascalCase` (e.g., `UserProfile`, `BlogPost`)
- Field names: `snake_case` (e.g., `first_name`, `created_at`)
- URL names: `kebab-case` in `urls.py` (e.g., `'user-detail'`, `'blog-list'`)
- View function names: `snake_case_view` (e.g., `list_posts_view`, `create_user_view`)
- Class-based views: `PascalCase` (e.g., `UserListView`, `PostDetailView`)
- Template names: `lowercase_with_underscores.html` (e.g., `user_profile.html`, `blog_post_list.html`)
- Variable names: `snake_case` in templates and Python code

### User Authentication & Authorization
- **Always use** `django.contrib.auth` for user authentication
- Create a custom `User` model extending `AbstractUser` if customization is needed
- Use `@login_required` decorator or `LoginRequiredMixin` for protecting views
- Implement proper permission checks with `@permission_required` or `PermissionRequiredMixin`
- Use Django's password validation framework
- Never implement custom authentication from scratch

### Security Best Practices
- Use Django's CSRF protection middleware (enabled by default)
- Use `django.contrib.auth.authenticate()` for login
- Use `django.contrib.auth.login()` to establish sessions
- Never store secrets in code; use environment variables via `os.environ.get()`
- Use Django's built-in password hashing for user passwords
- Enable `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE` in production
- Use Django ORM to prevent SQL injection; never use raw SQL without parameterization
- Always validate and sanitize user input
- Use Django forms for all user input validation

### Database & Models
- Define all models in `models.py` or create a `models/` directory for larger projects
- Use `on_delete=models.CASCADE`, `PROTECT`, or `SET_NULL` intentionally
- Add `verbose_name` and `help_text` to fields for admin interface
- Use model methods for business logic
- Create migrations for all schema changes: `python manage.py makemigrations && python manage.py migrate`
- Use `Meta` class for model options (ordering, verbose_names, permissions)
- Use appropriate field types and validators
- Add indexes on frequently queried fields

### Views & Logic
- Use class-based views (CBVs) for complex views: `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`
- Use function-based views only for simple logic
- Keep business logic in model methods or service classes, not views
- Use services/utilities modules for complex operations
- Implement proper permission checks in all views
- Return appropriate HTTP status codes
- Use Django's mixins for code reuse

### URLs & Routing
- Namespace URLs by app: `path('blog/', include('blog.urls', namespace='blog'))`
- Use `reverse()` and `reverse_lazy()` instead of hardcoding URLs
- Name all URL patterns for template/view reversals
- Use slug fields for user-friendly URLs
- Import views using `from . import views` to avoid circular imports

### Forms & Validation
- Use Django forms (`ModelForm`, `Form`) for all user input
- Validate data in form `clean()` methods when needed
- Never skip form validation for security
- Use form widgets appropriately
- Add proper error handling and user feedback

### Templates
- Use template inheritance with `{% extends %}` and `{% block %}`
- Store templates in `app_name/templates/app_name/` directory structure
- Use Django template tags and filters
- Never use raw HTML for dynamic content; use template escaping
- Use `{% url 'url-name' %}` for URL references instead of hardcoding
- Use `{% static %}` template tag for static files
- Keep template logic minimal; use views/context for complex logic

### Settings Management
- Keep imports at the top of `settings.py`
- Use `os.environ.get()` for all environment-specific settings
- Split settings by environment (development, staging, production) when appropriate
- Use `BASE_DIR = Path(__file__).resolve().parent.parent` for relative paths
- Configure all installed apps in `INSTALLED_APPS`
- Set `TEMPLATES` with proper loaders and context processors
- Configure static files and media properly

### Testing
- Create tests in `tests.py` or `tests/` directory per app
- Use Django's `TestCase` class
- Test models, views, forms, and utilities
- Use fixtures and factories for test data
- Aim for good test coverage
- Use `setUp()` and `tearDown()` methods appropriately

### Administration
- Register models in `admin.py` with `ModelAdmin` classes
- Customize admin with `list_display`, `list_filter`, `search_fields`
- Use `readonly_fields` appropriately
- Add custom actions when needed
- Display meaningful `__str__()` methods in models

### Dependencies & Packages
- Keep `requirements.txt` updated
- Pin versions for stability: `Django==4.2.27`
- Use virtual environments
- Document all external dependencies

### Common Django Patterns
- Use `.values()` and `.values_list()` for specific fields in queries
- Use `.select_related()` for ForeignKey queries to reduce database hits
- Use `.prefetch_related()` for ManyToMany queries
- Use `.get()` with try/except or `.get_object_or_404()` for single object retrieval
- Use `.filter()` for conditional queries
- Use `.first()` and `.last()` for retrieving single objects from querysets
- Use `.exists()` to check if objects exist instead of `.count() > 0`

---

**Remember**: When uncertain about implementation, consult the official [Django Documentation](https://docs.djangoproject.com/) and follow their recommended patterns.

**Before committing any code, ask yourself:**
1. Does this follow Django conventions?
2. Is this using Django's built-in features properly?
3. Would a Django developer immediately understand this code?
4. Have I used the Django ORM instead of raw SQL?
5. Is this secure and following Django's security best practices?
