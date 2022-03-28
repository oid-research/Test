"""Main survey file.
"""
import os

from flask_login import current_user
from hemlock import User, Page
from hemlock.functional import compile, validate, test_response
from hemlock.questions import Check, Input, Label, Range, Select, Textarea
from hemlock import utils
from sqlalchemy_mutable.utils import partial


@User.route("/survey")
def seed():
    """Creates the main survey branch.

    Returns:
        List[Page]: List of pages shown to the user.
    """
    return [
        Page(
            name_input:= Input(
                "What's your name?",
                variable="name"
            )
        ),
        Page(
            Label(compile=partial(greet_user, name_input)),
            back=True
        )
    ]


def greet_user(greet_label, name_input):
    greet_label.label = f"Hello, {name_input.response}!"