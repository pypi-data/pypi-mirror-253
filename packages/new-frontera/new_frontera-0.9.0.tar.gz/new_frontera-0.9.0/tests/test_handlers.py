import unittest
import logging
import logging.config

from new_frontera.logger.handlers import CONSOLE
from tests.utils import SetupDefaultLoggingMixin, LoggingCaptureMixin, colors


class SetupHandler(SetupDefaultLoggingMixin):
    @classmethod
    def setUpClass(cls):
        super(SetupHandler, cls).setUpClass()
        l = logging.getLogger("new_frontera")
        l.handlers[0] = cls.handler


class TestHandlerConsole(SetupHandler, LoggingCaptureMixin, unittest.TestCase):
    handler = CONSOLE

    def test_handler_color_based_on_level(self):
        self.logger.debug("debug message")
        self.logger.info("info message")
        self.logger.error("error message")
        self.assertEqual(
            self.logger_output.getvalue(),
            "{white}[new_frontera] debug message{reset}\n"
            "{green}[new_frontera] info message{reset}\n"
            "{red}[new_frontera] error message{reset}\n".format(
                white=colors["white"],
                green=colors["green"],
                red=colors["red"],
                reset=colors["reset"],
            ),
        )
