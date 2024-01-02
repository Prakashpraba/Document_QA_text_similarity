# Document_QA_text_similarity
This Python program is a GUI-based document QA tool that extracts text from PDFs using PyMuPDF, processes it with NLTK, and utilizes Sentence Transformers for sentence similarity. It enables users to upload a PDF, parses the text, and generates responses to questions about the document through a Tkinter-based interface.
----
# PyMuPDF
This app uses PyMuPDF to extract text from the user uploaded PDF documents.PyMuPDF is a powerful Python library for working with PDF files, providing versatile functionalities for reading, manipulating, and extracting content from PDF documents. With a focus on efficiency and speed, PyMuPDF, also known as Fitz, is built on top of the MuPDF library. It offers a comprehensive set of features, allowing users to access and navigate through PDF pages, extract text and images, and perform various document-related tasks.

One of the notable features of PyMuPDF is its ability to render high-quality images from PDF pages, making it suitable for tasks such as image extraction and conversion. Additionally, PyMuPDF supports advanced text extraction capabilities, enabling users to obtain precise and structured text content from PDF files.

Designed to be lightweight and efficient, PyMuPDF is an excellent choice for developers working on projects that involve PDF manipulation, document analysis, or data extraction from PDF documents. Its Pythonic interface, combined with MuPDF's speed, makes PyMuPDF a valuable tool for a wide range of applications, from document processing to data mining and content extraction.
-----
# NLTK
This app uses NLTK to tokenize the text that is extracted from the PDF document.NLTK (Natural Language Toolkit) is a comprehensive Python library for natural language processing (NLP) tasks. It provides tools and resources for working with human language data, including tokenization, stemming, and part-of-speech tagging. NLTK also offers access to numerous corpora and lexical resources, aiding in language analysis and research. With a user-friendly interface, NLTK supports various NLP techniques, making it a popular choice for both beginners and researchers in the field. Its modular design and extensive documentation contribute to its versatility in developing applications for tasks such as text classification, sentiment analysis, and language modeling.
-----
# Tkinter
This app uses tkinter for the GUI applications for user interaction.Tkinter is a standard GUI (Graphical User Interface) toolkit for Python, providing a set of tools for creating desktop applications. It comes bundled with most Python installations and allows developers to build interactive and user-friendly interfaces. Tkinter is based on the Tk GUI toolkit and features a wide range of GUI components such as buttons, labels, and entry widgets. It supports event-driven programming, enabling the creation of responsive applications with user-triggered actions. Tkinter's simplicity, ease of use, and cross-platform compatibility make it a popular choice for developing desktop applications in Python.
-----
# Sentence Transformers
This app uses S-BERT Sentence transformers to Embed the sentences and find the cosine similarity between the sentences.Sentence-BERT (S-BERT) is a variation of BERT (Bidirectional Encoder Representations from Transformers) designed for sentence-level embeddings. It transforms sentences into fixed-size vectors, capturing semantic similarities between sentences. By leveraging a Siamese network architecture, S-BERT enhances sentence representations for tasks like paraphrase identification and information retrieval. Utilizing pre-trained models from the Sentence Transformers library, S-BERT allows for efficient transfer learning and facilitates downstream applications like question answering and document retrieval. Its ability to generate contextually rich sentence embeddings makes S-BERT a valuable tool for natural language understanding and similarity-based tasks.
--------
# The sample for the DocumentQA APP:
-------
## Sample 1:
![sample](https://github.com/Prakashpraba/Document_QA_text_similarity/assets/100506541/00bcfa7e-7c69-4c24-b498-ddad150958c3)
------
## Sample 2:
![sample2](https://github.com/Prakashpraba/Document_QA_text_similarity/assets/100506541/503192f4-e5d3-4d10-88cd-a914792b8559)
-------
