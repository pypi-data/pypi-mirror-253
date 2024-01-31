# -*- encoding: utf-8 -*-
import sys

import requests

from suite_py.lib import logger
from suite_py.lib.handler.github_handler import GithubHandler


class CaptainHook:
    def __init__(self, config, tokens=None):
        self._baseurl = config.user["captainhook_url"]
        self._timeout = config.user["captainhook_timeout"]
        self._okta_base_url = config.okta["base_url"]
        self._okta_token = config.get_cache(f"{self._okta_base_url}_token")
        self._headers = {
            "Authorization": f"Bearer {self._okta_token}",
        }

        if tokens is not None:
            self._github = GithubHandler(tokens)

    def lock_project(self, project, env):
        data = {
            "project": project,
            "status": "locked",
            "user": self._get_user(),
            "environment": env,
        }
        return self.send_post_request("/projects/manage-lock", data)

    def unlock_project(self, project, env):
        data = {
            "project": project,
            "status": "unlocked",
            "user": self._get_user(),
            "environment": env,
        }
        return self.send_post_request("/projects/manage-lock", data)

    def status(self, project, env):
        return self.send_get_request(
            f"/projects/check?project={project}&environment={env}"
        )

    def check(self):
        return requests.get(f"{self._baseurl}/", timeout=(2, self._timeout))

    def get_users_list(self):
        return self.send_get_request("/users/all")

    def aggregators(self):
        return self.send_get_request("/cloudflare/aggregators/available")

    def change_aggregator(self, aggregator, qa_address):
        data = {"aggregator": aggregator, "qa_address": qa_address}
        return self.send_put_request("/cloudflare/aggregators", data)

    def send_post_request(self, endpoint, data):
        try:
            r = requests.post(
                f"{self._baseurl}{endpoint}",
                headers=self._headers,
                data=data,
                timeout=self._timeout,
            )

            return self._response(r)
        except Exception:
            logger.error("Unable to contact Captainhook, are you using the VPN?")
            sys.exit(-1)

    def send_put_request(self, endpoint, data):
        try:
            r = requests.put(
                f"{self._baseurl}{endpoint}",
                headers=self._headers,
                data=data,
                timeout=self._timeout,
            )

            return self._response(r)
        except Exception:
            logger.error("Unable to contact Captainhook, are you using the VPN?")
            sys.exit(-1)

    def send_get_request(self, endpoint):
        try:
            r = requests.get(
                f"{self._baseurl}{endpoint}",
                headers=self._headers,
                timeout=(2, self._timeout),
            )

            return self._response(r)
        except Exception:
            logger.error("Unable to contact Captainhook, are you using the VPN?")
            sys.exit(-1)

    def _response(self, response):
        if response.status_code == 401:
            logger.error("Unauthorized. Are you logged in?")
            sys.exit(-1)

        return response

    def set_timeout(self, timeout):
        self._timeout = timeout

    def _get_user(self):
        return self._github.get_user().login
