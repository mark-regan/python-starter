# Jira Reporting

A tool for generating reports from Jira data.

## Description

This project provides functionality to extract and analyze data from Jira, generating useful reports and insights.

## Getting Started

### Environment Setup

The project uses Dynaconf for configuration management, supporting multiple environments (development, staging, production).

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configuration can be managed in multiple ways:

   a. Using TOML files in the `settings` directory:
   ```
   settings/
   ├── generic/           # Generic settings shared across all environments
   │   ├── default.toml   # Base configuration
   │   ├── logging.toml   # Logging configuration
   │   └── security.toml  # Security settings
   ├── development.toml   # Development-specific settings
   ├── staging.toml       # Staging-specific settings
   └── production.toml    # Production-specific settings
   ```

   Example generic configuration (`settings/generic/default.toml`):
   ```toml
   [default]
   debug = false
   log_level = "INFO"

   [default.jira]
   url = "https://your-domain.atlassian.net"
   email = "your-email@example.com"
   api_token = "your-api-token"
   ```

   Example environment-specific configuration (`settings/development.toml`):
   ```toml
   [development]
   debug = true
   log_level = "DEBUG"

   [development.jira]
   url = "https://dev-domain.atlassian.net"
   email = "dev@example.com"
   api_token = "dev-api-token"
   ```

   The system will load:
   - All files from `settings/generic/` (shared settings)
   - The environment-specific file (e.g., `development.toml`, `staging.toml`, or `production.toml`)

   b. Using environment variables:
   ```bash
   export JIRA_URL=https://your-domain.atlassian.net
   export JIRA_EMAIL=your-email@example.com
   export JIRA_API_TOKEN=your-api-token
   ```

   c. Using `.env` file:
   ```
   # Set the environment (development, staging, or production)
   ENV_FOR_DYNACONF=development

   # Jira configuration
   JIRA_URL=https://your-domain.atlassian.net
   JIRA_EMAIL=your-email@example.com
   JIRA_API_TOKEN=your-api-token
   ```

3. Set the environment:
   ```bash
   # For development
   export ENV_FOR_DYNACONF=development
   
   # For staging
   export ENV_FOR_DYNACONF=staging
   
   # For production
   export ENV_FOR_DYNACONF=production
   ```

4. Using the configuration in your code:
   ```python
   from settings import settings, get_current_environment
   
   # Access configuration
   jira_url = settings.jira.url
   debug_mode = settings.debug
   log_level = settings.log_level
   
   # Access generic settings
   log_format = settings.logging.format
   security_timeout = settings.security.timeout
   
   # Get current environment
   current_env = get_current_environment()
   print(f"Running in {current_env} environment")
   ```

## Development

More details coming soon...
