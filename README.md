Clancy
======

Clancy is a command line client for [Red October](https://github.com/cloudflare/redoctober).

## Installing
Just clone the repo and install requirements. Clancy is written for `Python 2.7`.

```bash
~$ git clone git@github.com:pwyliu/clancy.git
~$ pip install -r requirements.txt
```

## Config File

Clancy will look for a JSON file called `clancy.conf` in the following locations, in order:

* `./clancy.conf` (the current directory)
* `~/.clancy/clancy.conf`
* `/etc/clancy/clancy.conf`

You can set a default for any optional command line argument. Typically you will just want to set `--server` and `--cacert` but you can also set other things like `--user` if your Red October username is not the same as your shell username.

An example config file:

```json
{
  "_comment": "CLI params will override these settings.",
  "--user": "SomeDifferentUsername",
  "--server": "redoctober.mydomain.local",
  "--cacert": "/etc/ssl/certs/my_cacert.crt"
}
```

## Using Clancy

Here are some sample invocations. For brevity, these examples assume a config file with `--server` and `--cacert` set. For more details, run `clancy --help` for help.

#### Initialize a new vault
```bash
~$ clancy create

Enter password
--------------
User: pliu
Password: 

Server Response
---------------
{
  "Status": "ok"
}
```

#### Delegate a key
```bash
~$ clancy delegate --time 1h30m --uses 1

Enter password
--------------
User: pliu
Password: 

Server Response
---------------
{
  "Status": "ok"
}

# As a different user
~$ clancy delegate --user admin1 --time 1h30m --uses 1

Enter password
--------------
User: admin1
Password:

Server Response
---------------
{
  "Status": "ok"
}
```

#### Encrypt data
```bash
# String: Why is a raven like a writing desk?
~$ clancy base64-encode
String to encode: 
V2h5IGlzIGEgcmF2ZW4gbGlrZSBhIHdyaXRpbmcgZGVzaz8=

~$ clancy encrypt --owners pliu,admin1,admin2 --min 2 --str V2h5IGlzIGEgcmF2ZW4gbGlrZSBhIHdyaXRpbmcgZGVzaz8=

Enter password
--------------
User: pliu
Password: 

Server Response
---------------
{
  "Response": "eyJWZXJzaW9uIjoxLCJWYXVsdElkIjoxMzA0MTU0NDExLCJLZXlTZXQiOlt7Ik5hbWUiOlsiYWRtaW4xIiwiYWRtaW4yIl0sIktleSI6IjhCbjI3RElLM2RxQk4vQ2FZVmZ1dHc9PSJ9LHsiTmFtZSI6WyJhZG1pbjEiLCJwbGl1Il0sIktleSI6IkpiaUpTS2Vibnhma1ZpbTRGN1dISVE9PSJ9LHsiTmFtZSI6WyJhZG1pbjIiLCJhZG1pbjEiXSwiS2V5IjoiQ2NjL0FkRkhNTjl5OHV4TmJmMEx2dz09In0seyJOYW1lIjpbImFkbWluMiIsInBsaXUiXSwiS2V5IjoiYm9nRUxkZDFpNkhQRzRDTVYxSHF2Zz09In0seyJOYW1lIjpbInBsaXUiLCJhZG1pbjEiXSwiS2V5IjoibmR4UFdUTk12azdoTW5FRElNSFFDUT09In0seyJOYW1lIjpbInBsaXUiLCJhZG1pbjIiXSwiS2V5IjoiZEdzOVkrcThXOU56eG1XK2RUaTJqdz09In1dLCJLZXlTZXRSU0EiOnsiYWRtaW4xIjp7IktleSI6IlFRUVB0a0RCc1BNWEoxTy96ZDFZT3VQRFpkRDNqejdEWmRlT3BORzdYWDdyTXJFMC8wMFJkcWhSNjFxaExub05MMktvdEdmMEV1a2FnZlJjcXUxVS9MYW0zY2prOTJGU1RiL3JwZGloam5DZG0yVFJRQmE4bXVXWWdzMFZYTzZrWVVPVmJQV3dZNExSTEdPaFpvRXpuc0JqRit1WVY4aXhjZFRMbzBXU25HWHFrdHNXeFNrPSJ9LCJhZG1pbjIiOnsiS2V5IjoiUVFUS3QrYk5wSVkzZ2k1Tm4zb05tS0tmZlQ0MGtOV1NSdlRyQW1KODkvanZFL3gxMGh1Z2tzUDI3dlJBY0txN3RHaEo0SWNMcmxNdmh2REJWZGJnWHlTRHFUOWlqU2E2Z1JnL1dFYWNQd2VidjE0QmFCSnBtekVDQlNxWStHb2tmdkMvbmJ3V09xaHFTWFBjK0tPaVdLb054Y0E3YVVGQWN2NlNleGRpU05ucjdaV3Fxcms9In0sInBsaXUiOnsiS2V5IjoiUVFTb2hpWFhGa0J1S2cvaVFYU2RBWXEzMHVaWm5UUXljQ3NUTmY1TWpNOXNKczEwQmxPTGNYb1NoYTk3ZzR1SGdjcnl1TVRkMmZaYWN2dGFCZk9TLzdKM0g3cGxNOSs4dnlySVFwdnpubVYxQjBnUkRja3M2SnkwVWxKaldLdjRxTGVUcklsRHVuTmlpbHJaVTk4Nk1lQ0xwOTRiZ1BvRTRGNFVDelBNamVyZ0dobTdNOG89In19LCJJViI6IlVieElJTVEzWVBVRUdEUHFhNS9qR1E9PSIsIkRhdGEiOiJuZzRBYm9MdWIrQ2lJeWVvRVNUVmNSaGFCMWh4U0ZZdWRqVEkzSnpRSWh0dGMvenB5ZE1aV2p6cnNBcWU5M2JEIiwiU2lnbmF0dXJlIjoiR29vUmZ3TGljcW1vZEZxZnBaWmpQME1BdGJFPSJ9", 
  "Status": "ok"
}
```

#### Decrypt data
```bash
~$ echo -n "eyJWZXJzaW9uIjoxLCJWYXVsdElkIjoxMzA0MTU0NDExLCJLZXlTZXQiOlt7Ik5hbWUiOlsiYWRtaW4xIiwiYWRtaW4yIl0sIktleSI6IjhCbjI3RElLM2RxQk4vQ2FZVmZ1dHc9PSJ9LHsiTmFtZSI6WyJhZG1pbjEiLCJwbGl1Il0sIktleSI6IkpiaUpTS2Vibnhma1ZpbTRGN1dISVE9PSJ9LHsiTmFtZSI6WyJhZG1pbjIiLCJhZG1pbjEiXSwiS2V5IjoiQ2NjL0FkRkhNTjl5OHV4TmJmMEx2dz09In0seyJOYW1lIjpbImFkbWluMiIsInBsaXUiXSwiS2V5IjoiYm9nRUxkZDFpNkhQRzRDTVYxSHF2Zz09In0seyJOYW1lIjpbInBsaXUiLCJhZG1pbjEiXSwiS2V5IjoibmR4UFdUTk12azdoTW5FRElNSFFDUT09In0seyJOYW1lIjpbInBsaXUiLCJhZG1pbjIiXSwiS2V5IjoiZEdzOVkrcThXOU56eG1XK2RUaTJqdz09In1dLCJLZXlTZXRSU0EiOnsiYWRtaW4xIjp7IktleSI6IlFRUVB0a0RCc1BNWEoxTy96ZDFZT3VQRFpkRDNqejdEWmRlT3BORzdYWDdyTXJFMC8wMFJkcWhSNjFxaExub05MMktvdEdmMEV1a2FnZlJjcXUxVS9MYW0zY2prOTJGU1RiL3JwZGloam5DZG0yVFJRQmE4bXVXWWdzMFZYTzZrWVVPVmJQV3dZNExSTEdPaFpvRXpuc0JqRit1WVY4aXhjZFRMbzBXU25HWHFrdHNXeFNrPSJ9LCJhZG1pbjIiOnsiS2V5IjoiUVFUS3QrYk5wSVkzZ2k1Tm4zb05tS0tmZlQ0MGtOV1NSdlRyQW1KODkvanZFL3gxMGh1Z2tzUDI3dlJBY0txN3RHaEo0SWNMcmxNdmh2REJWZGJnWHlTRHFUOWlqU2E2Z1JnL1dFYWNQd2VidjE0QmFCSnBtekVDQlNxWStHb2tmdkMvbmJ3V09xaHFTWFBjK0tPaVdLb054Y0E3YVVGQWN2NlNleGRpU05ucjdaV3Fxcms9In0sInBsaXUiOnsiS2V5IjoiUVFTb2hpWFhGa0J1S2cvaVFYU2RBWXEzMHVaWm5UUXljQ3NUTmY1TWpNOXNKczEwQmxPTGNYb1NoYTk3ZzR1SGdjcnl1TVRkMmZaYWN2dGFCZk9TLzdKM0g3cGxNOSs4dnlySVFwdnpubVYxQjBnUkRja3M2SnkwVWxKaldLdjRxTGVUcklsRHVuTmlpbHJaVTk4Nk1lQ0xwOTRiZ1BvRTRGNFVDelBNamVyZ0dobTdNOG89In19LCJJViI6IlVieElJTVEzWVBVRUdEUHFhNS9qR1E9PSIsIkRhdGEiOiJuZzRBYm9MdWIrQ2lJeWVvRVNUVmNSaGFCMWh4U0ZZdWRqVEkzSnpRSWh0dGMvenB5ZE1aV2p6cnNBcWU5M2JEIiwiU2lnbmF0dXJlIjoiR29vUmZ3TGljcW1vZEZxZnBaWmpQME1BdGJFPSJ9" > crypted.txt

# Encrypt and decrypt can read in from files too.
~$ clancy decrypt --file crypted.txt 

Enter password
--------------
User: pliu
Password: 

Server Response
---------------
{
  "Response": "V2h5IGlzIGEgcmF2ZW4gbGlrZSBhIHdyaXRpbmcgZGVzaz8=", 
  "Status": "ok"
}
```

#### View summary
```bash
~$ clancy summary

Enter password
--------------
User: pliu
Password: 

Server Response
---------------
{
  "All": {
    "admin1": {
      "Admin": false, 
      "Type": "ECC"
    }, 
    "admin2": {
      "Admin": false, 
      "Type": "ECC"
    }, 
    "pliu": {
      "Admin": true, 
      "Type": "ECC"
    }
  }, 
  "Live": {
    "admin1": {
      "Admin": false, 
      "Expiry": "2014-05-24T03:59:37.798097798-04:00", 
      "Type": "ECC", 
      "Uses": 9
    }, 
    "admin2": {
      "Admin": false, 
      "Expiry": "2014-05-24T03:59:43.918287951-04:00", 
      "Type": "ECC", 
      "Uses": 9
    }, 
    "pliu": {
      "Admin": true, 
      "Expiry": "2014-05-24T00:13:50.772676238-04:00", 
      "Type": "ECC", 
      "Uses": 1
    }
  }, 
  "Status": "ok"
}
```

#### Modify a user
```bash
(clancy)pliu@behemoth:~/projects/clancy$ ./clancy modify --action revoke --target admin2

Enter password
--------------
User: pliu
Password: 

Server Response
---------------
{
  "Status": "ok"
}
```

#### Change your password
```bash
~$ clancy change-password

Enter password
--------------
User: pliu
Password: 
New Password: 

Server Response
---------------
{
  "Status": "ok"
}
```
