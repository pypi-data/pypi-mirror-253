Tutorial: a real world sample
==============================

.. demo:: Demonstration : configuring (the setting of) your favorite web browser

    This tutorial shows to you an example of Rougail use on
    how to set a proxy in the `Mozilla Firefox <https://www.mozilla.org/en-US/firefox/new/>`_ browser.

More precisely, this tutorial aims at reproducing this Mozilla Firefox settings page:

.. image:: images/firefox.png

.. important:: Here we are in the configuration validation use case,
               that is the values entered by the user have to be validated.
               It's a common use case, but not the only one.

Let's explain this use case.

The Firefox proxy configuration
-------------------------------------------

The `proxy` family
-------------------

Let's create our first :term:`dictionary`.

.. prerequisites:: Let's create a folder named `dict` and a dictionary file inside

We will put our dictionary files in this folder.

Then let's put our first dictionary file in this folder, named :file:`00-proxy.yml`

.. code-block:: yaml
   :caption: the :file:`00-proxy.yml` file
   :linenos:

    ---
    version: '1.0'
    proxy:
      description: Proxy configuration in order to have access to the internet
      type: family

We can see that we have defined a :term:`family` here, and this family is *empty*
(that is, the family container contains no variable yet).

.. admonition:: If a family is empty

    We need to specify the :term:`family` type (line 5) here because if we don't,
    the Rougail's type engine will infer it by default as a :term:`variable`.

It's because we don't have set any :term:`variable` inside.


.. note:: The variables will be created in several files for educational purposes.
          Obviously all the variables can be put in the same file.


The proxy's configuration type
----------------------------------

In the Firefox configuration, it is possible to define several configuration modes,
from no proxy at all (`no proxy`) to a kind of automatic configuration mode from a file (`set up proxy configuration from a file`).

We're gonna create a first variable in this family with "Proxy mode" as the description.
Let's create a second :file:`dict/01-proxy_mode.yml` file.

.. code-block:: yaml
   :caption: the :file:`001-proxy_mode.yml` file
   :linenos:

    ---
    version: '1.0'
    proxy:
      proxy_mode:
        description: Proxy mode
        type: choice
        choices:
          - No proxy
          - Auto-detect proxy settings for this network
          - Use system proxy settings
          - Manual proxy configuration
          - Automatic proxy configuration URL
        default: No proxy

The `proxy_mode` variable requires a value (that is, `None` is not an option).
It shall have a value, but what if the user *does not* specify any value?
There is line 13, a possibility of setting a default value, wich is `No proxy` as the default.

The `proxy_mode` setting is "choice" (`type: choice`) means that
there is a list of available values that can be selected.
We say that the `proxy_mode` variable is *constrained* (by choices).

Line 8 to 12, we have the list of the possible (authorized) values:

- No proxy
- Auto-detect proxy settings for this network
- Use system proxy settings
- Manual proxy configuration
- Automatic proxy configuration URL

Now let's test our first two dictionaries:


>>> from rougail import Rougail, RougailConfig
>>> from pprint import pprint
>>> RougailConfig['dictionaries_dir'] = ['dict']
>>> rougail = Rougail()
>>> config = rougail.get_config()
>>> config.property.read_only()
>>> pprint(config.value.get(), sort_dicts=False)
{'rougail.proxy.proxy_mode': 'No proxy'}

The manual mode
------------------

.. questions:: OK then. What happens when you select the "Manual proxy configuration"?

A good configuration design is to place all the proxy's manual configuration in a :term:`family`.
Let's create the :file:`dict/02-proxy_manual.yml` dictionary:

.. code-block:: yaml
   :caption: the the :file:`dict/02-proxy_manual.yml` file

    ---
    version: '1.0'
    proxy:
      manual:
        description: Manual proxy configuration
        type: family
        disabled:
          type: jinja
          jinja: |
            {% if rougail.proxy.proxy_mode != 'Manual proxy configuration' %}
            the proxy mode is not manual
            {% endif %}

Well, if the user selects the "Manual proxy configuration" proxy mode, we want to see a new subfamily (that is, a new set of configuration variables) called `manual` to appear (which is disabled).

.. glossary::

   subfamily

       A subfamily is just a family inside a family, a family that contains a family.

.. questions:: What about this `Jinja` type?

If the :term:`Jinja` template returns some text, then the family will be `disabled`. Otherwise it is accessible.
Deactivating a family means that we will not be able to access it as well as the variables or families included in this family.

