<p align="center">

<a href="https://github.com/Spark4bhi/Aries">
   <img src="https://img.shields.io/github/forks/Spark4bhi/aries?logo=githubactions&logoColor=success&style=social" alt="github-fork">
</a>

<a href="https://github.com/Spark4bhi/aries">
   <img src="https://img.shields.io/github/stars/Spark4bhi/aries?label=Stars&logo=ReverbNation&&logoColor=yellow&style=social" alt="github-repo-stars">
</a>

# Aries (Beta)

Aries is a Python-based GUI digital assistant that can help you perform a variety of tasks, such as generating text, getting the weather, opening websites, searching the web, and managing a to-do list. Aries is designed to be easy to use and customize, and can be extended with additional functionality through Python modules.

Aries is an AI chatbot and is currently in beta. This means that the bot is still being developed and may have some bugs or limitations. However, Aries is designed to learn from user input and become better over time.

![Capture](https://user-images.githubusercontent.com/101919895/236738120-636ef663-9e0c-43ec-b04b-aa3523dcb72d.JPG)

## Features

- GUI based application using `pyQt`.
- Generate text based on a prompt using OpenAI's GPT-3 language model.
- Open a specified website in the default web browser.
- Search Google for a specified query and open the top result in the default web browser.
- Add, remove, and list items in a to-do list stored in a text file.
- Respond to voice commands using the SpeechRecognition library.
- Speak text using the pyttsx3 library.
- And More..!!

## Installation

1. To install Aries, you'll need to have Python 3.6 or later installed on your system. You can download Python from the official website.

2. Clone the Aries repository to your local machine:
```bash 
git clone https://github.com/spark4bhi/aries.git
```

3. Navigate to the Aries directory: cd aries.
Install the required Python packages: 
```bash
pip install -r requirements.txt
```
4. Create a .env file in the root directory of the project, and set the following environment variables:
```env
openaikey=<YOUR_API_KEY>
username=<YOUR_NAME>
botname=<YOUR_BOT_NAME>
```
    
## Usage

To start Aries, run the following command from the root directory of the project:

```bash
python index.py
```
You can then interact with Aries using the help command 
## Authors

- [@Spark4bhi](https://www.github.com/spark4bhi)


## License

© Spark4bhi, 2023. All rights reserved.

This project is protected under the MIT license. Unauthorized use and/or duplication of this material without express and written permission from the author and/or owner is strictly prohibited. Excerpts and links may be used, provided that full and clear credit is given to SPark4bhi with appropriate and specific direction to the original content.



## Feedback/Bugs

If you have any feedback or detect any, please fell free to reach out to me at spark4bhi@gmail.com


