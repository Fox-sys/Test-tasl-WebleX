from fastapi import FastAPI


from src.controllers.route_controller import RouteController

app = FastAPI()
route_controller = RouteController()
app.include_router(route_controller.router)