.. note:: If the Jinja template does not return any text, the variable will be **enabled**.
          Here we are using the Jinja condition statement.

.. glossary::

    Jinja

        `Jinja <https://jinja.palletsprojects.com>`_ is a template engine.
        we are using Jinja in a classical way, that is, Jinja allows us to handle different cases,
        for example with the `if` statement.

The HTTP proxy configuration
------------------------------

In this family let's add a *subfamily* named `http_proxy`, containing the address and port configuration variables.

Let's create the :file:`dict/03-proxy_manual_http_proxy.yml` dictionary:

.. code-block:: yaml
   :caption: the the :file:`dict/02-proxy_manual.yml` file
   :linenos:

    ---
    version: '1.0'
    proxy:
      manual:
        http_proxy:
          description: HTTP Proxy
          address:
            description: HTTP address
            type: domainname
          port:
            description: HTTP Port
            type: port
            default: '8080'

Both variables `address` and `port` have particular types (respectively `domainname` line 9 and `port` line 12) to validate the values configured by the user.

.. note:: No need to specify the type of the `http_proxy` as a family type, because here we have declared variables inside of it.

Duplicating the HTTP configuration to HTTPS
---------------------------------------------

We then want to offer the user the possibility of providing the same proxy for the HTTPS requests. Let's create the :file:`dict/04-proxy_manual_http_use_for_https.yml` file:

.. code-block:: yaml
   :caption: the :file:`dict/04-proxy_manual_http_use_for_https.yml` file

    version: '1.0'
    proxy:
      manual:
        use_for_https:
          description: Also use this proxy for HTTPS
          type: boolean

This variable is a `boolean` type, its default value is `True`.

HTTPS proxy configuration detail
-----------------------------------

Let's add a new subfamily named `ssl_proxy`, containing the `address` and `port` variables.

Let's create the :file:`dict/05-proxy_manual_ssl_proxy.yml` file:

.. code-block:: yaml
   :caption: the :file:`dict/04-proxy_manual_http_use_for_https.yml` file
   :linenos:

    ---
    version: '1.0'
    proxy:
      manual:
        ssl_proxy:
          description: HTTPS Proxy
          hidden:
            type: variable
            variable: rougail.proxy.manual.use_for_https
          address:
            description: HTTPS address
            type: domainname
            default:
              type: jinja
              jinja: |
                {% if rougail.proxy.manual.use_for_https %}
                {{ rougail.proxy.manual.http_proxy.address }}
                {% endif %}
          port:
            description: HTTPS Port
            type: port
            default:
              type: jinja
              jinja: |
                {% if rougail.proxy.manual.use_for_https %}
                {{ rougail.proxy.manual.http_proxy.port }}
                {% endif %}


Depending on the value of the `rougail.proxy.mandatory.use_for_https` variable, this family will appear or disappear (the `hidden` setting line 7). Unlike earlier, this time it is not necessary to use a Jinja function.

Let's notice that the family is not disabled because the variables will need to remain accessible (yet in `read-only` mode).

The address and port variables are copied from HTTP to HTTPS if `rougail.proxy.use_for_https` is set to `True`.

Now let's test all of it:

>>> from rougail import Rougail, RougailConfig
>>> from pprint import pprint
>>> RougailConfig['dictionaries_dir'] = ['dict']
>>> rougail = Rougail()
>>> config = rougail.get_config()
>>> config.property.read_only()
>>> pprint(config.value.get(), sort_dicts=False)
{'rougail.proxy.proxy_mode': 'No proxy'}

At this time the proxy is not configured yet, so we do not see any variables.
Let's look at what happens if we try to access the `rougail.proxy.manual` variable if we are not in manual mode:

.. code-block:: python

    >>> pprint(config.option('rougail.proxy.manual').value.get(), sort_dicts=False)

We have an error (with the message defined in the Jinja template):


.. code-block:: python

    tiramisu.error.PropertiesOptionError: cannot access to optiondescription "Manual proxy configuration" because has property "disabled" (the mode proxy is not manual)

Let's configure the proxy in manual mode

>>> config.property.read_write()
>>> config.option('rougail.proxy.proxy_mode').value.set('Manual proxy configuration')
>>> config.option('rougail.proxy.manual.http_proxy.address').value.set('proxy.example')
>>> pprint(config.value.get(), sort_dicts=False)

We can see that the returned variables does have the desired values:

