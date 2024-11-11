# ANTLR4-HELLO
This project demonstrates how to use ANTLR4 to parse a simple language that recognizes the phrase "Hello &lt;any_string>". The project includes the grammar definition, Python code to generate the lexer and parser, and the script to parse input strings.

Prerequisites
1. ANTLR4: The parser generator tool for creating lexers and parsers.
   sudo apt install antlr4
2. Java: ANTLR is written in Java, so you'll need Java installed on your system. You can install OpenJDK using the following command:
   sudo apt install openjdk-11-jdk
3. Python3: Python 3 is required for running the generated code.
    pip install antlr4-python3-runtime
Project Files
Hello.g4
This is the grammar file for the "Hello" language. It defines the structure of the input, where the phrase starts with the word hello followed by an identifier (a string of lowercase letters)

Generating Lexer and Parser
 java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 Hello.g4
This will generate the following files:
HelloLexer.py: Lexer for tokenizing the input.
HelloParser.py: Parser for recognizing the syntax of the input.
HelloListener.py: Listener for handling the parsing events.

hello_parser.py
This is the main Python file that uses the generated lexer and parser to process input strings. It reads an input string, tokenizes it, and parses it using the ANTLR-generated code.

Running the program
python3 hello_parser.py
Enter a string: hello world
Output:
(r hello world)

