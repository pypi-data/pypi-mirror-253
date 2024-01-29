import os
import sys
import time
from dotenv import load_dotenv
from openai import OpenAI

# Load env variables first.
load_dotenv()
api_key = os.getenv('GPT_KEY')

# Then initiate the OpenAI client with the api_key.
client = OpenAI(api_key=api_key)

file_diagram_prompt = """You are an intelligent code analyzer. 
Use the following step-by-step instructions to respond to user inputs. If you do not know for sure the relations between files, use your best guess.
1. given an input such as 'filename1' code_for_filename_1, 'filename2' code_for_filename_2 etc... Parse through all the code and 
find all which functions in each file depend on functions in other files.
2. Create an ASCII file diagram for the files to list the functions that interact with other files. The ASCII diagram should be 
formatted as such: each relevant file is in a box with its name on top, and the functions that interact with other files at the bottom.
3. Connect the functions to the files they interact with ASCII arrows. 

Reminder. If a file does not have any functions or imports that interact with it, do not include it.
Only count imports that import a file in the current folder you are looking at.

Here is an example. For this input:
"File 1:
import module2
import module3

def function1():
    module2.function2()
    module3.function3()

File 2:
def function2():
    pass

File 3:
import module2
def function3():
    module1.function1()"
This is how the output should look:
+---------------------+                 +---------------------+
|      File 1         |                 |      File 3         |
+---------------------+ ------------->  +---------------------+
| - File2.function2   |                 | - File3.function3   |
+---------------------+                 +---------------------+
        |
        |
        |
        v                  
+---------------------+
|      File 2         |
+---------------------+
| - File1.function1   |
+---------------------+
                 
On the bottom of the diagram include a short summary on what the files and components are doing as well as the purpose of the system as a whole if possible.
Only include the diagram and the summary in the ouput."""

system_diagram_prompt = """You are an intelligent code analyzer that will analyze code and group it into categories of a web system. Use the following step-by-step instructions to respond to user inputs.

Given input files such as 'filename1' code_for_filename_1, 'filename2' code_for_filename_2, etc., parse through all the code.

Infer the main components of the system based on the code analysis, considering functions, dependencies, and patterns in the code.

Identify the interactions between every inferred component in the system.

Group the files into the inferred components of the system.

Create an ASCII architecture diagram for the main components of the system. The ASCII diagram should be formatted as such: each relevant file is in a box belonging to an inferred component of a web system, with the component's name on top. 
Infer from the code and file name what the component is. 

Connect the boxes containing inferred components of the system to other boxes in a way that makes sense in a proper web system. 

Name each component with a proper name.
Instead of Component A, B, C, etc. use the inferred component names such as 
frontend, backend, other etc. Make sure all relevant files are included in the diagram.
Some tips you can use: 
HTML, CSS, JavaScript, React, Angular, Vue.js files are usually front end.
Node.js, Java, Python, files are usually backend. SQL and NoSQL files are usually database. and if a file calls AWS or another server, it is Server.
These frontend, backend, database, server, etc. are the main components of a web system.

Example Input:
"File1:
import module2
import module3

def function1():
    module2.function2()
    module3.function3()

File2:
def function2():
    pass

File3:
import module2
def function3():
    module1.function1()"

Output Example:
+---------------------+                 +---------------------+
|      Component A    |                 |      Component B    |
+---------------------+ ---------------> +---------------------+
| - File1             |                 | - File3             |
| - File2             |                 +---------------------+
+---------------------+
         |                              
         |                              
         v                              
+---------------------+
|      Component C    |
+---------------------+
| - File3             |
+---------------------+
                                       
On the bottom of the diagram include a short summary on what the files and components are doing as well as the purpose of the system as a whole if possible.
Only include the diagram and the summary in the ouput."""

system_component_prompt = """You are an intelligent code analyzer that can analyze code and group it into categories of a web system.
Use the following instructions to respond to user inputs. Based on the previous code analyzed, diagram generated, and responses you will...
Answer questions on specific system components. By telling the user know how the component works with other files and components as well as what the specific component does in the scope of all files."""

file_component_prompt = """You are an intelligent code analyzer that can analyze files and see how said files interact with each other.
Use the following instructions to respond to user inputs. Based on the previous code analyzed, diagram generated, and responses you will...
Answer questions on specific files by telling the user how the file interacts with other files as what the specific file does in the scope of all files."""


system_component_prompt = """You are an intelligent code analyzer that can analyze code and group it into categories of a web system.
Use the following instructions to respond to user inputs. Based on the previous code analyzed, diagram generated, and responses you will...
Answer questions on specific system components. By telling the user know how the component works with other files and components as well as what the specific component does in the scope of all files."""

file_component_prompt = """You are an intelligent code analyzer that can analyze files and see how said files interact with each other.
Use the following instructions to respond to user inputs. Based on the previous code analyzed, diagram generated, and responses you will...
Answer questions on specific files. By telling the user how the file interacts with other files and components as well as what the specific file does in the scope of all files."""


def prompt_gpt(file_data, diagram_type):

    messages = [{"role": "system", "content": system_diagram_prompt if diagram_type ==
                 "system" else file_diagram_prompt}]

    message = ""
    for f in file_data:
        message += f"{f[0]}:\n{f[1]}\n\n"

    messages.append({"role": "user", "content": message})
    cur_model = "gpt-4-0613"
    # cur_model = "gpt-3.5-turbo"
    chat = client.chat.completions.create(model=cur_model,
                                          messages=messages,
                                          temperature=0.1,
                                          n=1,
                                          stream=True,
                                          max_tokens=500)

    for chunk in chat:
        content = chunk.choices[0].delta.content
        if content is not None:
            if content.endswith("None"):
                print(content[:-4], end="")
            else:
                print(content, end="")
    print("\n")
    
    while True:
        inquiry = input("What would you like to learn more about?\n")
        if inquiry.lower() == "exit":
            break
        inquiry_messages = [{"role": "system", "content": system_component_prompt if diagram_type ==
                 "system" else file_component_prompt}]
        inquiry_messages.append({"role": "user", "content": inquiry})
        inquiry_chat = client.chat.completions.create(model=cur_model,
                                          messages=inquiry_messages,
                                          temperature=0.1,
                                          n=1,
                                          stream=True,
                                          max_tokens=500)
        print("\n")
        for chunk in inquiry_chat:
            content = chunk.choices[0].delta.content
            if content is not None:
                if content.endswith("None"):
                    print(content[:-4], end="")
                else:
                    print(content, end="")
        print("\n")
        

    return chat
