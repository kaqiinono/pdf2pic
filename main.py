from utils.file_picker import getalltxt, pyMuPDF_fitz

if __name__ == "__main__":
    # 1、PDF地址
    pdfPath = './files'
    # 2、需要储存图片的目录
    imagePath = './imgs'
    fileList = []
    getalltxt(pdfPath, fileList)

    for file in fileList:
        fileName = file.split("/")[-1].split('.')[0]
        try:
            pyMuPDF_fitz(file, imagePath + '/' + fileName)
        except:
            print('error:' + file)
