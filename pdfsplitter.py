from PyPDF2 import PdfFileWriter, PdfFileReader
import os

from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

import imgdetect


def split_pdf(input_filepath, output_filepath, month, year):

    original_output_filepath = output_filepath + "/"
    arr = input_filepath.split("/")
    lenarr = len(arr)

    individual_filename = arr[lenarr-1]

    # remove .pdf
    individual_filename = individual_filename[:-4] 

    pdf_outputfolder = output_filepath + "/pdfs"
    images_outputfolder = output_filepath + "/uncropped_images"
    if not os.path.exists(pdf_outputfolder):
        os.makedirs(pdf_outputfolder)
    if not os.path.exists(images_outputfolder):
        os.makedirs(images_outputfolder)


    inputpdf = PdfFileReader(open(input_filepath, "rb"))

    numpgs = inputpdf.numPages

    # Iterate over pages in PDF, call img detection function
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        output_filepath = pdf_outputfolder + "/"

        newpdf_filename = output_filepath + individual_filename + "_" + "%s.pdf" % i

        with open(output_filepath + individual_filename + "_" + "%s.pdf" % i, "wb") as outputStream:
            # Save individual PDF
            output.write(outputStream)
        
        jpgfilename = individual_filename + "_" + "%s" % i + "_"

        # Convert to jpeg
        convert_from_path(newpdf_filename, output_folder=images_outputfolder, fmt="png", output_file=jpgfilename)

        converted_filename = images_outputfolder + "/" + jpgfilename + "0001-1.png"
        print(converted_filename)

        # Crop image
        num_photos_found = imgdetect.doWork(converted_filename, original_output_filepath, month, year)
        print("Finished page " + str(i+1) + " - output " + str(num_photos_found) + " separate images")
    

