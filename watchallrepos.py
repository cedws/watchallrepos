#!/usr/bin/env python

import os
import asyncio

from aiohttp import ClientSession
from argparse import ArgumentParser

API = "https://api.github.com"

parser = ArgumentParser()
parser.add_argument(
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

	args = parser.parse_args()

	async with ClientSession(headers={
		"Authorization": "token {}".format(token)
	}) as client:
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
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())