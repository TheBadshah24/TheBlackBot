# Credit @TheBlackXYZ.
# Please Don't remove credit
# TheBlackXYZBotz Forever !
# Thanks You For Help Us In This Amazing Creativity 
# Thanks You For Giving Me Credit @TheBlackXYZBotz
# For Any ERROR Please Contact Me -> Telegram ->@TheBlackXYZBotz & Insta @TheBlackXYZ
# Please Love & Support 💗💗🙏



from info import *
from aiohttp import web
from TheBlack import StartTime, __version__



routes = web.RouteTableDef()


@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("MovieVerse Is Alive")
