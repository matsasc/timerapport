from flask import Flask
from flask import request
from flask import send_file
from io import BytesIO

from generate_docx import makeDokument

app=Flask(__name__)


@app.route('/', methods=['GET'])
def get_document():
    document = makeDokument(request.args)
    f = BytesIO()
    document.save(f)
    f.seek(0)
    return send_file(f, as_attachment=True, attachment_filename='timerapport.docx')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)