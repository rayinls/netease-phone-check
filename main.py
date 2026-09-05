
from netease.client import NeteaseClient


def main():
    phone = input("请输入测试手机号：").strip()

    if not phone.isdigit():
        print("手机号格式不正确")
        return

    client = NeteaseClient()

    try:
        result = client.cellphone_existence_check(phone)

        print("接口返回：")
        print(result)

    except Exception as e:
        print("请求失败：")
        print(type(e).__name__)
        print(str(e))


if __name__ == "__main__":
    main()
