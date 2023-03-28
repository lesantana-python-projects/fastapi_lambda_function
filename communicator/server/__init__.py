import importlib
import pkgutil
import inspect
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRouter
from communicator.configs import get_config
from communicator.exceptions import ErrorStartServer

configs = get_config()


class ServerCommunicator:

    def __prepare_url(self, router, module):
        for item in inspect.getmembers(module, inspect.isclass):
            module_search = item[0]
            if module_search == 'APIRouter':
                module_real = getattr(module, 'router')
                router.include_router(module_real)

    @staticmethod
    def __gen_submodule_names(package):
        for item in pkgutil.walk_packages(
                path=package.__path__,
                prefix=package.__name__ + '.',
                onerror=lambda x: None):
            modname = item[1]
            yield modname

    def __get_urls(self, views):
        router = APIRouter(prefix='/api')
        gen = self.__gen_submodule_names(views)
        for sub_modules in gen:
            module = importlib.import_module(sub_modules)
            self.__prepare_url(router, module)
        return router

    def make_app(self, views):
        app = FastAPI(title=configs.APP_TITLE,
                      version=configs.APP_VERSION, docs_url="/")
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        router = self.__get_urls(views)
        app.include_router(router)
        return app

    def start(self, views):
        try:
            app = self.make_app(views)
            return app
        except Exception as error:
            raise ErrorStartServer(str(error))
