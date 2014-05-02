zca_snippets
========================================

* zca-list
* zca-snippets

zca-list

.. code:: shell

    $ zca-list pyramid.interfaces
    pyramid.interfaces:ITranslationDirectories
    pyramid.interfaces:INewRequest
    pyramid.interfaces:IRootFactory
    pyramid.interfaces:IDefaultRootFactory
    pyramid.interfaces:IViewMapperFactory
    pyramid.interfaces:IBeforeRender
    ## ..snip
    pyramid.interfaces:IExceptionViewClassifier
    pyramid.interfaces:ILocaleNegotiator
    pyramid.interfaces:IMultiDict
    pyramid.interfaces:IAuthenticationPolicy

zca-snippets

.. code:: shell

    $ zca-snippets pyramid.interfaces:IAuthenticationPolicy
    from zope.interface import implementer
    from pyramid.interfaces import IAuthenticationPolicy

    ## see: pyramid.interfaces:IAuthenticationPolicy
    @implementer(IAuthenticationPolicy)
    class AuthenticationPolicy(object):
        def remember(self, request, principal, **kw):
            pass

        def effective_principals(self, request):
            pass

        def forget(self, request):
            pass

        def authenticated_userid(self, request):
            pass

        def unauthenticated_userid(self, request):
            pass

.. code:: shell

	$ zca-snippets -q pyramid.interfaces:IAuthorizationPolicy
    ## see: pyramid.interfaces:IAuthorizationPolicy
    @implementer(IAuthorizationPolicy)
    class AuthorizationPolicy(object):
        def principals_allowed_by_permission(self, context, permission):
            pass

        def permits(self, context, principals, permission):
            pass
