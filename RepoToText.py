import os
from datetime import datetime
import re

class LocalRepoScraper:
    """Scrape files from a local directory."""

    def __init__(self, directory_path, selected_file_types=None, excluded_items=None):
        if selected_file_types is None:
            selected_file_types = []
        if excluded_items is None:
            excluded_items = {
                "file_names": {".env", ".env.local", ".env.production", ".gitignore"},
                "folder_names": {"dist", "node_modules", ".git"},
            }
        self.directory_path = directory_path
        self.selected_file_types = selected_file_types
        self.excluded_items = excluded_items

    def fetch_all_files(self):
        """Fetch all files recursively from the local directory, excluding specific items."""
        files_data = []

        for root, dirs, files in os.walk(self.directory_path):
            # Remove excluded folders from traversal
            dirs[:] = [d for d in dirs if d not in self.excluded_items["folder_names"]]

            for file_name in files:
                # Exclude specific file names
                if file_name in self.excluded_items["file_names"]:
                    continue
                # Include files only if they match selected file types
                if not self.selected_file_types or any(file_name.endswith(file_type) for file_type in self.selected_file_types):
                    file_path = os.path.join(root, file_name)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            file_content = f"\n'''--- {file_path} ---\n"
                            file_content += file.read()
                            file_content += "\n'''"
                            files_data.append(file_content)
                    except (UnicodeDecodeError, OSError) as e:
                        print(f"Warning: Skipping {file_path} due to an error: {e}")
        
        return files_data

    def write_to_file(self, files_data):
        """Create a .txt file with all the gathered data."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        output_filename = f"local_repo_content_{timestamp}.txt"
        with open(output_filename, "w", encoding='utf-8') as output_file:
            output_file.write(f"*Local Directory: \"{self.directory_path}\"*\n")
            for file_data in files_data:
                output_file.write(file_data)
        return output_filename

    def clean_up_text(self, filename):
        """Remove excessive line breaks."""
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        cleaned_text = re.sub(r'\n{3,}', '\n\n', text)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)

    def run(self):
        """Run the script."""
        print("Fetching all files...")
        files_data = self.fetch_all_files()

        print("Writing to output file...")
        filename = self.write_to_file(files_data)

        print("Cleaning up text...")
        self.clean_up_text(filename)

        print(f"Done. Output file created: {filename}")
        return filename


if __name__ == "__main__":
    # Input the local directory path
    directory_path = input("Enter the path to the local directory: ").strip()
    
    # Input file types to filter (optional)
    file_types_input = input("Enter the file types to include (comma-separated, e.g., .py,.txt), or press Enter to include all files: ").strip()
    selected_file_types = [file_type.strip() for file_type in file_types_input.split(',') if file_type.strip()]

    # Default exclusions
    excluded_items = {
        "file_names": {".env", "package-lock.json", "data_observability.log", "white_car_processed.jpg", ".env.local", ".env.production", ".gitignore", "package.json", "README.md", "yarn.lock", "tsconfig.json", "vercel.json", "eslint.config.js", "toyota_filtered_data.xlsx", "tsconfig.app.json", "eslint.config.js", "vite.config.ts", "tsconfig.node.json"},
        "folder_names": {"dist", "node_modules", ".git", "public", "assets", "data", "models", "__pycache__", "visualizations", ""},
    }

    scraper = LocalRepoScraper(directory_path, selected_file_types, excluded_items)
    scraper.run()
