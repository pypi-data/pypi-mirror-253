from swift_templater import tokenize_word_document, replace_tokens

# Tokenize Word Document
doc_path = "swiftscribe-templater/template.docx"
doc_tokens = tokenize_word_document(doc_path)

# Replace Tokens
replacement_dict = {"{title}": "John Doe", 
                    "{date}": "2024-01-24"}

modified_doc = replace_tokens(doc_path, replacement_dict)

# Save the modified document
modified_doc.save("modified_document1.docx")
