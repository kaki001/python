#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import types
import shutil
import os
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

userBaseUrl = 'http://gitlab.url/api/v3/users/';
token = '?private_token=gitlabadmintoken';

userInfoDic = {};
with open('userinfo.txt', 'r') as f:
    for line in f:
        splitLine = line.split(",");
        userInfoDic[splitLine[0]] = splitLine[1];

for gitUid, username in userInfoDic.iteritems() :
    userSshKeysUrl = userBaseUrl + str(gitUid) + "/keys" + token
    userSshCont = requests.get(userSshKeysUrl).content;
    userSshJson = json.loads(userSshCont);

    if type(userSshJson) is types.DictType :
        print("No git user info : " + gitUid + " : " + username)
    else :
        if len(userSshJson) != 0 :
            userInfoKeysUrl = userBaseUrl + str(gitUid) + token;
            userInfoCont = requests.get(userInfoKeysUrl).content;
            userInfoJson = json.loads(userInfoCont)
            username = userInfoJson[u'username'];
            # print userSshJson;
            userKeyPath = "user/"+ username;
            if not os.path.isdir(userKeyPath):
                os.makedirs(userKeyPath);
            else:
                shutil.rmtree(userKeyPath, ignore_errors=True);
                os.makedirs(userKeyPath);

            f = open(userKeyPath + "/authorized_keys", 'w');
            for sshObj in userSshJson:
                sshKey = sshObj[u'key'];
                f.write(str(sshKey));
            f.close();
        else :
            print("No git keys info : " + gitUid + " : " + username)
