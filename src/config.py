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
    'downloads': r'C:\Users\Victo\Downloads\deep-Learn-inator-Downloads',  # Path to store downloaded files
    'transcripts': r'C:\Users\Victo\Documents\Projects\deep-Learn-inator\transcripts',  # Path to store audio transcripts
    'summaries': r'C:\Users\Victo\Documents\Projects\deep-Learn-inator\summaries',  # Path to store summaries
    'markdown': r'C:\Users\Victo\Documents\Projects\deep-Learn-inator\markdown',  # Path to store Markdown files in Obsidian format
    'logs': r'C:\Users\Victo\Documents\Projects\deep-Learn-inator\logs'  # Path for logging information
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
