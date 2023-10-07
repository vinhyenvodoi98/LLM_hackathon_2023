import os

import uvicorn

if __name__ == "__main__":
    os.environ["BACKEND_DATA"] = "MOCK"
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
