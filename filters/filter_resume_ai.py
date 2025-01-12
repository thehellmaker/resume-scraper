from llm.openai_helper import client
from pypdf import PdfReader
import os
import shutil

folder_path = "resumes/shortlisted"
shortlist_path = os.path.join(folder_path, "shortlisted")
os.makedirs(shortlist_path, exist_ok=True)

files = os.listdir(folder_path)


def is_shortlisted(file, text):
    content = """
    You are given the contents of a resume under the <resume></resume> XML tag below.

    A candidate should be shortlist if majority of the following are true:
    1. They have good experience in flutter, react native or reactnative.
    2. They have good open source contributions. Do not consider just github links as most canidates copy paste their projects and dnt have experience.
    3. Consider valid experiences like Summery of Code and Summer of anything else.
    4. Should have done atleast 1 mobile development project or internship. 
    5. Do not consider candidates with no experience in mobile development.
    6. Ignore candidates who have boring resume with no achievements.
    
    Only consider candidates who have more than 1 internship experience.
    COnsider freelance development as a plus and always shortlist them.

    Return True if the candidate is shortlisted and False otherwise. Output only True or False and nothing else.

    """ + f"<resume>{text}</resume>"
    chat_completion = client.chat.completions.create(
        messages=[
        {
            "role": "user",
            "content": content,
        }
    ],
        model="gpt-4o-mini",
    )

    # Extract the name text
    name = chat_completion.choices[0].message.content  # Strip any extra spaces around the text
    # print(file, name)
    return name == "True"

files.sort()

for file in files:
    try:
        if file == "shortlisted":
            continue
        file = f"resumes/shortlisted/{file}"
        reader = PdfReader(file)
        text = reader.pages[0].extract_text()
        if is_shortlisted(file, text):
            # pass
            print(file)
            # destination = os.path.join(shortlist_path, os.path.basename(file))
            # shutil.move(file, destination)
            # print(f"Moved {file} to shortlisted folder")
    except Exception as e:
        # print(f"Error processing {file}: {str(e)}")
        pass