.. code-block:: python

    {'rougail.proxy.proxy_mode': 'Manual proxy configuration',
     'rougail.proxy.manual.http_proxy.address': 'proxy.example',
     'rougail.proxy.manual.http_proxy.port': '8080',
     'rougail.proxy.manual.use_for_https': True}

Let's set the `read_only` mode:

.. code-block:: python

    >>> config.property.read_only()
    >>> pprint(config.value.get(), sort_dicts=False)
    {'rougail.proxy.proxy_mode': 'Manual proxy configuration',
     'rougail.proxy.manual.http_proxy.address': 'proxy.example',
     'rougail.proxy.manual.http_proxy.port': '8080',
     'rougail.proxy.manual.use_for_https': True,
     'rougail.proxy.manual.ssl_proxy.address': 'proxy.example',
     'rougail.proxy.manual.ssl_proxy.port': '8080'}

In the `read_only` mode, we can see that the HTTPS configuration appears.

.. note:: We can see that `rougail.proxy.manual.http_proxy` values have been copied
          in `rougail.proxy.manual.ssl_proxy` too...

Changing values programmatically
--------------------------------------

We are going to use the :term:`Tiramisu` API to manipulate programmatically the different variables.

First, let's set `rougail.proxy.manual.use_for_https` to `False`. It is now possible
to configure the HTTPS:

.. code-block:: python

    >>> config.property.read_write()
    >>> config.option('rougail.proxy.manual.use_for_https').value.set(False)
    >>> config.option('rougail.proxy.manual.ssl_proxy.address').value.set('other.proxy.example')
    >>> pprint(config.value.get(), sort_dicts=False)
    {'rougail.proxy.proxy_mode': 'Manual proxy configuration',
     'rougail.proxy.manual.http_proxy.address': 'proxy.example',
     'rougail.proxy.manual.http_proxy.port': '8080',
     'rougail.proxy.manual.use_for_https': False,
     'rougail.proxy.manual.ssl_proxy.address': 'other.proxy.example',
     'rougail.proxy.manual.ssl_proxy.port': '8080'}

The value of the variable `rougail.proxy.manual.ssl_proxy.address` has actually been modified.
But if this variable is hidden again, then the value comes back to the default value:

.. code-block:: python

    >>> config.option('rougail.proxy.manual.use_for_https').value.set(False)
    >>> config.property.read_only()
    >>> pprint(config.value.get(), sort_dicts=False)
    {'rougail.proxy.proxy_mode': 'Manual proxy configuration',
     'rougail.proxy.manual.http_proxy.address': 'proxy.example',
     'rougail.proxy.manual.http_proxy.port': '8080',
     'rougail.proxy.manual.use_for_https': False,
     'rougail.proxy.manual.ssl_proxy.address': 'proxy.example',
     'rougail.proxy.manual.ssl_proxy.port': '8080'}

SOCK's proxy configuration
-------------------------------

Let's add a new :term:`subfamily` named `socks_proxy` with the `address`,
`port` and `version` variables.

Let's create the :file:`dict/06-proxy_manual_socks_proxy.yml` file:

.. code-block:: yaml
   :caption: the :file:`dict/06-proxy_manual_socks_proxy.yml` file

    ---
    version: '1.0'
    proxy:
      manual:
        socks_proxy:
          description: SOCKS Proxy
          address:
            description: SOCKS Address
            type: domainname
          port:
            description: SOCKS Port
            type: port
          version:
            description: SOCKS host version used by proxy
            type: choice
            choices:
              - v4
              - v5
            default: v5

There's nothing new to learn with this file.

The automatic detection mode
------------------------------

Let's add a new variable named `auto`.

Let's create the :file:`dict/07-proxy_auto.yml` file:

.. code-block:: yaml
   :caption: the :file:`dict/07-proxy_auto.yml` file

    ---
    version: '1.0'
    proxy:
      auto:
        type: web_address
        description: Automatic proxy configuration URL
        disabled:
          type: jinja
          jinja: |
            {% if rougail.proxy.proxy_mode != 'Automatic proxy configuration URL' %}
            the proxy mode is not automatic
            {% endif %}

The `web_address` type imposes a value starting with `http://` or `https://`.
This variable is activated when the proxy is in automatic mode.

The proxy's exceptions
---------------------------

Finally, let's add a variable containing proxy exceptions.

Let's create the :file:`dict/07-proxy_no_proxy.yml` file:

