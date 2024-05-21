import fitz
import os
import argparse


def search_in_pdf(file_path, search_words):
    """Search for the words in a given PDF file."""
    try:
        doc = fitz.open(file_path)
        for page in doc:
            text = page.get_text()
            for word in search_words:
                if word in text:
                    print(f"Found '{word}' in {file_path} on page {page.number + 1}")
        doc.close()
    except Exception as e:
        print(f"Could not read {file_path}. Error: {e}")


def search_pdfs_in_directory(directory_path, search_words):
    """Search all PDF files in the directory and subdirectories for the words."""
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                search_in_pdf(file_path, search_words)


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Search words in PDF files within a specified directory.')
    parser.add_argument('-d', '--directory', type=str, default=os.getcwd(),
                        help='The directory to search within (default is the current directory)')
    parser.add_argument('-w', '--words', type=str, required=True,
                        help='Comma-separated list of words to search')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    directory = args.directory
    words = args.words.split(',')
    search_pdfs_in_directory(directory, [word.strip() for word in words])
