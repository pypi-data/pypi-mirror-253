from routerfy import APIRouter, Response

router = APIRouter(prefix="/hello")

@router.get("/")
def hello_world_get_request():
    return "Hello World!"