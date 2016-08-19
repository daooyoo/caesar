#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from caesar import encrypt

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Caesar</title>
        <style>
            form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
            }
            textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
            }
            p.error {
                color: red;
            }
        </style>
    </head>
<body>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

rot_form = """
<form method="post">
    <div>
        <label for="rot">Rotate by:</label>
        <input type="text" name="rot" value="{0}">
        <p class="error">{1}</p>
    </div>
    <textarea type="text" name="text">{2}</textarea>
    <br>
    <input type="submit">
</form>
"""

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/'
    """

    def get(self):
        error = self.request.get("error")

        response = page_header + rot_form.format(0, error, "") + page_footer

        self.response.write(response)

    def post(self):
        text = self.request.get("text")
        rot_value = self.request.get("rot")

        if not rot_value.isdigit():
            error = "Please enter an integer amount"
            self.redirect("/?error=" + error)

        rot_value = int(rot_value)
        answer = encrypt(text, rot_value)

        response = page_header + rot_form.format(rot_value, "", cgi.escape(answer)) + page_footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index),
], debug=True)
