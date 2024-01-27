import requests
from .config import URL, API_KEY


def hello() -> None:
    print("Hello, world from vihub")


def addImage(
    monitoringId: str,
    imageBytes: bytes,
    imageTitle: str,
    imageType: str,
    predLabel: str = None,
) -> str:
    res = requests.request(
        "POST",
        URL,
        headers={"apiKey": API_KEY},
        data={"monitoringId": monitoringId, "predLabel": predLabel},
        files=[
            (
                "image",
                (
                    imageTitle,
                    imageBytes,
                    imageType,
                ),
            )
        ],
    )

    print(res.text)
    return res.text
