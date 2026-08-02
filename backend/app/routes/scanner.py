from fastapi import APIRouter, UploadFile, File
from app.services.scanner_service import scan_document

from docx import Document
import pdfplumber


router = APIRouter(
    prefix="/scanner",
    tags=["Scanner"]
)



def extract_text(file):

    filename = file.filename.lower()


    if filename.endswith(".txt"):

        content = file.file.read()

        return content.decode("utf-8")


    elif filename.endswith(".pdf"):

        text = ""

        with pdfplumber.open(file.file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"


        return text



    elif filename.endswith(".docx"):

        doc = Document(file.file)

        text = ""

        for para in doc.paragraphs:

            text += para.text + "\n"


        return text


    else:

        return ""




@router.post("/analyze")
async def analyze_file(
        file: UploadFile = File(...)
):


    text = extract_text(file)


    if text.strip()=="":
        return {
            "status":False,
            "message":"No text extracted"
        }


    result = scan_document(text)


    return {

        "status":True,

        "filename":file.filename,

        "result":result

    }