Clancy
======

Clancy is a command line client for `Red October <https://github.com/cloudflare/redoctober>`_.

Requirements
------------

* Python 2.7.6+

Installation and Configuration
------------------------------

You can install clancy with pip:

.. code-block:: bash

  pip install clancy

Clancy will look for a YAML file called *config.yaml* in the following locations, in order:

* *./config.yaml* (the current directory)
* *~/.clancy/config.yaml*

You can set default values for the cacert, server and user arguments. This can save a lot of typing time! Here is an example config file:

.. code-block:: yaml

  ---
  user: MyRedOctoberUsername
  cacert: /etc/ssl/certs/my_cacert.pem
  server: redoctober.mydomain.local

Command line arguments override the config file.

Using Clancy
------------

Here are some sample invocations. For brevity, these examples assume a config file with *server* and *cacert*. Run *clancy --help* for more details.

Initialize New Vault
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

  ~$ clancy create

Delegate
~~~~~~~~

.. code-block:: bash

  ~$ clancy delegate --time 1h30m --uses 1

  # As a different user
  ~$ clancy delegate --user hsolo --time 1h30m --uses 1

Encrypt Data
~~~~~~~~~~~~

.. code-block:: bash

  ~$ clancy base64-encode
  String to encode: Why is a raven like a writing desk?
  
  Base64
  ------
  V2h5IGlzIGEgcmF2ZW4gbGlrZSBhIHdyaXRpbmcgZGVzaz8=
  
  ~$ clancy encrypt --owners pliu,hsolo,wantilles --min 2 --str V2h5IGlzIGEgcmF2ZW4gbGlrZSBhIHdyaXRpbmcgZGVzaz8=

  ... snip ...
  
  Server Response
  ---------------
  {
    "Response": "eyJWZXJzaW9uIjoxLCJWYXVsdElkIjoxMzA0MTU0NDExLCJLZXlTZXQiOlt7Ik5hbWUiOlsiYWRtaW4xIiwiYWRtaW4yIl0sIktleSI6IjhCbjI3RElLM2RxQk4vQ2FZVmZ1dHc9PSJ9LHsiTmFtZSI6WyJhZG1pbjEiLCJwbGl1Il0sIktleSI6IkpiaUpTS2Vibnhma1ZpbTRGN1dISVE9PSJ9LHsiTmFtZSI6WyJhZG1pbjIiLCJhZG1pbjEiXSwiS2V5IjoiQ2NjL0FkRkhNTjl5OHV4TmJmMEx2dz09In0seyJOYW1lIjpbImFkbWluMiIsInBsaXUiXSwiS2V5IjoiYm9nRUxkZDFpNkhQRzRDTVYxSHF2Zz09In0seyJOYW1lIjpbInBsaXUiLCJhZG1pbjEiXSwiS2V5IjoibmR4UFdUTk12azdoTW5FRElNSFFDUT09In0seyJOYW1lIjpbInBsaXUiLCJhZG1pbjIiXSwiS2V5IjoiZEdzOVkrcThXOU56eG1XK2RUaTJqdz09In1dLCJLZXlTZXRSU0EiOnsiYWRtaW4xIjp7IktleSI6IlFRUVB0a0RCc1BNWEoxTy96ZDFZT3VQRFpkRDNqejdEWmRlT3BORzdYWDdyTXJFMC8wMFJkcWhSNjFxaExub05MMktvdEdmMEV1a2FnZlJjcXUxVS9MYW0zY2prOTJGU1RiL3JwZGloam5DZG0yVFJRQmE4bXVXWWdzMFZYTzZrWVVPVmJQV3dZNExSTEdPaFpvRXpuc0JqRit1WVY4aXhjZFRMbzBXU25HWHFrdHNXeFNrPSJ9LCJhZG1pbjIiOnsiS2V5IjoiUVFUS3QrYk5wSVkzZ2k1Tm4zb05tS0tmZlQ0MGtOV1NSdlRyQW1KODkvanZFL3gxMGh1Z2tzUDI3dlJBY0txN3RHaEo0SWNMcmxNdmh2REJWZGJnWHlTRHFUOWlqU2E2Z1JnL1dFYWNQd2VidjE0QmFCSnBtekVDQlNxWStHb2tmdkMvbmJ3V09xaHFTWFBjK0tPaVdLb054Y0E3YVVGQWN2NlNleGRpU05ucjdaV3Fxcms9In0sInBsaXUiOnsiS2V5IjoiUVFTb2hpWFhGa0J1S2cvaVFYU2RBWXEzMHVaWm5UUXljQ3NUTmY1TWpNOXNKczEwQmxPTGNYb1NoYTk3ZzR1SGdjcnl1TVRkMmZaYWN2dGFCZk9TLzdKM0g3cGxNOSs4dnlySVFwdnpubVYxQjBnUkRja3M2SnkwVWxKaldLdjRxTGVUcklsRHVuTmlpbHJaVTk4Nk1lQ0xwOTRiZ1BvRTRGNFVDelBNamVyZ0dobTdNOG89In19LCJJViI6IlVieElJTVEzWVBVRUdEUHFhNS9qR1E9PSIsIkRhdGEiOiJuZzRBYm9MdWIrQ2lJeWVvRVNUVmNSaGFCMWh4U0ZZdWRqVEkzSnpRSWh0dGMvenB5ZE1aV2p6cnNBcWU5M2JEIiwiU2lnbmF0dXJlIjoiR29vUmZ3TGljcW1vZEZxZnBaWmpQME1BdGJFPSJ9", 
    "Status": "ok"
  }