.. code-block:: yaml
   :caption: the :file:`dict/07-proxy_no_proxy.yml` file
   :linenos:

    ---
    version: '1.0'
    proxy:
      no_proxy:
        description: Address for which proxy will be desactivated
        multi: true
        type: "domainname"
        params:
          allow_ip: true
          allow_cidr_network: true
          allow_without_dot: true
          allow_startswith_dot: true
        disabled:
          type: jinja
          jinja: |
            {% if rougail.proxy.proxy_mode == 'No proxy' %}
            proxy mode is no proxy
            {% endif %}
        mandatory: false

This `no_proxy` variable is much like a `domainname` type except that we add
a `params` line 7, we authorize the :

- IP
- CIDR networks
- machine names (without `'.'`)
- sub-domaines like `.example`

There can be multiple exceptions to the proxy, so the variable is :term:`multi` (line5).
This variable is only accessible if no proxy is defined (`disabled`).

.. glossary::

   multi

       A multi is a multiple variable, that is a variable that can have multiple values.


The `no_proxy` variable do not requires a value (that is, `None` is an option),
there is line 19 this statement `mandatory: false` which means that this variable is not mandatory.


Let's test it:


>>> from rougail import Rougail, RougailConfig
>>> from pprint import pprint
>>> RougailConfig['dictionaries_dir'] = ['dict']
>>> rougail = Rougail()
>>> config = rougail.get_config()
>>> config.property.read_write()
>>> config.option('rougail.proxy.proxy_mode').value.set('Manual proxy configuration')
>>> config.option('rougail.proxy.manual.http_proxy.address').value.set('proxy.example')
>>> config.option('rougail.proxy.no_proxy').value.set(['.example', '192.168.1.1'])
>>> config.property.read_only()
>>> pprint(config.value.get(), sort_dicts=False)

It outputs:

.. code-block:: python

    {'rougail.proxy.proxy_mode': 'Manual proxy configuration',
     'rougail.proxy.manual.http_proxy.address': 'proxy.example',
     'rougail.proxy.manual.http_proxy.port': '8080',
     'rougail.proxy.manual.use_for_https': True,
     'rougail.proxy.manual.ssl_proxy.address': 'proxy.example',
     'rougail.proxy.manual.ssl_proxy.port': '8080',
     'rougail.proxy.manual.socks_proxy.address': None,
     'rougail.proxy.manual.socks_proxy.port': None,
     'rougail.proxy.manual.socks_proxy.version': 'v5',
     'rougail.proxy.no_proxy': ['.example', '192.168.1.1']}

But not possible to put an invalid value:

.. code-block:: python

    >>> config.option('rougail.proxy.no_proxy').value.set(['.example', '192.168.1.1', 'not valid'])
    [..]
    tiramisu.error.ValueOptionError: "not valid" is an invalid domain name for "Address for which proxy will be desactivated", could be a IP, otherwise must start with lowercase characters followed by lowercase characters, number, "-" and "." characters are allowed


The authentification request
--------------------------------

Nothing special when creating the authentication request. To do this, let's create a `dict/08-proxy_prompt_authentication.yml` file:


.. code-block:: yaml
   :caption: the :file:`dict/08-proxy_prompt_authentication.yml` file
   :linenos:

    ---
    version: '1.0'
    proxy:
      prompt_authentication:
        description: Prompt for authentication if password is saved
        type: boolean
        default: true
        disabled:
          type: jinja
          jinja: |
            {% if rougail.proxy.proxy_mode == 'No proxy' %}
            proxy mode is no proxy
            {% endif %}

The proxy SOCKS v5's DNS
------------------------------

The DNS variable for the SOCKS v5 proxy only appears if the proxy is configured and the version of the SOCKS proxy selected is `v5`.

Let's create a `dict/09-proxy_proxy_dns_socks5.yml` file:

.. code-block:: yaml
   :caption: the :file:`dict/09-proxy_proxy_dns_socks5.yml` file
   :linenos:

    ---
    version: '1.0'
    proxy:
      proxy_dns_socks5:
        description: Use proxy DNS when using SOCKS v5
        type: boolean
        default: false
        disabled:
          type: jinja
          params:
            socks_version:
              type: variable
              variable: rougail.proxy.manual.socks_proxy.version
              propertyerror: false
          jinja: |
            {% if rougail.proxy.proxy_mode == 'No proxy' %}
            the proxy mode is no proxy
            {% elif socks_version is undefined or socks_version == 'v4' %}
            socks version is v4
            {% endif %}

The difficulty here is that the  `rougail.proxy.manual.socks_proxy.version` variable
can be deactivated (and therefore not usable in a calculation).

