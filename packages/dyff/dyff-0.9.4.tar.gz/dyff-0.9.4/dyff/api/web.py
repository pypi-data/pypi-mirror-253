# Copyright UL Research Institutes
# SPDX-License-Identifier: Apache-2.0

import fastapi
from fastapi.responses import HTMLResponse


def _generate_unique_id(route: fastapi.routing.APIRoute) -> str:
    """Strip everything but the function name from the ``operationId`` fields."""
    return route.name


def check_route_permissions(request: fastapi.Request) -> None:
    pass


app = fastapi.FastAPI(
    title="Dyff Cloud Console",
    generate_unique_id_function=_generate_unique_id,
    dependencies=[fastapi.Depends(check_route_permissions)],
)


@app.get("/")
def homepage() -> HTMLResponse:
    return HTMLResponse(
        "<body><p>I'm sorry, Dave. I'm afraid I can't do that.</p></body>"
    )
