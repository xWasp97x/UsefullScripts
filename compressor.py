import os
import sys
from PIL import Image
import PyPDF2


root = sys.argv[1].strip()


def compress_img(img):
    print(img)
    picture = Image.open(img)
    picture.save(img, optimize=True, quality=75)


def compress_pdf(pdf):
    print(pdf)
    writer = PyPDF2.PdfFileWriter()
    try:
        reader = PyPDF2.PdfFileReader(pdf)

        for i in range(reader.numPages):
            page = reader.getPage(i)
            page.compressContentStreams()
            writer.addPage(page)
    except PyPDF2.errors.PdfReadError:
        return

    with open(pdf, 'wb') as file:
        writer.write(file)


print(f'Root: "{root}"')


complete_paths = []
for root, _, files in os.walk(root):
    complete_paths.extend([os.path.join(root, file) for file in files])

# print(complete_paths)

pictures = [file for file in complete_paths if file.endswith('.jpg') or file.endswith('.png')]

print(f'{len(pictures)} pictures found')

[compress_img(picture) for picture in pictures]

print('Pictures compressed.')


pdfs = [file for file in complete_paths if file.endswith('.pdf')]
print(f'{len(pdfs)} pdfs found')

[compress_pdf(pdf) for pdf in pdfs]

print('pdfs compressed.')




