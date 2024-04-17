# config.py: Stores API keys, file paths, and configuration variables.
# Configuration settings for the Deep-Learn-inator application

# API Keys and endpoints
API_KEYS = {
    'youtube': 'YOUR_YOUTUBE_API_KEY_HERE',
    'speech_recognition': 'YOUR_SPEECH_RECOGNITION_API_KEY_HERE',
    'transformers': 'YOUR_TRANSFORMERS_API_KEY_HERE'
}

# File paths for storing data and logs
FILE_PATHS = {
    'downloads': './downloads/',  # Path to store downloaded files
    'transcripts': './transcripts/',  # Path to store audio transcripts
    'summaries': './summaries/',  # Path to store summaries
    'markdown': './obsidian/',  # Path to store Markdown files in Obsidian format
    'logs': './logs/'  # Path for logging information
}

# Database configuration
DATABASE_CONFIG = {
    'database_url': 'sqlite:///deep_learn_inator.db'  # SQLite database URL
    # For PostgreSQL use: 'postgresql://username:password@localhost/deep_learn_inator'
}

# Obsidian specific settings
OBSIDIAN_CONFIG = {
    'vault_path': './obsidian_vault/'  # Path to Obsidian vault
}
