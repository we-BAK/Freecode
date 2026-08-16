import argparse
from collections import Counter
import os

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.words = text.lower().split()
        self.lines = text.split('\n')
    
    def count_characters(self, include_spaces=False):
        """Count total characters in text"""
        if include_spaces:
            return len(self.text)
        return len(self.text.replace(' ', ''))
    
    def count_words(self):
        """Count total words"""
        return len(self.words)
    
    def count_lines(self):
        """Count total lines"""
        return len([line for line in self.lines if line.strip()])
    
    def count_sentences(self):
        """Count sentences (ending with . ! ?)"""
        return sum(1 for char in self.text if char in '.!?')
    
    def most_common_words(self, n=10):
        """Get n most common words"""
        return Counter(self.words).most_common(n)
    
    def average_word_length(self):
        """Calculate average word length"""
        if not self.words:
            return 0
        return sum(len(word) for word in self.words) / len(self.words)
    
    def get_summary(self):
        """Return complete analysis summary"""
        return {
            'characters': self.count_characters(),
            'characters_with_spaces': self.count_characters(include_spaces=True),
            'words': self.count_words(),
            'lines': self.count_lines(),
            'sentences': self.count_sentences(),
            'avg_word_length': round(self.average_word_length(), 2),
            'most_common_words': self.most_common_words(5)
        }

def main():
    parser = argparse.ArgumentParser(description='Command-line Text Analyzer')
    parser.add_argument('input', nargs='?', help='Text to analyze (use quotes)')
    parser.add_argument('-f', '--file', help='Read text from file')
    parser.add_argument('-w', '--words', type=int, default=10, help='Number of common words to show')
    
    args = parser.parse_args()
    
    # Get text from file or command line
    if args.file:
        if not os.path.exists(args.file):
            print(f"Error: File '{args.file}' not found")
            return
        with open(args.file, 'r') as f:
            text = f.read()
    elif args.input:
        text = args.input
    else:
        print("Error: Please provide text or use -f/--file option")
        parser.print_help()
        return
    
    # Analyze text
    analyzer = TextAnalyzer(text)
    summary = analyzer.get_summary()
    
    # Display results
    print("\n" + "="*50)
    print("TEXT ANALYSIS REPORT")
    print("="*50)
    print(f"Characters (no spaces): {summary['characters']}")
    print(f"Characters (with spaces): {summary['characters_with_spaces']}")
    print(f"Words: {summary['words']}")
    print(f"Lines: {summary['lines']}")
    print(f"Sentences: {summary['sentences']}")
    print(f"Average word length: {summary['avg_word_length']}")
    print(f"\nTop {args.words} Most Common Words:")
    for word, count in analyzer.most_common_words(args.words):
        print(f"  {word}: {count}")
    print("="*50 + "\n")

if __name__ == '__main__':
    main()