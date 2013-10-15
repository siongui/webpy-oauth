#!/usr/bin/env python
# -*- coding:utf-8 -*-

import web
import json
import auth


# create Google app & get app ID/secret from:
# https://cloud.google.com/console
auth.parameters['google']['app_id'] = 'google-client-id'
auth.parameters['google']['app_secret'] = 'google-client-secret'

# create Facebook app & get app ID/secret from:
# https://developers.facebook.com/apps
auth.parameters['facebook']['app_id'] = 'facebook-client-id'
auth.parameters['facebook']['app_secret'] = 'facebook-client-secret'


urls = (
  r"/", "LoginPage",
  r"/logout", "LogoutPage",
  r"/auth/(google|facebook)", "AuthPage",
  r"/auth/(google|facebook)/callback", "AuthCallbackPage",
)


class handler(auth.handler):
  def callback_uri(self, provider):
    """Please return appropriate url according to your app setting.
    """
    return 'http://localhost:8080/auth/%s/callback' % provider

  def on_signin(self, provider, profile):
    """Callback when the user successfully signs in the account of the provider
    (e.g., Google account or Facebook account).

    Arguments:
      provider: google or facebook
      profile: the user profile of Google or facebook account of the user who
               signs in.
    """
    user_id = '%s:%s' % (provider, profile['id'])

    # set '_id' in the cookie to sign-in the user in our webapp
    web.setcookie('_id', user_id)
    web.setcookie('_profile', json.dumps(profile))

    raise web.seeother('/')


class AuthPage(handler):
  def GET(self, provider):
    self.auth_init(provider)


class AuthCallbackPage(handler):
  def GET(self, provider):
    self.auth_callback(provider)


class LoginPage:
  def GET(self):
    # check '_id' in the cookie to see if the user already sign in
    if web.cookies().get('_id'):
      # user already sign in, retrieve user profile
      profile = json.loads( web.cookies().get('_profile') )
      return """<html><head></head><body>
        <a href="/logout">Logout</a><br />
        Hello <b><i>%s</i></b>, your profile<br />
        %s<br />
      </body></html>
      """ % ( profile['id'], json.dumps(profile) )
    else:
      # user not sing in
      return """<html><head></head><body>
        <a href="/auth/facebook">Facebook Login</a><br />
        <a href="/auth/google">Google Login</a><br />
      </body></html>
      """


class LogoutPage:
  def GET(self):
    # invalidate '_id' in the cookie to logout the user
    web.setcookie('_id', '', 0)
    raise web.seeother('/')


app = web.application(urls, globals())
if __name__ == '__main__':
  app.run()
