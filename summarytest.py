
import sys
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from language_tool_python import LanguageTool

tool = LanguageTool('en-US')

MODEL_PATH = "E:/TestCorrectModel/testcorrectmodel"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, device=-1)  # CPU

def download_youtube_subtitle(video_id, output_file='transcriptofvid.txt'):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcripts([video_id])[0]
        subtitle_text = " ".join([entry['text'] for entry in transcript_list])
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(subtitle_text)
        return subtitle_text
    except (TranscriptsDisabled, NoTranscriptFound) as e:
        print(f"No transcript available: {e}")
        return None
    except Exception as e:
        print(f"Error downloading transcript: {e}")
        return None

def chunk_text(text, chunk_size=50):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])

def summarize_text(text, max_length=150):
    try:
        summary = summarizer(text, max_length=max_length, min_length=50, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Error summarizing chunk: {e}")
        return ""

def post_process_summary(summary):
    try:
        return tool.correct(summary)
    except Exception as e:
        print(f"Error correcting summary: {e}")
        return summary

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python summarytest_id_only.py <YouTube Video ID>")
        sys.exit(1)

    video_id =  sys.argv[1]
    print(f"Using video ID: {video_id}")

    transcript = download_youtube_subtitle(video_id)
    if transcript is None:
        print("Transcript unavailable. Exiting without errors.")
        sys.exit(0)

    print("Transcript downloaded successfully.\n")

    chunked_summary = []
    for i, chunk in enumerate(chunk_text(transcript, chunk_size=50)):
        print(f"Processing chunk {i+1}...")
        chunked_summary.append(summarize_text(chunk))

    final_summary = " ".join(chunked_summary)
    corrected_summary = post_process_summary(final_summary)

    output_file = 'summary.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(corrected_summary)

    print("\nSummary completed! Saved to 'summary.txt'.")
    print("\nPreview:\n", corrected_summary[:500], "...")



