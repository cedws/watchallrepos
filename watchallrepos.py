#!/usr/bin/env python

import os
import asyncio

from argparse import ArgumentParser
from aiohttp import ClientSession

API = "https://api.github.com"

PARSER = ArgumentParser()
PARSER.add_argument(
    "-s", "--skip_forks",
    action="store_true",
    help="skip your repositories which are forks"
)

async def main():
    token = os.environ.get("GITHUB_PA_TOKEN")

    if not token:
        print(
            "You must pass a GitHub personal access token via the "
            "GITHUB_PA_TOKEN environment variable."
        )
        return

    args = PARSER.parse_args()
    headers = {
        "Authorization": "Token {}".format(token)
    }

    async with ClientSession(headers=headers) as client:
        repositories = await repos(client)

        for repo in repositories:
            if args.skip_forks and repo.get("fork"):
                continue

            print("Watching {}".format(repo.get("url")))
            await subscribe(client, repo)

async def repos(client):
    async with client.get("{}/user/repos".format(API)) as resp:
        return await resp.json()

async def subscribe(client, repo):
    await client.put(repo.get("subscription_url"))

if __name__ == "__main__":
    LOOP = asyncio.get_event_loop()
    LOOP.run_until_complete(main())
