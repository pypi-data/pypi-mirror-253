# OpenID Connect Hub

The `oidc_hub` package provides a user-friendly web interface for managing OpenID identities. As an Identity Provider (IdP), this Django project allows users to manage their OpenID credentials and authenticate with these seamlessly.

## Features

- User-Friendly Interface: A clean and intuitive web interface for users to manage their OpenID identities effortlessly.

- OpenID Authentication: Serve as an OpenID Identity Provider, enabling users to utilize their OpenID credentials for authentication across various services.

- Identity Management: Users can create, update, and delete OpenID identities easily through the web interface.

- Security: Implement secure OpenID authentication practices to ensure the safety and privacy of user identities.

## Installation

```shell
pip install oidc-hub
```

### Configuration

Add `oidc_hub` and `oidc_provider` to your `INSTALLED_APPS` in the Django project's settings:

```python
INSTALLED_APPS = [
  # ...
  "oidc_provider",
  "oidc_hub",
  # ...
]
```

### Migrations

Run migrations to create the required database tables:

```shell
python3 manage.py migrate
```

The first time you migrate, an administrator account will be created according to the settings you have specified in a settings module.

The initial migration will use `ADMIN_USERNAME`, `ADMIN_EMAIL` and `ADMIN_PASSWORD` settings or their default values if these settings are not specified.

## Webserver

#### Development

Start the Django development server.

```shell
python3 manage.py runserver
```

## License

This project is licensed under the AGPLv3 License - see the [LICENSE.md](LICENSE.md) file for details.
