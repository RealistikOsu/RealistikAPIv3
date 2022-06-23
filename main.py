from app.state.config import config

import uvicorn
import uvloop

uvloop.install()

def main() -> int:
    uvicorn.run(
        "app.init_api:fastapi_app",
        server_header= False,
        date_header= False,
        port= config.server_port,
    )
    
    return 0

if __name__ == "__main__":
    raise SystemExit(
        main()
    )
