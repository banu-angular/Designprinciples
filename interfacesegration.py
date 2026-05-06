# Imagine you have a large DocumentProcessor interface with methods for reading, printing, and faxing documents. Now, you want to create a class that only needs to read documents, but implementing the whole interface forces it to also implement the print and fax methods, which it doesn't need. This violates the Interface Segregation Principle. You should refactor this large interface into smaller, more specialized ones so that classes can only implement what they need. Can you write the Python code for that?Sure! Below is an example of how to refactor a large `DocumentProcessor` interface into smaller, more specialized interfaces to adhere to the Interface Segregation Principle.
# Original large interface
class DocumentProcessor:   
    def read(self, document):
        pass
    def printer(self, document):
        pass
    def fax(self, document):
        pass
# Smaller interfaces    
class DocumentReader:   
    def read(self, document):
        pass
class DocumentPrinter:   
    def printer(self, document):
        pass
class DocumentFaxer:   
    def fax(self, document):
        pass
# Example usage:    
class SimpleDocumentReader(DocumentReader):   
    def read(self, document):
        print(f"Reading document: {document}")
# Example usage:    
if __name__ == "__main__":
    reader = SimpleDocumentReader()
    reader.read("MyDocument.txt")
# In this refactored design:
# - We have created three smaller interfaces: `DocumentReader`, `DocumentPrinter`, and `DocumentFaxer`, each with a single responsibility.
# - The `SimpleDocumentReader` class only implements the `DocumentReader` interface, which allows it to focus solely on reading documents without being forced to implement unnecessary methods for printing and faxing.    