Decrypt Data
~~~~~~~~~~~~

.. code-block:: bash

  ~$ echo -n "eyJWZXJzaW9uIjoxLCJWYXVsdElkIjoxMzA0MTU0NDExLCJLZXlTZXQiOlt7Ik5hbWUiOlsiYWRtaW4xIiwiYWRtaW4yIl0sIktleSI6IjhCbjI3RElLM2RxQk4vQ2FZVmZ1dHc9PSJ9LHsiTmFtZSI6WyJhZG1pbjEiLCJwbGl1Il0sIktleSI6IkpiaUpTS2Vibnhma1ZpbTRGN1dISVE9PSJ9LHsiTmFtZSI6WyJhZG1pbjIiLCJhZG1pbjEiXSwiS2V5IjoiQ2NjL0FkRkhNTjl5OHV4TmJmMEx2dz09In0seyJOYW1lIjpbImFkbWluMiIsInBsaXUiXSwiS2V5IjoiYm9nRUxkZDFpNkhQRzRDTVYxSHF2Zz09In0seyJOYW1lIjpbInBsaXUiLCJhZG1pbjEiXSwiS2V5IjoibmR4UFdUTk12azdoTW5FRElNSFFDUT09In0seyJOYW1lIjpbInBsaXUiLCJhZG1pbjIiXSwiS2V5IjoiZEdzOVkrcThXOU56eG1XK2RUaTJqdz09In1dLCJLZXlTZXRSU0EiOnsiYWRtaW4xIjp7IktleSI6IlFRUVB0a0RCc1BNWEoxTy96ZDFZT3VQRFpkRDNqejdEWmRlT3BORzdYWDdyTXJFMC8wMFJkcWhSNjFxaExub05MMktvdEdmMEV1a2FnZlJjcXUxVS9MYW0zY2prOTJGU1RiL3JwZGloam5DZG0yVFJRQmE4bXVXWWdzMFZYTzZrWVVPVmJQV3dZNExSTEdPaFpvRXpuc0JqRit1WVY4aXhjZFRMbzBXU25HWHFrdHNXeFNrPSJ9LCJhZG1pbjIiOnsiS2V5IjoiUVFUS3QrYk5wSVkzZ2k1Tm4zb05tS0tmZlQ0MGtOV1NSdlRyQW1KODkvanZFL3gxMGh1Z2tzUDI3dlJBY0txN3RHaEo0SWNMcmxNdmh2REJWZGJnWHlTRHFUOWlqU2E2Z1JnL1dFYWNQd2VidjE0QmFCSnBtekVDQlNxWStHb2tmdkMvbmJ3V09xaHFTWFBjK0tPaVdLb054Y0E3YVVGQWN2NlNleGRpU05ucjdaV3Fxcms9In0sInBsaXUiOnsiS2V5IjoiUVFTb2hpWFhGa0J1S2cvaVFYU2RBWXEzMHVaWm5UUXljQ3NUTmY1TWpNOXNKczEwQmxPTGNYb1NoYTk3ZzR1SGdjcnl1TVRkMmZaYWN2dGFCZk9TLzdKM0g3cGxNOSs4dnlySVFwdnpubVYxQjBnUkRja3M2SnkwVWxKaldLdjRxTGVUcklsRHVuTmlpbHJaVTk4Nk1lQ0xwOTRiZ1BvRTRGNFVDelBNamVyZ0dobTdNOG89In19LCJJViI6IlVieElJTVEzWVBVRUdEUHFhNS9qR1E9PSIsIkRhdGEiOiJuZzRBYm9MdWIrQ2lJeWVvRVNUVmNSaGFCMWh4U0ZZdWRqVEkzSnpRSWh0dGMvenB5ZE1aV2p6cnNBcWU5M2JEIiwiU2lnbmF0dXJlIjoiR29vUmZ3TGljcW1vZEZxZnBaWmpQME1BdGJFPSJ9" > crypted.txt

  # Encrypt and decrypt can read from files too.
  ~$ clancy decrypt --file crypted.txt 

  ... snip ...

  {
    "Response": "V2h5IGlzIGEgcmF2ZW4gbGlrZSBhIHdyaXRpbmcgZGVzaz8=", 
    "Status": "ok"
  }

View Summary, Modify User, Change Password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

  ~$ clancy summary
  ~$ clancy modify --action revoke --target dvader
  ~$ clancy change-password
