
import base64
import hashlib
import json

from Crypto.Cipher import AES


EAPI_KEY = b"36cd479b6b5"


def md5_hex(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def aes_ecb_encrypt(data: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)

    padding = 16 - len(data) % 16
    data += bytes([padding]) * padding

    return cipher.encrypt(data)


def eapi(path: str, payload: dict) -> str:
    """
    网易云 EAPI 请求数据构造。

    path:
        例如 /api/cellphone/existence/check

    payload:
        要发送的 JSON 对象

    返回:
        params=xxxx
    """

    text = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
    )

    message = f"nobody{path}use{text}md5forencrypt"

    digest = md5_hex(message.encode("utf-8"))

    data = (
        f"{path}"
        f"-36cd479b6b5-"
        f"{text}"
        f"-36cd479b6b5-"
        f"{digest}"
    )

    encrypted = aes_ecb_encrypt(
        data.encode("utf-8"),
        EAPI_KEY,
    )

    return "params=" + encrypted.hex()
