# main.py: Orchestrates the workflow from input handling to storing outputs in Obsidian.
# - Load configuration settings from config.py
# - Determine the source type (YouTube, podcast, newsletter, book)
# - If source is audio/video:
#   - Call transcriber.py to transcribe audio to text
# - If source is text:
#   - Call text_extractor.py to extract text content
# - Pass the extracted or transcribed text to summarizer.py for summarization
# - Use markdown_formatter.py to format the summarized text into Markdown
# - Store the formatted Markdown in Obsidian using obsidian_manager.py
# - Optionally update the database with new tags and metadata via database.py
# - Handle any exceptions and log appropriate errors or messages

