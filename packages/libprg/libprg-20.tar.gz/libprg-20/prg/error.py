#!/usr/bin/env python3
# This file is placed in the Public Domain.
#
# pylint: disable=C,R,W0201,W0212,W0105,W0613,W0406,E0102,W0611,W0718,W0125


"deferred exception handling"


import io
import traceback


from obj import Object


class Error(Object):

    errors = []
    filter = []
    output = print
    shown  = []

    @staticmethod
    def add(exc) -> None:
        excp = exc.with_traceback(exc.__traceback__)
        Error.errors.append(excp)

    @staticmethod
    def format(exc) -> str:
        res = ""
        stream = io.StringIO(
                             traceback.print_exception(
                                                       type(exc),
                                                       exc,
                                                       exc.__traceback__
                                                      )
                            )
        for line in stream.readlines():
            res += line + "\n"
        return res

    @staticmethod
    def handle(exc) -> None:
        if Error.output:
            txt = str(Error.format(exc))
            Error.output(txt)

    @staticmethod
    def show() -> None:
        for exc in Error.errors:
            Error.handle(exc)

    @staticmethod
    def skip(txt) -> bool:
        for skp in Error.filter:
            if skp in str(txt):
                return True
        return False


def debug(txt):
    if Error.output and not Error.skip(txt):
        Error.output(txt)
