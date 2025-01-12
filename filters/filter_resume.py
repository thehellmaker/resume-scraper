from pypdf import PdfReader
import os
import shutil

folder_path = "resumes"
shortlist_path = os.path.join(folder_path, "shortlisted")
os.makedirs(shortlist_path, exist_ok=True)

files = os.listdir(folder_path)


def is_contains_text(text, keywords):
    for keyword in keywords:
        if keyword.lower() in text.lower():
            return True
    return False

i = 0
for file in files:
    file = f"resumes/{file}"
    try:
        reader = PdfReader(file)
        text = reader.pages[0].extract_text()
        if is_contains_text(text, ["flutter", "react native", "reactnative"]):
            print(file, i)
            destination = os.path.join(shortlist_path, os.path.basename(file))
            shutil.move(file, destination)
            print(f"Moved {file} to shortlisted folder")
            i = i + 1
    except Exception as e:
        print(f"Error processing {file}: {str(e)}")
        try:
            os.remove(file)
            print(f"Deleted {file}")
        except Exception as delete_error:
            print(f"Failed to delete {file}: {str(delete_error)}")
