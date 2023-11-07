import uvicorn

from conf import uvicorn_config

def main():
    uvicorn.run("app:app", **uvicorn_config)

if __name__ == "__main__":
    main()