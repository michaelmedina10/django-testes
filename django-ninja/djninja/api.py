from ninja import NinjaAPI
from tracks.router import router as tracks_router

api = NinjaAPI()
api.add_router("/api/v1", tracks_router)
