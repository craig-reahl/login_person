Latching onto a Reahl [SystemAccount](https://www.reahl.org/docs/6.1/domain/systemaccountmodel.d.html#module-reahl.domain.systemaccountmodel)
=====================================


This example builds on the [login1bootstrap](https://www.reahl.org/docs/6.1/tutorial/loggingin.d.html) tutorial found in Reahl.

The __Person__ object creates a relationship to `reahl.domain.systemaccountmodel.EmailAndPasswordSystemAccount`

The file `login_person.py` resembles the login1bootstrap.py file from the tutorial. 
This file utilises the PersonFactory that resides in file `login_model.py`, to manage `Person` objects.

The Person class was added to setup.cfg: 

```
persisted = ["login_model:Person",]
```

Note:
=====

To serve the project with only HTTP this config was added to `etc/web.config.py`:

```
web.encrypted_http_port = 8383
web.encrypted_http_scheme = 'http'
```

This ensures when the web framework redirects the browser to a secure scheme, that it stays on HTTP and does not
go to HTTPS for the sensitive part of the web application. This switching to HTTPS protocol will be removed in a future web framework release as most sites should only be on HTTPS by now.


