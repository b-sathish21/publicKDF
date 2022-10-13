
def convert_to_pdf(xlPath, pdfPath):
    import jpype
    import asposecells

    jpype.startJVM()
    from asposecells.api import Workbook, FileFormatType, PdfSaveOptions

    workbook = Workbook(xlPath)
    saveOptions = PdfSaveOptions()
    saveOptions.setOnePagePerSheet(True)
    workbook.save(pdfPath, saveOptions)

    jpype.shutdownJVM()