.. FIXME definir ce qu'est une calculation

In this case, we will add a parameter (here called `socks_version`) which will contain,
if there is no property error, the value of the variable.
Otherwise the parameter will not be passed to the Jinja template.

This is why it is necessary to test in the Jinja template whether the `socks_version` variable really exists.

The DNS over HTTPS
----------------------

Finally we will configure DNS over HTTPS in the 10-proxy_dns_over_https.yml file:

Let's create a `dict/10-proxy_dns_over_https.yml` file:

.. code-block:: yaml
   :caption: the :file:`dict/10-proxy_dns_over_https.yml` file
   :linenos:

    ---
    version: '1.0'
    proxy:
      dns_over_https:
        description: DNS over HTTPS
        enable_dns_over_https:
          description: Enable DNS over HTTPS
          type: boolean
          default: false
        provider:
          description: Use Provider
          type: choice
          choices:
            - Cloudflare
            - NextDNS
            - Custom
          default: Cloudflare
          disabled:
            type: jinja
            jinja: |
              {% if not rougail.proxy.dns_over_https.enable_dns_over_https %}
              Enable DNS over HTTPS is False
              {% endif %}
        custom_dns_url:
          description: Custom DNS URL
          type: web_address
          disabled:
            type: jinja
            params:
              provider:
                type: variable
                variable: rougail.proxy.dns_over_https.provider
                propertyerror: false
            jinja: |
              {% if provider is not defined or provider != 'Custom' %}
              provider is not custom
              {% endif %}
          validators:
            - type: jinja
              jinja: |
                {% if rougail.proxy.dns_over_https.custom_dns_url.startswith('http://') %}
                only https is allowed
                {% endif %}

.. FIXME : define validators

The only particularity here is that we added additional validation (validators) to the `custom_dns_url` variable. Only an address starting with `https://` is allowed (not `http://`).

----

The FoxyProxy type's proxy configuration
--------------------------------------------

Here is now the integration of part of the Firefox FoxyProxy plugin.

The idea is to have a namespace specific to FoxyProxy and to find in it part of the settings that we will have made in the main namespace.

This is what the page looks like:

.. image:: images/foxyproxy.png

It is possible, in this plugin, to specify an unlimited number of proxies.
Our `proxy` family will no longer be of the `family` type as before but of another type : the :term:`leadership` type.

.. FIXME: expliquer ce qu'est le type leardership

Here is the complete content of the FoxyProxy type proxy configuration
(to be put in the `foxyproxy/00-base.yml` file):

.. code-block:: yaml
   :caption: the :file:``foxyproxy/00-base.yml`` file
   :linenos:

    ---
    version: '1.0'
    proxy:
      _type: leadership
      title:
        description: Title or Description
        multi: true
      color:
        description: Color
      type:
        type: choice
        choices:
          - HTTP
          - HTTPS/SSL
          - SOCKS5
          - SOCKS4
          - PAC URL
          - WPAD
          - System (use system settings)
          - Direct (no proxy)
        default: Direct (no proxy)
      address:
        description: IP address, DNS name, server name
        multi: true
        disabled:
          type: jinja
          jinja: |
            {% if foxyproxy.proxy.type not in ['HTTP', 'HTTPS/SSL', 'SOCKS5', 'SOCKS4'] %}
            proxy does not need address
            {% endif %}
        default:
          type: jinja
          params:
            firefox_address:
              type: variable
              variable: rougail.proxy.manual.http_proxy.address
              propertyerror: false
          jinja: |
            {% if firefox_address is not undefined %}
            {{ firefox_address }}
            {% endif %}
      port:
        description: Port
        type: port
        default:
          type: jinja
          params:
            firefox_port:
              type: variable
              variable: rougail.proxy.manual.http_proxy.port
              propertyerror: false
          jinja: |
            {% if firefox_port is not undefined %}
            {{ firefox_port }}
            {% endif %}
        disabled:
          type: jinja
          jinja: |
            {% if foxyproxy.proxy.type not in ['HTTP', 'HTTPS/SSL', 'SOCKS5', 'SOCKS4'] %}
            proxy does not need port
            {% endif %}
      username:
        description: Username
        type: unix_user
        mandatory:
          type: jinja
          jinja: |
            {% if foxyproxy.proxy.password %}
            username is mandatory
            {% endif %}
        disabled:
          type: jinja
          jinja: |
            {% if foxyproxy.proxy.type not in ['HTTP', 'HTTPS/SSL', 'SOCKS5', 'SOCKS4'] %}
            proxy does not need username
            {% endif %}
      password:
        description: Password
        type: secret
        disabled:
          type: jinja
          jinja: |
            {% if foxyproxy.proxy.type not in ['HTTP', 'HTTPS/SSL', 'SOCKS5', 'SOCKS4'] %}
            proxy does not need password
            {% endif %}
      url:
        type: web_address
        disabled:
          type: jinja
          jinja: |
            {% if foxyproxy.proxy.type not in ['PAC URL', 'WPAD'] %}
            proxy does not need url
            {% endif %}


