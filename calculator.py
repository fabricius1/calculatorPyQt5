#!/usr/bin/env python3

# Filename: calculator.py

"""Calculator is a simple calculator built using Python and PyQt5."""

import sys
from PyQt5.QtWidgets import QApplication

from src.model import evaluateExpression
from src.controller import PyCalcCtrl
from src.view import PyCalcUi


__version__ = '0.1.1'
__author__ = """Fabrício Brasil
(built on top of Leodanis Pozo Ramos's code)
"""


def main():
    """Main function."""
    # Create an instance of QApplication
    calculator = QApplication(sys.argv)

    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()

    # Create instances of the model and the controller
    model = evaluateExpression
    PyCalcCtrl(model=model, view=view)

    # Execute the calculator's main loop
    sys.exit(calculator.exec())


if __name__ == '__main__':
    main()
