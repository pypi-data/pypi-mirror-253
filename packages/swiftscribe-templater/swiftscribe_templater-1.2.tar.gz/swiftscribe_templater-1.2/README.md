# SwiftScribe Templater

SwiftScribe Templater is a Python package that provides functionality for tokenizing Word documents and replacing tokens.

## Installation

You can install SwiftScribe Templater using pip:

```bash
pip install swiftscribe-templater
```

## Usage

Import the library 

```
from swift_templater import tokenize_word_document, replace_tokens
```

Specify the template, define the variables and lastly define the output document path.

```
# Tokenize Word Document
doc_path = "template.docx"
doc_tokens = tokenize_word_document(doc_path)

# Replace Tokens
replacement_dict = {"{title}": "John Doe", 
                    "{date}": "2024-01-24"}

modified_doc = replace_tokens(doc_path, replacement_dict)

# Save the modified document
modified_doc.save("output.docx")

```
Remember to add the tokens inside your word template. For example:

```
{title}
{date}
```
Dependencies

- nltk
- python-docx

## License
This project is licensed under the MIT License.

## Acknowledgments
- [NLTK][google-link]
- [python-docx][py-docx-link]

[py-docx-link]: https://python-docx.readthedocs.io/en/latest/
[google-link]: https://www.nltk.org//

## Contributing
Contributions are welcome! Please feel free to open an issue or submit a pull request.

## Authors

Nathan Budhu

## Contact

For any questions or feedback, please contact nathanbudhu@gmail.com.



