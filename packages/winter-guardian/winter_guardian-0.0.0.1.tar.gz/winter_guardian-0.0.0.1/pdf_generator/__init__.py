import copy
from datetime import datetime

import pdfkit
from flask import redirect, url_for

global_options = {
    "quiet": "",
    "page-size": "A4",
    "margin-top": "0.75in",
    "margin-right": "0.75in",
    "margin-bottom": "0.75in",
    "margin-left": "0.75in",
    "encoding": "UTF-8",
    "no-outline": None,
    "dpi": 96,
    "zoom": 1,
    "footer-font-size": 9,
    "header-font-size": 9,
}


def pdf_export(static_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            options = copy.deepcopy(global_options)
            template_meta = func(*args, **kwargs)
            options.update({"options": template_meta.get("options", {})})

            now = datetime.now().strftime("%y%m%d%H%M%S")
            filename = f"{template_meta.get('file_prefix', '')}-{now}.pdf"
            output_path = f"{static_path}/{filename}"

            pdfkit.from_url(
                template_meta.get("url"),
                output_path,
                options=global_options,
            )
            return redirect(url_for("api.static", filename=filename))

        return wrapper

    return decorator
