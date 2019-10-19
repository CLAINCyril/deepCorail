# -*- coding: utf-8 -*-
from starlette.applications import Starlette
from starlette.responses import JSONResponse,HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import uvicorn, sys
from io import BytesIO
from modelWarpper import *
from PIL import Image
app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
model = load()
if __name__ == '__main__':
    if 'serve' in sys.argv: app.mount('/static', StaticFiles(directory='app/static'))
    if 'test' in sys.argv: app.mount('/static', StaticFiles(directory='app/static'))

@app.route('/')
def index(request):
    html = 'app/view/index.html'
    return HTMLResponse(open(html,encoding="utf-8").read())

@app.route('/test')
def index(request):
    
    return JSONResponse({})

@app.route("/upload", methods=["POST"])
async def upload(request):
    data = await request.form()
    files =  data.getlist('file')
    print(files)
    res = {}
    i = 0
    for f in files:
        bytess = await (f.read())
        image = Image.open(BytesIO(bytess))
        classe = predict_image(model,image)
        res[i] = {'class' : classe,'size':len(bytess)}
        i+=1
    return JSONResponse(res)


if __name__ == '__main__':
    if 'serve' in sys.argv: uvicorn.run(app, host='0.0.0.0', port=8080)
    if 'test' in sys.argv: uvicorn.run(app, host='localhost', port=3000)

