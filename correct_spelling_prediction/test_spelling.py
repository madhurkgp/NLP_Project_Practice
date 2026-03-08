#!/usr/bin/env python3
"""
Simple test script for the spelling corrector
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from spelling_corrector import SpellingCorrector

def test_spelling_corrector():
    """Test the spelling corrector functionality."""
    print("=== Testing Spelling Corrector ===")
    
    # Initialize the corrector with demo vocabulary (faster)
    corrector = SpellingCorrector()
    
    # Test words
    test_words = ["propose", "hello", "pythn", "wrold", "programing"]
    
    print("\nTesting spelling corrections:")
    print("-" * 50)
    
    for word in test_words:
        suggestions = corrector.get_corrections(word, n=3)
        print(f"\nWord: '{word}'")
        if suggestions:
            for i, (suggested_word, prob) in enumerate(suggestions, 1):
                print(f"  {i}. {suggested_word} (prob: {prob:.6f})")
        else:
            print("  No suggestions found")
    
    print("\n=== Test completed successfully! ===")

if __name__ == "__main__":
    test_spelling_corrector()
