# Basic OAuth 2.0 Support for [Web.py](http://webpy.org/)

Implement basic OAuth 2.0 support for web.py. Inspired by [simpleauth](https://github.com/crhym3/simpleauth).

## Supported providers:

  - Google (OAuth 2.0)

    - Doc:

      - [Using OAuth 2.0 for Web Server Applications](https://developers.google.com/accounts/docs/OAuth2WebServer)

      - [Using OAuth 2.0 for Login](https://developers.google.com/accounts/docs/OAuth2Login)

    - Create App & Get client ID/Secret:

      - [Google Cloud Console](https://cloud.google.com/console)

    - Scopes:

      - `https://www.googleapis.com/auth/userinfo.profile`: Userinfo - Profile

      - `https://www.googleapis.com/auth/userinfo.email`: Userinfo - Email

      - Reference: [List of Google OAuth Scopes](http://www.subinsb.com/2013/04/list-google-oauth-scopes.html)

  - Facebook (OAuth 2.0)

    - Doc:

      - [The Login Flow for Web (without JavaScript SDK)](https://developers.facebook.com/docs/facebook-login/login-flow-for-web-no-jssdk/)

    - Create App & Get client ID/Secret:

      - [Facebook Developers](https://developers.facebook.com/apps)

    - Scopes:

      - `email`: Provides access to the primary email address of the user in the email property.

      - `user_about_me`: Provides access to the "About Me" section of the profile in the about property

      - Reference: [Permissions](https://developers.facebook.com/docs/facebook-login/permissions/)

## Dependency

  - Web.py: see [Web.py Install Guide](http://webpy.org/install) to install web.py.

## Usage & Example

1. Create app & get client id/secret from providers. (Google: [Google Cloud Console](https://cloud.google.com/console), Facebook: [Facebook Developers](https://developers.facebook.com/apps))

2. Put `auth.py` in your project root dir, and also add your project root dir to sys path. `auth.py` handles OAuth 2.0 process for you, and you do not need to modify this script.

3. In you main python script, create a request handler by subclassing `auth.handler`. Set url routing and client id/secret. Please refer to `login.py` for a complete example.

4. You can run the example (remember to modify app id/secret and `callback_uri` function in the exmaple) by the following bash command:
```bash
$ python login.py
```

## References

  - [SimpleAuth](https://github.com/crhym3/simpleauth)

  - [Facebook login on top of webpy](http://matteolandi.blogspot.tw/2012/09/facebook-login-on-top-of-webpy.html)

  - [Facebook OAuth Example](http://facebook-python-library.docs-library.appspot.com/facebook-python/examples/oauth.html)

## Other

This project is released in public domain, see [UNLICENSE](http://unlicense.org/)
