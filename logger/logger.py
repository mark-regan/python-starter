import logging
import logging.handlers
from pathlib import Path
from settings import settings

def setup_logger(name: str = None) -> logging.Logger:
    """
    Set up and configure logging based on application settings.
    
    Args:
        name: Optional name for the logger. If not provided, returns the root logger.
    
    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    log_dir = Path(settings.logging.file).parent
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Configure root logger
    logging.basicConfig(
        level=settings.log_level,
        format=settings.logging.format,
        datefmt=settings.logging.date_format
    )
    
    # Add file handler with rotation
    file_handler = logging.handlers.RotatingFileHandler(
        settings.logging.file,
        maxBytes=int(settings.logging.max_size.replace('MB', '')) * 1024 * 1024,
        backupCount=settings.logging.backup_count
    )
    file_handler.setFormatter(logging.Formatter(settings.logging.format))
    
    # Get the logger
    logger = logging.getLogger(name)
    logger.addHandler(file_handler)
    
    return logger 