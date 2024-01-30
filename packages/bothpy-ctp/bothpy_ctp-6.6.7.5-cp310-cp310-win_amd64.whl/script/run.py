from bothpy.event import EventEngine
from bothpy.trader.engine import MainEngine
from bothpy.trader.ui import MainWindow, create_qapp

from bothpy_ctp import CtpGateway


def main():
    """主入口函数"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    main_engine.add_gateway(CtpGateway)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()
