# Profanity Filtering Mini Project

This mini project aims to create a simple profanity filtering system using Python. The program will take text input and check for any profane or offensive words, providing a filtered version of the text.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/profanity-filtering-mini-project.git
   ```

2. Change to the project directory:

   ```bash
   cd profanity-filtering-mini-project
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:

   ```bash
   python profanity_filter.py
   ```

2. Enter the text you want to check for profanity.

3. The program will analyze the text and provide a filtered version with any detected profane words replaced by asterisks.

## Customization

The profanity filtering system can be customized according to your specific requirements. Here are a few ways you can modify the program:

- **Profanity Word List**: Update the `profanity_words.txt` file with your own list of profane words. Ensure each word is on a separate line.

- **Filtering Replacement**: If you prefer to replace profane words with something other than asterisks, you can modify the `replace_word` variable in `profanity_filter.py` to your desired replacement string.

- **Thresholds**: You can adjust the sensitivity of the filtering system by modifying the `threshold` variable in `profanity_filter.py`. A lower threshold will result in stricter filtering.

- **Integration**: This project provides a basic implementation of a profanity filter. You can integrate it into your existing applications or projects by importing the `profanity_filter` module and using the `filter_text` function.

## Contributions

Contributions to this mini project are always welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This mini project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as per the terms of the license.

## Acknowledgments

This project was inspired by the need for a simple profanity filtering solution. Special thanks to the developers of the profanity-check library for their contributions to the profanity word list used in this project.
