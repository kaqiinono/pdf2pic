from utils.file_picker import getalltxt, pyMuPDF_fitz
from utils.vedio import getFileList, getMP4

if __name__ == "__main__":
    # # 1、PDF地址
    # pdfPath = './files'
    # # 2、需要储存图片的目录
    # imagePath = './imgs'
    # fileList = []
    # getalltxt(pdfPath, fileList)
    #
    # for file in fileList:
    #     fileName = file.split("/")[-1].split('.')[0]
    #     try:
    #         pyMuPDF_fitz(file, imagePath + '/' + fileName)
    #     except:
    #         print('error:' + file)
    print("欢迎使用批量合成M4S工具")
    # fileDir = str(input("请输入含M4S文件的目录:"))
    f = getFileList('/Users/songmeinuo/Movies/bilibili/196435546/')
    getMP4(f[0], f[1])
    print("合成完毕")
