import json
import os

# Content class to define a content item
class Content:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def to_dict(self):
        return {
            'title': self.title,
            'body': self.body
        }

# CMSManager class to handle CMS operations
class CMSManager:
    def __init__(self):
        self.contents = []
        self.load_contents()

    def add_content(self, title, body):
        content = Content(title, body)
        self.contents.append(content)
        self.save_contents()

    def list_contents(self):
        if not self.contents:
            print("No content available.")
            return

        for idx, content in enumerate(self.contents, start=1):
            print(f"{idx}. {content.title}")
            print(f"   Body: {content.body[:50]}...")  # Show first 50 characters

    def edit_content(self, index, new_title, new_body):
        if 0 <= index < len(self.contents):
            self.contents[index].title = new_title
            self.contents[index].body = new_body
            self.save_contents()
            print("Content updated successfully.")
        else:
            print("Invalid content index.")

    def delete_content(self, index):
        if 0 <= index < len(self.contents):
            del self.contents[index]
            self.save_contents()
            print("Content deleted successfully.")
        else:
            print("Invalid content index.")

    def save_contents(self):
        with open("cms_data.json", "w") as f:
            contents_data = [content.to_dict() for content in self.contents]
            json.dump(contents_data, f, indent=4)

    def load_contents(self):
        if os.path.exists("cms_data.json"):
            with open("cms_data.json", "r") as f:
                contents_data = json.load(f)
                for content_dict in contents_data:
                    content = Content(content_dict['title'], content_dict['body'])
                    self.contents.append(content)

def main():
    cms_manager = CMSManager()

    while True:
        print("\nCMS Menu:")
        print("1. Add Content")
        print("2. View Contents")
        print("3. Edit Content")
        print("4. Delete Content")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter content title: ")
            body = input("Enter content body: ")
            cms_manager.add_content(title, body)
            print("Content added successfully.")

        elif choice == "2":
            cms_manager.list_contents()

        elif choice == "3":
            cms_manager.list_contents()
            index = int(input("Enter content number to edit: ")) - 1
            new_title = input("Enter new title: ")
            new_body = input("Enter new body: ")
            cms_manager.edit_content(index, new_title, new_body)

        elif choice == "4":
            cms_manager.list_contents()
            index = int(input("Enter content number to delete: ")) - 1
            cms_manager.delete_content(index)

        elif choice == "5":
            print("Exiting CMS.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
