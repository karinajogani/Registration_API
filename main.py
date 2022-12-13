import os
import uvicorn


'''
This main file and we have to run this file and this application
runs on uvicorn server on 7000 port.
'''

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=7000, lifespan="on", reload=True)
