import uvicorn
import src

if __name__ == "__main__":
    config = src.config()
    uvicorn.run(src.build(), host=config.APP_HOST, port=config.APP_PORT)
