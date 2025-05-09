import os
from pathlib import Path
from dynaconf import Dynaconf, Validator

# Get the settings directory paths
SETTINGS_DIR = Path(__file__).parent / "settings"
GENERIC_DIR = SETTINGS_DIR / "generic"

# First load .env to get the environment
env_settings = Dynaconf(
    load_dotenv=True,
    envvar_prefix="JIRA"
)

# Get the current environment from .env or default to 'development'
current_env = os.getenv('ENV_FOR_DYNACONF', 'development').lower()

# Get all generic settings files
generic_files = [str(f) for f in GENERIC_DIR.glob("*.toml")]

# Get the environment-specific file
env_file = str(SETTINGS_DIR / f"{current_env}.toml")

# Combine all settings files
settings_files = generic_files + [env_file]

# Create the main settings object
settings = Dynaconf(
    envvar_prefix="JIRA",  # export envvars with `export JIRA_FOO=bar`
    settings_files=settings_files,  # Load generic and environment-specific files
    environments=True,  # Enable multiple environments
    load_dotenv=True,  # Load .env file
    validators=[
        # Ensure required variables are set
        Validator('JIRA.URL', must_exist=True),
        Validator('JIRA.EMAIL', must_exist=True),
        Validator('JIRA.API_TOKEN', must_exist=True),
        
        # Validate debug and log_level
        Validator('DEBUG', is_type_of=bool),
        Validator('LOG_LEVEL', is_in=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']),
        
        # Validate logging settings
        Validator('LOGGING.FORMAT', must_exist=True),
        Validator('LOGGING.DATE_FORMAT', must_exist=True),
        Validator('LOGGING.FILE', must_exist=True),
        
        # Validate security settings
        Validator('SECURITY.TOKEN_EXPIRY', is_type_of=int),
        Validator('SECURITY.MAX_RETRIES', is_type_of=int),
        Validator('SECURITY.TIMEOUT', is_type_of=int),
        Validator('SECURITY.SSL_VERIFY', is_type_of=bool),
    ]
)

# Validate all settings
settings.validators.validate_all()

# Add a helper function to get current environment
def get_current_environment():
    """Get the current environment name."""
    return current_env 