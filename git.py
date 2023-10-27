import subprocess
import os
import datetime

PROD_BRANCH = "prod"


# Function to perform Git commands
def git_operations(directory_path, prod = False):
    cwd = os.getcwd()
    try:
        subprocess.run(["git", "add", "history.md"])
        # Change directory to the Git repository
        os.chdir(directory_path)

        # 1. Git checkout to another branch
        if prod: subprocess.run(["git", "checkout", PROD_BRANCH])

        # 2. Add all files in the directory and remove non-existing files
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "clean", "-fdx"])

        # 3. Make commit with current timestamp
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_message = f"Auto commit at {current_time}"
        subprocess.run(["git", "commit", "-m", commit_message])

        # 4. Push the code
        subprocess.run(["git", "push"])
        
        # 5. Check back to main branch
        # subprocess.run(["git", "checkout", 'main'])

        print("Git commands executed successfully.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        os.chdir(cwd)