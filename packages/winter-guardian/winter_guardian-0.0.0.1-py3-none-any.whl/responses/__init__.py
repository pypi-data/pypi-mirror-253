from flask import Response


def response(json_data, status: int = 200) -> Response:
    return Response(json_data, mimetype="application/json", status=status)
