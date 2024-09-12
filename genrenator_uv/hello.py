import httpx
import mistune
import quart

app = quart.Quart(__name__)


async def get_genre() -> str:
    httpx_client: httpx.AsyncClient = app.httpx_client
    response = await httpx_client.get(
        "https://binaryjazz.us/wp-json/genrenator/v1/genre/1"
    )

    # The above API returns a JSON string, so we call `response.json()` to evaluate it.
    return response.json()


@app.before_serving
async def startup():
    app.httpx_client = httpx.AsyncClient()


@app.after_serving
async def shutdown():
    await app.httpx_client.aclose()


@app.route("/")
async def index():
    genre = await get_genre()
    response = mistune.html(f"<big>Your *new favorite genre* is **{genre}**!</big>")
    return response


def main():
    app.run()
