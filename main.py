from jwt import app
import uvicorn
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.authentication import requires

@requires('authenticated')
async def homepage(request):
    return JSONResponse({'hello': 'world'})

async def register(request):
    return JSONResponse({'hello': request.session['username']})

@requires('authenticated')
async def auth(request):
    return JSONResponse({'hello': 'world'})

@requires('authenticated')
async def refresh(request):
    return JSONResponse({'hello': 'world'})

@requires('authenticated')
async def revoke(request):
    return JSONResponse({'hello': 'world'})

my_routes = [
    Route('/', homepage),
    Route('/register', register),
    Route('/auth', auth),
    Route('/refresh', refresh),
    Route('/revoke', revoke)
]

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, routes=my_routes)


# python -m uvicorn main:app
