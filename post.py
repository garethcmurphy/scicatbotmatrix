#!/usr/bin/env python3
"""scicatbot"""
import requests

class ScicatBot():
    """scicatbot"""
    url = "https://scitest.esss.lu.se/_matrix/client/r0"

    def read_config(self):
        """read config"""
        with open("config.json") as json_file:
            data = json.load(json_file)
            username = data["username"]
            password = data["password"]

    def login(self):
        """login"""
        url = self.url + "/login"
        data = {"type":"m.login.password", "user":"scicatbot", "password":"scicatbot"} 
        response = requests.post(url, json=data)
        token = response.json()
        self.token = token["access_token"]

    def post(self):
        """post"""
        roomid = "!vbGjwTjpOplTnnLFZR:synapse"

        url = self.url + "/rooms/"+roomid+"/send/m.room.message?access_token=" + self.token
        filename  = "nicos_00000788.hdf"
        scicat_url = "https://scicat.esss.se/datasets/20.500.12269%2F788nicos_00000788.hdf"
        data = {"msgtype":"m.text", "body":"The file " + filename + " was created. See " + scicat_url+ " for details"}
        print(url)
        response = requests.post(url, json=data)
        token = response.json()
        print(token)


def main():
    """main"""
    bot  = ScicatBot()
    bot.login()
    bot.post()

if __name__ == "__main__":
    main()