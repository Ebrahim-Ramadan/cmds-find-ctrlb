Command History Search Tool
A Python script for searching through command history files in different shells (Bash, Zsh, and PowerShell). The script provides real-time search results as you type, with debouncing to minimize excessive searches.

Features
Search through Bash, Zsh, and PowerShell command history files.
Real-time search results with a debounce delay.
Supports dynamic input and updates search results accordingly.
Requirements
Python 3.x
Access to the command history files for Bash, Zsh, and PowerShell
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Ebrahim-Ramadan/cmds-find-ctrlb.git
cd command-history-search-tool
Install Python (if not already installed): Ensure you have Python 3.x installed. You can download it from the official Python website.

Usage
Run the Script:

bash
Copy code
python search_tool.py
Enter Search Term:

The script will prompt you to enter a search term. Type your search term and press Enter. The script will display results from the Bash, Zsh, and PowerShell command history files as you type.

How It Works
Command History Files:

Bash: ~/.bash_history
Zsh: ~/.zsh_history
PowerShell: C:\Users\<username>\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
Debouncing: The script uses a debounce mechanism to wait for a short period after the user stops typing before performing a search.

Multi-threading: The script uses Python's threading to handle user input and search operations concurrently.

Configuration
Debounce Time: You can adjust the debounce time in the search_loop function by modifying the debounce_time parameter (in seconds).
Troubleshooting
File Not Found: If a history file is not found, ensure that the file exists and that you have the necessary permissions to access it.

No Results: If no results are found, check that the command history files contain the commands you expect and that the search term is correct.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Feel free to submit issues or pull requests to improve the tool.

Contact
For any questions or suggestions, please contact ramadanebrahim@gmail.com

