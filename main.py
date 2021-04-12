import os
from pdf2image import convert_from_path
from os import listdir, path, remove, rename, stat

# May be needed when implementing on web-adapters
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import img2pdf
import tempfile
import sys
from PIL import Image
from PIL import ImageEnhance

# turns pdf into mult jpgs (much smaller size)
def convert_pdf_to_tiff():
    pdf_path = './pdf_images/1.pdf'
    dirname = './jpg_images'
    convert_from_path(pdf_path, output_folder=dirname, fmt='tiff', size=800, dpi=300, grayscale=True, jpegopt={
    "quality": 25,
    "progressive": True,
    "optimize": True
})

    # convert all files ending in .tif inside a directory
    with open("name.pdf", "wb") as f:
        imgs = []
        for fname in os.listdir(dirname):
            if not fname.endswith(".tif"):
                continue
            path = os.path.join(dirname, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        f.write(img2pdf.convert(imgs))













# THIS ONE TURNS TO SINGLE PDF THAT IS SMALLER - MISSION SUCCESS!
# def convert_pdf_to_tiff():
#     pdf_path = './pdf_images/1.pdf'
#     dirname = './jpg_images'
#     convert_from_path(pdf_path, output_folder=dirname, fmt='tiff', size=800, dpi=300, grayscale=True,
#                       jpegopt={
#             "quality": 25,
#             "progressive": True,
#             "optimize": True
#         })
#
#     # convert all files ending in .tif inside a directory
#     with open("name.pdf", "wb") as f:
#         imgs = []
#         for fname in os.listdir(dirname):
#             if not fname.endswith(".tif"):
#                 continue
#             path = os.path.join(dirname, fname)
#             if os.path.isdir(path):
#                 continue
#             imgs.append(path)
#         f.write(img2pdf.convert(imgs))






    # num_pages = 50
    #
    # for page in range(num_pages):
    #     print('page', page)







    #
    # def get_concat_v_repeat(im, row):
    #     dst = Image.new('RGB', (im.width, im.height * row))
    #     for y in range(row):
    #         dst.paste(im, (0, y * im.height))
    #     return dst
    #
    # return 0





# def get_concat_h_multi_blank(im_list):
#     _im = im_list.pop(0)
#     for im in im_list:
#         _im = get_concat_h_blank(_im, im)
#     return _im
#
# get_concat_h_multi_blank([im1, im2, im1]).save('data/dst/pillow_concat_h_multi_blank.jpg')






#
# def get_concat_v(im1, im2):
#     dst = Image.new('RGB', (im1.width, im1.height + im2.height))
#     dst.paste(im1, (0, 0))
#     dst.paste(im2, (0, im1.height))
#     return dst





















    # print('images:')
    # print(images)
    #
    # # images = [Image.open(x) for x in ['Test1.jpg', 'Test2.jpg', 'Test3.jpg']]
    # widths, heights = zip(*(i.size for i in images))
    # total_width = sum(widths)
    # max_height = max(heights)
    # new_im = Image.new('RGB', (total_width, max_height))
    # x_offset = 0
    #
    # for im in images:
    #     new_im.paste(im, (x_offset, 0))
    #     x_offset += im.size[0]
    #     new_im.save('test.jpg')
    #
    # return new_im

    # pdf = PyPDF3.PdfFileReader(pdf)
    # num_pages = pdf.getNumPages()
    # writer = PyPDF3.PdfFileWriter()  # create a writer to save the updated results
    # for page in range(num_pages):
    #     page0 = pdf.getPage(page)
    #     page0.scaleBy(0.5)  # float representing scale factor - this happens in-place
    #     # writer = PyPDF2.PdfFileWriter()  # create a writer to save the updated results
    #     writer.addPage(page0)
    #     print('page added')
    #     with open('jpg_path', "wb+") as f:
    #         writer.write(f)




#
# # works
# def convert_pdf_to_tiff():
#     pdf_path = './pdf_images/1.pdf'
#     dirname = './jpg_images'
#     obj = ''
#     convert_from_path(pdf_path, output_folder=dirname, fmt='tiff')
#
#     # convert all files ending in .jpg inside a directory
#     # dirname = "/path/to/images"
#     with open("name.pdf", "wb") as f:
#         imgs = []
#         for fname in os.listdir(dirname):
#             if not fname.endswith(".tif"):
#                 continue
#             path = os.path.join(dirname, fname)
#             if os.path.isdir(path):
#                 continue
#             imgs.append(path)
#         f.write(img2pdf.convert(imgs))
# if __name__ == '__main__':
#     convert_pdf_to_tiff()



















#
# def convert_pdf_to_jpg():
#     pdf_path = './pdf_images/1.pdf'
#     jpg_path = './jpg_images'
#     output_folder1 = []
#     images = convert_from_path(pdf_path,output_folder=output_folder1, fmt='jpg')
#     print('images:')
#     print(images)
#     print(output_folder1)
#
#     # images = [Image.open(x) for x in ['Test1.jpg', 'Test2.jpg', 'Test3.jpg']]
#     widths, heights = zip(*(i.size for i in images))
#     total_width = sum(widths)
#     max_height = max(heights)
#     new_im = Image.new('RGB', (total_width, max_height))
#     x_offset = 0
#     for im in images:
#         new_im.paste(im, (x_offset, 0))
#         x_offset += im.size[0]
#         new_im.save('test.jpg')
#     image_file = Image.open(new_im)
#
#     # Changing the image resolution using quality parameter
#     image_file.save("1.pdf", quality=25, save_all=True)
#     return image_file




# CONVERTS TO WRONG IMAGE TYPE
# def convert_pdf_to_tiff():
#     pdf_images.save('test.Tiff', 'TIFF')
#     images = convert_from_bytes(open(pdf_images, 'rb').read())
#     with tempfile.TemporaryDirectory() as path:
#     images = convert_from_path('./pdf_images/1.pdf', output_folder='./jpg_images')
#     print('pdf converted')
#     return images
#








#
# def convert_pdf_to_tiff(directory_path: str, img_name: str):
    # convert PDF to TIFF
    # pdf_path = './pdf_images/1.pdf'
    # jpg_path = './jpg_images'
    # images_from_path = convert_from_path(pdf_path, output_folder=jpg_path)
    # # save tiff in tiff_images
    # print('pdf converted')
    # pdf_path = './pdf_images/1.pdf'
    #
    # pdf_path.save("PDF", resolution=50.0, save_all=True)
    #
    # return pdf_path
# from PIL import Image

# def convert_pdf_to_tiff(directory_path: str, img_name: str):
#     # pdf1_filename = "/Users/apple/Desktop/bbd1.pdf"
#     # im1 = Image.open("/Users/apple/Desktop/bbd.jpg")
#     #
#     # im1.save(pdf1_filename, "PDF", resolution=50.0, save_all=True)
#
#     image_path = './pdf_images/1.pdf'
#     jpg_path = './jpg_images'
#
#     # Open the image by specifying the image path.
#     # image_path = "image_name.jpeg"
#     image_file = Image.open(directory_path)
#
#     # Changing the image resolution using quality parameter
#     image_file.save("1.pdf", quality=25, save_all=True)
#
#     return image_file
#
#
if __name__ == '__main__':
    convert_pdf_to_tiff()

























#
# def convert_pdf_to_tiff():
#     pdf_path = './pdf_images/1.pdf'
#     temp_dir = tempfile.NamedTemporaryFile()
#     images = convert_from_path(pdf_path, fmt='tiff', size=800, dpi=300, grayscale=True,
#                       single_file=False, jpegopt={
#             "quality": 25,
#             "progressive": True,
#             "optimize": True
#         })
#
#
#
#     # convert all files ending in .tif inside a directory
#     with open("name.pdf", "wb") as f:
#         imgs = []
#         for fname in os.listdir(temp_dir):
#             if not fname.endswith(".tif"):
#                 continue
#             path = os.path.join(temp_dir, fname)
#             if os.path.isdir(path):
#                 continue
#             imgs.append(path)
#         f.write(img2pdf.convert(imgs))
#
#
# if __name__ == '__main__':
#     convert_pdf_to_tiff()
