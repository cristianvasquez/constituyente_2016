import textract

file_name = './informe-final-cco-16-de-enero-de-2017.pdf'
output = file_name+'.md'

test = textract.process(file_name, method='tesseract', language='spa')
text_file = open(output, "wb")
text_file.write(test)
text_file.close()
