# EditDateofChange

Simple Windows 10 utility with GUI that lets users set or edit the “last modified” date of photo and video files manually.

The finished executable file is located in the output directory.

## License

This project is licensed under the **Open-Source Attribution Only License (OSAO) 1.0**.  
You may use, modify, and distribute this software **only in open-source projects**, with mandatory attribution to the original author.

---

## Requirements

- Windows 10
- Python 3.10+
- ExifTool (Windows executable, included in repository, not installed via pip. Downloaded from https://exiftool.org)

---

## Setup (development)

Create virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate
```

Install Python dependencies:
```bash
pip install -r requirements.txt
```

Run application:
```bash
python main.py
```

## Build .exe
```bash
pip install auto-py-to-exe
```

Run GUI:
```bash
auto-py-to-exe
```

Make sure to include the exiftool folder as additional files when building the executable
