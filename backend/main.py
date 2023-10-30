import uvicorn

from conf import config

def main():
    uvicorn.run('app:app', **config)

if __name__ == "__main__":
    main()