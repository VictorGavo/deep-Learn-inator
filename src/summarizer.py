# summarizer.py: Utilizes AI models to summarize the extracted texts.
# IDEA | Have a conversation about the text to leverage your learning. Maybe the template involves prompting.
# - Use transformers to apply AI summarization models to the text
# - Return summarized text
from transformers import pipeline

# Initialize the summarization pipeline with a pre-trained model
summarizer = pipeline("summarization")

def summarize_text(text):
    # Use the transformers pipeline to summarize the text
    try:
        summarized_text = summarizer(text, max_length=130, min_length=30, do_sample=False)
        # Extract the summary text from the output structure
        return ' '.join([summary['summary_text'] for summary in summarized_text])
    except Exception as e:
        print(f"Error during summarization: {str(e)}")
        return None
