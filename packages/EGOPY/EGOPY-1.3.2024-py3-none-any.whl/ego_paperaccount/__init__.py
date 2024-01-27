from pathlib import Path

import importlib_metadata
from egopy.trader.app import BaseApp

from .engine import PaperEngine, APP_NAME


class PaperAccountApp(BaseApp):
    """"""
    app_name = APP_NAME
    app_module = __module__
    app_path = Path(__file__).parent
    display_name = "EGOPY 系统测试"
    engine_class = PaperEngine
    widget_name = "PaperManager"
    icon_name = str(app_path.joinpath("ui", "paper.png"))
