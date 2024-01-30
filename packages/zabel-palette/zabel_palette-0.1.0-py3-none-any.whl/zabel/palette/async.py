"""Asynchronous helpers.

A bit like concurrent.futures, but without the Executor requirement.
"""

__all__ = [
    'async_call',
    'async_map',
    'async_await',
    'collect',
]


import queue
import threading


########################################################################
# Functions


def _submit(f, *a):
    """Return a started deamon thread computing f on *a."""
    t = threading.Thread(target=f, args=a)
    t.deamon = True
    t.start()
    return t


def async_call(f):
    """Return an asynchronous computation of calling f.

    f is a function of zero arguments that returns an iterable.
    """
    q = queue.Queue()
    return [q, _submit(lambda q: q.put(f()), q)]


def async_map(f, xs):
    """Return an asynchronous computation of calling f on elements of xs.

    f is a function of one argument, an x (member of xs), that
        returns an iterable.
    xs is an iterable.
    """
    q = queue.Queue()
    return [q] + [_submit(lambda x, q: q.put(f(x)), x, q) for x in xs]


def async_await(ac):
    """Return the result of an asynchronous computation."""
    allc = []
    for t in ac[1:]:
        t.join()
        allc += ac[0].get()

    return allc


def collect(f, xs):
    """Return the aggregated result of calling f on elements of xs.

    f is a function of one argument, an x (member of xs), that
        returns an iterable.
    xs is an iterable.

    f runs in parallel on elements of xs.

    It is equivalent to async_await(async_map(f, xs)).
    """
    return async_await(async_map(f, xs))
