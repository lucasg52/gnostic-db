import json
from keybert import KeyBERT
from collections import defaultdict
import os
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Initialize model
kw_model = KeyBERT(model="all-MiniLM-L6-v2")

def filter_stop_words(keywords_list):
    """Remove keywords that are only stop words or contain only stop words."""
    filtered = []
    for kw, score in keywords_list:
        # Split keyword into words (handles both single words and phrases)
        words = kw.lower().split()
        # Keep keyword if it has at least one non-stop word
        if any(word not in ENGLISH_STOP_WORDS for word in words):
            filtered.append((kw, score))
    return filtered

def extract_keywords_to_json(title, paragraph, output_file="keywords.json"):
    """
    Extracts keywords from title and paragraph.
    
    Args:
        title: The title text
        paragraph: The paragraph text
        output_file: Output JSON file path
    """
    # Calculate number of keywords based on paragraph length
    num_words = len(paragraph.split())
    n_keywords = min(100, max(10, int(num_words / 20)))
    
    print(f"Title: {title}")
    print(f"Document length: {num_words} words")
    
    # Extract keywords from title separately
    title_keywords = kw_model.extract_keywords(
        title,
        keyphrase_ngram_range=(1, 2),
        stop_words='english',
        top_n=min(10, n_keywords),
        use_mmr=True,
        diversity=0.7
    )
    
    # Post-filter title keywords to remove any stop words that slipped through
    title_keywords = filter_stop_words(title_keywords)
    
    # Extract keywords from paragraph separately
    paragraph_keywords = kw_model.extract_keywords(
        paragraph,
        keyphrase_ngram_range=(1, 2),
        stop_words='english',
        top_n=n_keywords,
        use_mmr=True,
        diversity=0.7
    )
    
    # Merge keywords
    # Use a dictionary to track the best score for each keyword
    keyword_scores = defaultdict(float)
    
    # Add title keywords
    for kw, score in title_keywords:
        keyword_scores[kw] = max(keyword_scores[kw], score)
    
    # Add paragraph keywords
    for kw, score in paragraph_keywords:
        keyword_scores[kw] = max(keyword_scores[kw], score)
    
    # Sort by score (descending) and take top n_keywords
    sorted_keywords = sorted(keyword_scores.items(), key=lambda x: x[1], reverse=True)
    keywords_with_scores = sorted_keywords[:n_keywords]
    
    # Extract only the keyword strings for JSON
    keywords = [kw for kw, score in keywords_with_scores]
    
    print(f"Extracted {len(keywords)} keywords (merged from title and paragraph)")

    # Save JSON file with only keywords
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(keywords, f, ensure_ascii=False, indent=4)

    print(f"Keywords saved to {output_file}")
    return keywords

