import os

def search_history(file_path, search_term):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            results = [line for line in lines if search_term.lower() in line.lower()]
            return results
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

def search_powershell_history(search_term):
    powershell_history_path = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt')
    return search_history(powershell_history_path, search_term)

def main():
    # Define the paths to the history files
    bash_history_path = os.path.expanduser('~/.bash_history')
    zsh_history_path = os.path.expanduser('~/.zsh_history')
    
    search_term = input("Enter the search term: ")
    
    # Search in Bash history
    # print(f"\nSearching Bash history for '{search_term}':")
    bash_results = search_history(bash_history_path, search_term)
    if bash_results:
        for line in bash_results:
            print(line.strip())
    else:
        pass
        # print("No results found in Bash history.")

    # Search in Zsh history
    # print(f"\nSearching Zsh history for '{search_term}':")
    zsh_results = search_history(zsh_history_path, search_term)
    if zsh_results:
        for line in zsh_results:
            print(line.strip())
    else:
        pass
        # print("No results found in Zsh history.")
    
    # Search in PowerShell history
    # print(f"\nSearching PowerShell history for '{search_term}':")
    powershell_results = search_powershell_history(search_term)
    if powershell_results:
        for line in powershell_results:
            print(line.strip())
    else:
        pass
        # print("No results found in PowerShell history.")

if __name__ == "__main__":
    main()
