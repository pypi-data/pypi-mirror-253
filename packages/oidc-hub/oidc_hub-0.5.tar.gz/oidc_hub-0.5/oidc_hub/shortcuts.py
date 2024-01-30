from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import resolve_url


def redirect(to, *args, permanent=False, status_code=None, **kwargs):
    """
    A replacement for the `redirect` function in Django that allows specifying a
    custom status code.

    :param      to:           The URL or view name to redirect to.
    :type       to:           str
    :param      args:         Positional arguments for the URL or view.
    :type       args:         list
    :param      permanent:    If True, perform a permanent redirect (status code
                              301), False by default.
    :type       permanent:    bool
    :param      status_code:  The custom status code to set for the redirect
                              response.
    :type       status_code:  int
    :param      kwargs:       Keyword arguments for the URL or view.
    :type       kwargs:       dict

    :returns:   A redirect response to the specified URL or view.
    :rtype:     HttpResponse
    """
    redirect_class = (
        HttpResponsePermanentRedirect if permanent else HttpResponseRedirect
    )
    response = redirect_class(resolve_url(to, *args, **kwargs))
    if status_code:
        response.status_code = status_code
    return response
