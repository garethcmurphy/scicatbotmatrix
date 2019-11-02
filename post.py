#!/usr/bin/env python3
"""scicatbot"""
import urllib
import json
import requests


class ScicatBot():
    """scicatbot"""
    url = "https://scitest.esss.lu.se/_matrix/client/r0"
    username = ""
    password = ""

    def read_config(self):
        """read config"""
        with open("config.json") as json_file:
            data = json.load(json_file)
            self.username = data["username"]
            self.password = data["password"]

    def login(self):
        """login"""
        url = self.url + "/login"
        self.read_config()
        data = {"type": "m.login.password",
                "user": self.username, "password": self.password}
        response = requests.post(url, json=data)
        token = response.json()
        self.token = token["access_token"]

    def post(self, room_id):
        """post"""
        url = self.create_url("/rooms/"+room_id + "/send/m.room.message")
        filename = "nicos_00000788.hdf"
        scicat_url = "https://scicat.esss.se/datasets/20.500.12269%2F788nicos_00000788.hdf"
        data = {"msgtype": "m.text", "body": "The file " + filename +
                " was created. See " + scicat_url + " for details"}
        print(url)
        response = requests.post(url, json=data)
        token = response.json()
        print(token)

    def create_room(self, alias, proposal_id, proposal_topic):
        """create room"""
        url = self.create_url("/createRoom")
        guests = ["@garethmurphy:synapse"]
        data = {"room_alias_name": proposal_id,
                "topic": proposal_topic,
                "name": proposal_id,
                "invite": guests}
        print(data)
        response = requests.post(url, json=data)
        token = response.json()
        print(token)

    def create_url(self, api_call):
        """create url"""
        url = self.url + api_call + "?access_token=" + self.token
        return url

    def get_room_id(self, room_alias):
        room_alias_encode = urllib.parse.quote(room_alias)
        url = self.create_url("/directory/room/"+room_alias_encode)
        response = requests.get(url)
        response_json = response.json()
        print(url)
        print(response_json)
        room_id = response_json.get("room_id")
        return room_id

    def invite(self, room_id, user_id):
        """invite"""
        url = self.create_url("/rooms/" + room_id + "/invite")
        data = {"user_id": "@garethmurphy:synapse"}
        response = requests.post(url, json=data)
        token = response.json()
        print(token)


def main():
    """main"""
    bot = ScicatBot()
    bot.login()
    # bot.post()
    proposal_topic = "Investigation of water"
    proposal_id = "QHK123"
    room_alias = "#"+proposal_id+":synapse"
    # bot.create_room(room_alias, proposal_id, proposal_topic)
    room_id = bot.get_room_id(room_alias)
    bot.post(room_id)
    # username = "@garethmurphy:synapse"
    # bot.invite(room_id, username)


if __name__ == "__main__":
    main()
