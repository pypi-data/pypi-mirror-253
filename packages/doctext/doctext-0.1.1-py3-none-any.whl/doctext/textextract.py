import tempfile, shutil, os
from pathlib import Path
from tika import parser
from PIL import Image
import pytesseract
from termcolor import cprint
import magic
from openai import OpenAI
import chardet
from doctext.utils import run_checked

def is_plain_text(mimetype: str) -> bool:
    if mimetype and mimetype.startswith('text/'):
        return True
    if mimetype and '/json' in mimetype:
        return True
    if mimetype and '/yaml' in mimetype:
        return True
    if mimetype and '/xml' in mimetype:
        return True
    if mimetype and '/csv' in mimetype:
        return True
    if mimetype and '/markdown' in mimetype:
        return True
    if mimetype and '/html' in mimetype:
        return True
    if mimetype and '/xhtml' in mimetype:
        return True
    return False

def extract_pdf(file_path: str) -> str|None:
    try:
        with tempfile.TemporaryDirectory() as tmpdirname:
            tmpf = os.path.join(tmpdirname, 'text.txt')
            if run_checked(["pdftotext", "-enc", "UTF-8", file_path, tmpf]):
                with open(tmpf, 'r') as file:
                    return file.read()
    except Exception as e:
        print(f"Failed to extract text from {file_path}")
        print(e)
    return None

def extract_plain_text(file_path: str) -> str|None:
    try:
        # Detect encoding
        with open(file_path, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']

        # Read the file with detected encoding
        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read()

        # Convert to UTF-8
        return content.encode('utf-8')
    except Exception as e:
        print(f"Failed to extract plain text from {file_path}")
        print(e)
        return None

def convert_to_string_if_bytes(text):
    if isinstance(text, bytes):
        detected_encoding = chardet.detect(text)['encoding']
        if detected_encoding:
            return text.decode(detected_encoding)
        else:
            print("Unable to detect encoding for byte conversion. Using UTF-8.")
            return text.decode('utf-8')
    else:
        return text

def extract_text_postprocess(func):
    """Decorator to perform postprocessing on extracted text."""
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        text = convert_to_string_if_bytes(text)
        # Postprocess the text
        if text:
            return text.replace('\x00', '')
        return text
    return wrapper

def ocr(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Failed to OCR {image_path}")
        print(e)
        return None


def extract_text_from_image(image_path: str) -> str|None:

    def heic_to_png(src: str, dest: str) -> bool:
        if run_checked(["heif-convert", src, dest]):
            return os.path.exists(dest)
        return False

    def cr2_to_png(src: str, dest: str) -> bool:
        if run_checked(["dcraw", "-c", "-w", src, "|", "pnmtopng", ">", dest]):
            return os.path.exists(dest)
        return False

    def any_to_png_pil(src: str, dest: str) -> bool:
        try:
            with Image.open(src) as img:
                img.save(dest, 'PNG')
                return os.path.exists(dest)
        except:
            return False

    def any_to_png_im(src: str, dest: str) -> bool:
        if run_checked(["convert", src, dest]):
            return os.path.exists(dest)
        return False
    
    def any_to_png_ffmpeg(src: str, dest: str) -> bool:
        if run_checked(["ffmpeg", "-i", src, "-vf", "scale=1920:-1", dest]):
            return os.path.exists(dest)
        return False

    def to_png(src: str, dest: str) -> bool:
        if any_to_png_pil(src, dest):
            return True
        elif any_to_png_im(src, dest):
            return True
        elif any_to_png_ffmpeg(src, dest):
            return True
        elif heic_to_png(src, dest):
            return True
        elif cr2_to_png(src, dest):
            return True
        else:
            return False

    # guess mimetype
    mime = magic.Magic(mime=True)
    mimetype = mime.from_file(image_path)

    # convert video to sequence of images
    if mimetype not in ['image/jpeg','image/png','image/jpg'] or Path(image_path).suffix == '.jpe':
        with tempfile.TemporaryDirectory() as tmpdirname:
            tmpimg = os.path.join(tmpdirname, 'image.png')
            if to_png(image_path, tmpimg):
                return ocr(tmpimg)
            else:
                cprint(f"Cannot convert {image_path} to PNG", "red")
                return None

    return ocr(image_path)
    
def extract_text_from_video(f: Path) -> str:
    text = []
    with tempfile.TemporaryDirectory() as tmpdirname:
        if run_checked(["ffmpeg", "-i", str(f), f"{tmpdirname}/image%d.jpg"]):
            images = sorted(os.path.abspath(os.path.join(tmpdirname, f)) for f in os.listdir(tmpdirname) if f.endswith('.jpg'))
            for image in images:
                try:
                    text.append(ocr(image))
                except Exception as ex:
                    cprint(f"Cannot extract text from {image}\n{ex}", "red")
        return " ".join(text)

def extract_text_from_audio(f: Path, openai_api_key: str) -> str|None:
    
    # check if we have an API key
    if openai_api_key is None:
        cprint("No OpenAI API key provided. Skipping audio to text conversion.", "yellow")
        return None

    client = OpenAI(api_key=str(openai_api_key))    
    try:
        with tempfile.TemporaryDirectory() as tmpdirname:
            tmpf = os.path.join(tmpdirname, 'audio.m4a')
            if run_checked(["ffmpeg", "-i", str(f), "-c:a", "aac", "-b:a", "192k", tmpf]):
                return client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=open(tmpf, "rb"),
                    response_format="text"
                )
    except Exception as ex:
        print(f"Cannot extract text from {str(f)}\n{ex}")
    return None

def tika(file_path):
    try:
        parsed = parser.from_file(file_path)        
        return parsed['content']
    except Exception as e:
        print(f"Failed to extract text with tika from {file_path}")
        print(e)
        return None

@extract_text_postprocess
def extract_text(file_path: str, openai_api_key: str = None) -> str|None:

    mime = magic.Magic(mime=True)
    mimetype = mime.from_file(file_path)

    # try special handlers
    if is_plain_text(mimetype):
        return extract_plain_text(file_path)
    if mimetype and mimetype.startswith('image/'):
        return extract_text_from_image(file_path)
    if mimetype and mimetype.startswith('video/'):
        return extract_text_from_video(file_path)
    if mimetype and mimetype.startswith('audio/'):
        return extract_text_from_audio(file_path, openai_api_key)
    if mimetype and mimetype.startswith('application/pdf'):
        return extract_pdf(file_path)

    # try tika
    return tika(file_path)