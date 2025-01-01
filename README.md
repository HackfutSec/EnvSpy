# **EnvSpy**  
**Uncover and extract hidden `.env` files with ease – your ultimate tool for configuration discovery!**

[![GitHub](https://img.shields.io/github/license/HackfutSec/EnvSpy)](https://github.com/HackfutSec/EnvSpy)  
[![GitHub issues](https://img.shields.io/github/issues/HackfutSec/EnvSpy)](https://github.com/HackfutSec/EnvSpy/issues)  
[![GitHub forks](https://img.shields.io/github/forks/HackfutSec/EnvSpy)](https://github.com/HackfutSec/EnvSpy/network)

## **Overview**

**EnvSpy** is a powerful tool designed to uncover and retrieve `.env` files from URLs or from a list of URLs provided in a file. It allows security researchers and developers to quickly extract environment variable files from web resources, automate the process of retrieving sensitive information (if legally permitted), and offers integration with Telegram for easy alerts.

---

## **Features**

- **Retrieve `.env` Files**: Extract `.env` files from any accessible URL.
- **Bulk URL Processing**: Process a list of URLs from a file, one after another.
- **Save Results**: Save retrieved `.env` file contents to a local file for future reference.
- **Telegram Integration**: Automatically send the results to your Telegram bot for real-time monitoring and alerts.
- **Customizable Timeout**: Adjust the timeout for HTTP requests to suit your network conditions.
- **Clear, User-Friendly Interface**: Dynamic and clean terminal output with beautiful banners.

---

## **Installation**

### **Prerequisites**
- Python 3.x
- The following Python packages:
  - `requests`
  - `beautifulsoup4`
  - `colorama`

### **Step 1: Clone the Repository**
Clone the repository to your local machine:

```bash
git clone https://github.com/HackfutSec/EnvSpy.git
cd EnvSpy
```

### **Step 2: Install Dependencies**
Install the required Python dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### **Step 3: Run the Tool**
Once the installation is complete, you can start using **EnvSpy** by running:

```bash
python envspy.py
```

---

## **Usage**

When you run the tool, you’ll be presented with a menu of options:

1. **Test a single URL**: Enter a URL to retrieve the `.env` file content.
2. **Test multiple URLs**: Provide a file containing a list of URLs to process.
3. **Exit**: Exit the program.

If you choose to send the results to your Telegram bot, you will be prompted for:
- **Telegram Bot Token**: Create a bot via [BotFather](https://core.telegram.org/bots#botfather) on Telegram and get your token.
- **Chat ID**: Get the chat ID to send messages using your bot. You can use this [Telegram API tool](https://api.telegram.org/bot<YourBotToken>/getUpdates) to find your chat ID.

### **Example Menu Flow:**

```bash
[1] Test a single link.
[2] Test a file containing multiple links.
[3] Exit the program.
Choose an option (1/2/3):
```

---

## **Command-Line Arguments**

You can also use the following command-line arguments for customization:

- `--lines-per-page`: Number of lines to display per page.
- `--timeout`: HTTP request timeout duration (default is 5 seconds).

### **Example:**

```bash
python envspy.py --lines-per-page 50 --timeout 10
```

---

## **Example Output**

When testing a URL, you will see output similar to this:

```bash
[✓] Content found at the following URL: http://example.com/.env
HTML page content (only visible text):
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASS=password

Results saved to env.txt
```

For bulk URL testing, the program will display:

```bash
[!] Processing URL: http://example.com/.env
[✓] Content found at the following URL: http://example.com/.env
HTML page content (only visible text):
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASS=password

Results saved to env.txt
```

---

## **Telegram Integration**

If you opt to send the results to your Telegram bot, the tool will automatically send the contents of the `.env` file to the chat you specify.

Example:

```bash
[✓] Message sent to Telegram.
```

---

## **Contributing**

We welcome contributions to **EnvSpy**! If you have ideas for new features, bug fixes, or improvements, please fork the repository and create a pull request.

### Steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to your branch (`git push origin feature-name`).
6. Open a pull request.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**

- Thanks to [HackfutSec](https://github.com/HackfutSec) for making **EnvSpy** available to the community.
- Libraries used in this project:
  - [requests](https://docs.python-requests.org/en/master/)
  - [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)
  - [colorama](https://pypi.org/project/colorama/)

---

## **Disclaimer**

**EnvSpy** is a tool designed for educational and ethical use. **The creator is not responsible for the misuse of this tool**. Always ensure that you have permission to access the URLs and data you are working with.

--- 

Feel free to adjust the details like your GitHub username or any additional features you might add. This README will help users easily understand the tool's purpose, how to install and use it, and how to contribute.
