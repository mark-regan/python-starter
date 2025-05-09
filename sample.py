import os
from settings import settings, get_current_environment
from logger import setup_logger

def connect_to_jira():
    """Simulate connecting to Jira with configured settings."""
    logger = setup_logger(__name__)
    
    logger.info(f"Connecting to Jira at {settings.jira.url}")
    logger.debug(f"Using email: {settings.jira.email}")
    
    # Simulate connection with timeout
    logger.info(f"Connection timeout set to {settings.security.timeout} seconds")
    logger.info(f"SSL verification: {'enabled' if settings.security.ssl_verify else 'disabled'}")
    
    return {
        "url": settings.jira.url,
        "email": settings.jira.email,
        "timeout": settings.security.timeout,
        "ssl_verify": settings.security.ssl_verify
    }

def main():
    """Main function demonstrating configuration usage."""
    # Set up logging
    logger = setup_logger(__name__)
    
    # Log current environment
    current_env = get_current_environment()
    logger.info(f"Running in {current_env} environment")
    logger.info(f"Debug mode: {'enabled' if settings.debug else 'disabled'}")
    
    # Demonstrate Jira connection
    try:
        connection = connect_to_jira()
        logger.info("Successfully configured Jira connection")
        logger.debug(f"Connection details: {connection}")
        
        # Demonstrate retry logic
        for attempt in range(settings.security.max_retries):
            logger.info(f"Attempt {attempt + 1} of {settings.security.max_retries}")
            # Simulate some operation
            if attempt == settings.security.max_retries - 1:
                logger.info("Operation completed successfully")
            else:
                logger.warning("Operation failed, retrying...")
        
    except Exception as e:
        logger.error(f"Error connecting to Jira: {str(e)}")
        raise

if __name__ == "__main__":
    main() 