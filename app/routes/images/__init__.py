"""
routes to /images, prefix="/images"
"""
from flask import Blueprint, request, Response, json, render_template

image_bp = Blueprint("router", __name__)


@image_bp.route("", methods=["POST"])
def transfer_style():
    style_img = request.files.get("style", None)
    target_img = request.files.get("target", None)
    if style_img is None or target_img is None:
        return Response(json.dumps({"message": "fail", "content": "argument missing"}), status=400)

    # TODO : 모델 나오면 style_img, target_img로 이미지 돌려주는 함수 만들기
    return Response("success")


@image_bp.route("")
def render_img_html():
    return render_template("index.html")
