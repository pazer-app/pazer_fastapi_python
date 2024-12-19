from pazer_core_python import Core
from Config import config
from Router import Routing

core = Core(config=config(), fetch=True)
app = core.app
Routing(core.app)