A few comments:

- in the `foxyproxy.proxy` :term:`leader` family there is a variable named `type` (line 4), this may conflict with the `type` attribute (specified line 10). In this case, to specify the type we use the `_type` attribute
- a :term:`follower` variable can also be multiple
  (which is the case for `foxyproxy.proxy.address`)
- `foxyproxy.proxy.username` (line 62) becomes :term:`mandatory` if `foxyproxy.proxy.password`
  is specified, in fact a password without a username is meaningless

Let's test it:

>>> from rougail import Rougail, RougailConfig
>>> from pprint import pprint
>>> RougailConfig['dictionaries_dir'] = ['dict']
>>> RougailConfig['extra_dictionaries']['foxyproxy'] = ['foxyproxy/']
>>> rougail = Rougail()
>>> config = rougail.get_config()
>>> config.option('rougail.proxy.proxy_mode').value.set('Manual proxy configuration')
>>> config.option('rougail.proxy.manual.http_proxy.address').value.set('proxy.example')
>>> config.option('foxyproxy.proxy.title').value.set(['MyProxy'])
>>> config.option('foxyproxy.proxy.type', 0).value.set('HTTP')
>>> config.option('foxyproxy.proxy.color', 0).value.set('#00000')
>>> config.property.read_only()
>>> pprint(config.value.get(), sort_dicts=False)

The output is:

.. code-block:: python

    {'rougail.proxy.proxy_mode': 'Manual proxy configuration',
     'rougail.proxy.manual.http_proxy.address': 'proxy.example',
     'rougail.proxy.manual.http_proxy.port': '8080',
     'rougail.proxy.manual.use_for_https': True,
     'rougail.proxy.manual.ssl_proxy.address': 'proxy.example',
     'rougail.proxy.manual.ssl_proxy.port': '8080',
     'rougail.proxy.manual.socks_proxy.address': None,
     'rougail.proxy.manual.socks_proxy.port': None,
     'rougail.proxy.manual.socks_proxy.version': 'v5',
     'rougail.proxy.no_proxy': [],
     'rougail.proxy.proxy_dns_socks5': False,
     'rougail.proxy.dns_over_https.enable_dns_over_https': False,
     'foxyproxy.proxy.title': [{'foxyproxy.proxy.title': 'MyProxy',
                                'foxyproxy.proxy.color': '#00000',
                                'foxyproxy.proxy.type': 'HTTP',
                                'foxyproxy.proxy.address': ['proxy.example'],
                                'foxyproxy.proxy.port': '8080',
                                'foxyproxy.proxy.username': None,
                                'foxyproxy.proxy.password': None}]}

The choice we made here is to make `foxyproxy.proxy.username` :term:`mandatory` if a password is specified in the `foxyproxy.proxy.password` variable.

It makes sense to have a username without a password (in this case the password will be requested when connecting to the proxy). But the opposite does not make sense.

From a user point of view this may seem disturbing (if you enter the password, you have to return to the previous option to specify the password).

It is possible to reverse the logic. If the `foxyproxy.proxy.username` variable is set, the `foxyproxy.proxy.password` variable becomes editable.

None of this two variables needs to be :term:`mandatory`.

If you prefer this option, here is a second extra dictionary :file:`foxyproxy/01-redefine.yml` which will redefine the behavior only of the `foxyproxy.proxy.username` and `foxyproxy.proxy.password` variables:




.. code-block:: yaml
   :caption: the :file:`foxyproxy/01-redefine.yml` file
   :linenos:

    ---
    version: '1.0'
    proxy:
      username:
        redefine: true
        # suppress mandatory constrainte
        mandatory: false
      password:
        redefine: true
        hidden:
          type: jinja
          jinja: |
            {% if not foxyproxy.proxy.username %}
            no username defined
            {% endif %}


**It's up to you to play now !**
