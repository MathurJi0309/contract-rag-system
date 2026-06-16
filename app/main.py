from fastapi import FastAPI
app=FastAPI(title='Contract-rag-system')


@app.get('/test')
def test():
    return {'message':'Working fine'}
